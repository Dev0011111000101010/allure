import pytest #, webdriver-manager

def test_is_PYTEST_installed_and_what_version():
    """
    Function requires "import pytest" + #pip3 install pytest
    Function checks if the project has Pytest installed
    And if yes, what version
    The result is output to the console.
    Example: "
    1. "Pytest" installed successfully;
    2. "Pytest" imported successfully;
    3. "Pytest" version is = 7.2.2 "
    """
    if pytest:
        pytest_is_ok = print('\n1. "Pytest" installed successfully; \n'
              '2. "Pytest" imported successfully;  \n'
              '3. "Pytest" version is =', pytest.__version__, '\n')
    else:
        print('\n#"pytest" is not installed/imported')
    assert pytest
test_is_PYTEST_installed_and_what_version()

def test_function():
    print('')
    print('Hi')
    a = 2
    b = 2
    assert a == b