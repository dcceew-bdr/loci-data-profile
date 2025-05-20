# Tests

These tests use Python's [pytest](https://docs.pytest.org/en/stable/) unit test testing framework. The testing files are in this folder beginning with `test_...` and thy can be executed with the command line `pytest` executed in the parent folder to this one. The Python packages required for the tests are listed in `requirement.txt`. 

The data files in `data/` are validated one-by-one in by `test_validate.py` which extracts the expected result - valid or invalid - from the file name.
