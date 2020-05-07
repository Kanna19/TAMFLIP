Make sure you are in the root directory of the project (TAMFLIP) before proceeding.

### Run all test cases
```
 python -m tamflip.tests.test_cases
 ```

### Run a specific test case

```
python -m unittest tamflip.tests.test_cases.TestCases.<test_case_method_name>
```

### Generate coverage report

```
coverage run -m tamflip.tests.test_cases
```

Coverage report can be viewed at `htmlcov/index.html`
