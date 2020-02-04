@echo off
set PYTHONPATH=%CD%

rem ensure packages
pip install -r requirements.txt

rem Validating styleguide I
flake8 --max-line-length=100 engine tests
if %ERRORLEVEL% gtr 0 Exit /B

rem Validating types
mypy --strict engine
if %ERRORLEVEL% gtr 0 Exit /B

rem Validating styleguide II
pylint --rcfile=pylint.rcfile engine tests
if %ERRORLEVEL% gtr 0 Exit /B

rem Checking for vulnerations
bandit -r engine tests
if %ERRORLEVEL% gtr 0 Exit /B

rem Show Complexity > A
radon cc --show-complexity --min B engine

rem Running unittests.
pytest --doctest-modules ^
    --cov=engine --cov-branch --cov-fail-under=100 ^
    --cov-report=xml --cov-report=term --cov-report=html
