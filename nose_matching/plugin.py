import re

from os import path

import nose
from nose.selector import Selector
from nose.plugins import Plugin


class MatchSelector(Selector):
    """ Special selector to allow selective running of tests filtered by method name. """
    def configure(self, config):
        super(MatchSelector, self).configure(config)

        self.classMatch = getattr(config, 'classMatch', None)
        self.directoryMatch = getattr(config, 'directoryMatch', None)
        self.fileMatch = getattr(config, 'fileMatch', None)
        self.functionMatch = getattr(config, 'functionMatch', None)
        self.methodMatch = getattr(config, 'methodMatch', None)
        self.moduleMatch = getattr(config, 'moduleMatch', None)

    def _apply_match(self, wanted, match, mstr):
        if match is None or not wanted:
            return wanted
        else:
            return match.search(mstr)

    def wantClass(self, cls):
        wanted = super(MatchSelector, self).wantClass(cls)

        return self._apply_match(wanted, self.classMatch, cls.__name__)

    def wantDirectory(self, dirname):
        wanted = super(MatchSelector, self).wantDirectory(dirname)

        dirname = path.basename(dirname)

        return self._apply_match(wanted, self.directoryMatch, dirname)
    
    def wantFile(self, fname):
        wanted = super(MatchSelector, self).wantFile(fname)

        fname = path.basename(fname)

        return self._apply_match(wanted, self.fileMatch, fname)

    def wantFunction(self, function):
        wanted = super(MatchSelector, self).wantFunction(function)

        if wanted:
            if hasattr(function, 'compat_func_name'):
                funcname = function.compat_func_name
            else:
                funcname = function.__name__
        
            return self._apply_match(wanted, self.functionMatch, funcname)
        else:
            return False

    def wantMethod(self, method):
        wanted = super(MatchSelector, self).wantMethod(method)

        return self._apply_match(wanted, self.methodMatch, method.__name__)

    def wantModule(self, module):
        wanted = super(MatchSelector, self).wantModule(module)

        return self._apply_match(wanted, self.moduleMatch, module.__name__)


class Matching(Plugin):
    def _compile_match_str(self, mstr):
        compiled = None
        if mstr is not None:
            compiled = re.compile(mstr)

        return compiled

    def configure(self, options, conf):
        super(Matching, self).configure(options, conf)

        if self.enabled:
            self.class_match_re = self._compile_match_str(options.class_match_str)
            self.dir_match_re = self._compile_match_str(options.dir_match_str)
            self.file_match_re = self._compile_match_str(options.file_match_str)
            self.function_match_re = self._compile_match_str(options.function_match_str)
            self.method_match_re = self._compile_match_str(options.method_match_str)
            self.module_match_re = self._compile_match_str(options.module_match_str)

    def options(self, parser, env):
        """ Register command line options """
        super(Matching, self).options(parser, env)

        parser.add_option('--match-class', dest='class_match_str',
                          default=None,
                          help='Regular expression to select valid classes.')

        parser.add_option('--match-dir', dest='dir_match_str',
                          default=None,
                          help='Regular expression to select valid directories.')

        parser.add_option('--match-file', dest='file_match_str',
                          default=None,
                          help='Regular expression to select valid files.')

        parser.add_option('--match-function', dest='function_match_str',
                          default=None,
                          help='Regular expression to select valid functions.')

        parser.add_option('--match-method', dest='method_match_str',
                          default=None,
                          help='Regular expression to select valid methods.')

        parser.add_option('--match-module', dest='module_match_str',
                          default=None,
                          help='Regular expression to select valid modules.')

    def prepareTestLoader(self, loader):
        config = loader.config
        config.classMatch = self.class_match_re
        config.classMatch = self.class_match_re
        config.directoryMatch = self.dir_match_re
        config.fileMatch = self.file_match_re
        config.functionMatch = self.function_match_re
        config.methodMatch = self.method_match_re
        config.moduleMatch = self.module_match_re

        loader.selector = MatchSelector(config)

