nose-matching is a plugin for the [`nose`](https://nose.readthedocs.org/en/latest/) that allows for granular filtering of tests, allowing you to specify filters for tests using different matching logic for classes, directories, files, functions, methods and modules. These are applied *on top* of the normal `--match`, `--include` and `--exclude` logic.

## Installation
As this is a plugin for [`nose`](https://nose.readthedocs.org/en/latest/), you should install that module first before this plugin. This is an alpha version and has not been released on PyPi yet. For now, you can install it by cloning the git repository and running the following command from the root directory:

```
python setup.py install
```

## Use

Once installed, use the `--with-matching` flag to activate the matching plugin, then use one of the `--match-x` switches with a regular expression to match at the level you want. The options are:

```
Options:
  --with-matching       Enable plugin Matching: (no help available)
                        [NOSE_WITH_MATCHING]
  --match-class=CLASS_MATCH_STR
                        Regular expression to select valid classes.
  --match-dir=DIR_MATCH_STR
                        Regular expression to select valid directories.
  --match-file=FILE_MATCH_STR
                        Regular expression to select valid files.
  --match-function=FUNCTION_MATCH_STR
                        Regular expression to select valid functions.
  --match-method=METHOD_MATCH_STR
                        Regular expression to select valid methods.
  --match-module=MODULE_MATCH_STR
                        Regular expression to select valid modules.
```

As an example, consider a test suite arranged as such:

```
test_foo.py
|-- FooTests
| |-- testConstructor
| |-- testRepr
| |-- testAddition
| |-- testSubtraction
| +-- testBug117
|
|-- BarTests
| |-- testConstructor
| |-- testRepr
| |-- testAddition
| |-- testSubtraction
| |-- testBug247
| +-- testBug738
```

If you are are working on overhauling `Foo`, you may not want to run the `BarTests` suite each time, so you can use:

```
nosetests --with-matching --match-class BarTests
```

If you just want to run all the addition tests, you can use"

```
nosetests --with-matching --match-method testAddition
```

If you want to run all bug-related tests, you can use:

```
nosetests --with-matching --method-match testBug*
```

## License
This code is licensed under the [MIT License](https://opensource.org/licenses/MIT). It is also available under the MIT License with a waiver of the copyright notice requirement.
