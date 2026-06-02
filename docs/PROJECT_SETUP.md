# Project Setup and Execution Guide

## Executive Summary

This document defines the reproducible setup procedure for cloning, configuring, and executing the automated test suite in this repository. The instructions are based on the current repository implementation and verified environment metadata captured from the project virtual environment. All statements are tied either to repository source files or to official external documentation.

## Scope and Preconditions

This guide targets the current Windows-oriented workflow used in the repository.

Required software:

1. Git
2. Python 3.12 or newer
3. Google Chrome and or Microsoft Edge
4. PowerShell

Official references:

1. Python downloads and installation guidance: https://www.python.org/downloads/
2. Python virtual environment documentation: https://docs.python.org/3/library/venv.html
3. pip user guide: https://pip.pypa.io/en/stable/user_guide/
4. Pytest documentation: https://docs.pytest.org/
5. Selenium documentation: https://www.selenium.dev/documentation/
6. pytest-html documentation: https://pytest-html.readthedocs.io/

## Repository Clone Procedure

~~~powershell
# Clone the repository
# Source: standard Git usage

git clone https://github.com/pearsonDaniel/automated_testing_example_selenium.git
cd automated_testing_example_selenium
~~~

## Python Environment Setup

### 1. Verify Python installation

~~~powershell
python --version
~~~

If Python is not available on PATH, install Python from the official installer and ensure the interpreter is accessible in terminal sessions.

### 2. Create a dedicated virtual environment

~~~powershell
python -m venv selenium-venv
~~~

### 3. Activate the virtual environment in PowerShell

~~~powershell
# If script execution is restricted in the current shell session:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

# Activate the environment
.\selenium-venv\Scripts\Activate.ps1
~~~

### 4. Upgrade pip

~~~powershell
python -m pip install --upgrade pip
~~~

## Dependency Installation

The repository imports and uses Selenium, Pytest, pytest-html, Requests, OpenPyXL, Faker, and imageio-ffmpeg in current source.

Source references:

1. conftest imports: conftest.py lines 2-7
2. login page workbook usage: src/pages/login_page.py lines 7-13
3. login test and pytest marker usage: test/login_tests/test_login.py lines 9-14

~~~python
# Source citation: conftest.py imports
from selenium import webdriver
import pytest
import requests
import pytest_html
import imageio_ffmpeg

# Source citation: src/pages/login_page.py imports
import openpyxl
~~~

Install the primary dependency set:

~~~powershell
python -m pip install selenium pytest requests pytest-html openpyxl Faker imageio-ffmpeg
~~~

### ffmpeg runtime for local video capture

Local per-test MP4 recording uses ffmpeg through `imageio-ffmpeg`.

1. In most environments, installing `imageio-ffmpeg` is sufficient because it resolves/provisions an ffmpeg executable for the test run.
2. If your environment blocks that binary provisioning, install ffmpeg manually:

~~~powershell
winget install Gyan.FFmpeg
# or
choco install ffmpeg
~~~

### Verified installed package set in the current selenium-venv

The following packages are currently installed in the verified environment snapshot:

~~~text
attrs==26.1.0
certifi==2026.5.20
cffi==2.0.0
charset-normalizer==3.4.7
colorama==0.4.6
et_xmlfile==2.0.0
Faker==40.19.1
h11==0.16.0
idna==3.16
iniconfig==2.3.0
Jinja2==3.1.6
MarkupSafe==3.0.3
openpyxl==3.1.5
outcome==1.3.0.post0
packaging==26.2
pip==25.0.1
pluggy==1.6.0
pycparser==3.0
Pygments==2.20.0
PySocks==1.7.1
pytest==9.0.3
pytest-html==4.2.0
pytest-metadata==3.1.1
requests==2.34.2
selenium==4.44.0
imageio-ffmpeg==0.6.0
sniffio==1.3.1
sortedcontainers==2.4.0
trio==0.33.0
trio-websocket==0.12.2
typing_extensions==4.15.0
tzdata==2026.2
urllib3==2.7.0
websocket-client==1.9.0
wsproto==1.3.2
~~~

## Runtime Data Requirements

The login flow reads credentials from an Excel workbook.

Source reference:

1. Workbook load and cell extraction: src/pages/login_page.py lines 10-13

Expected file path:

1. test/test_resources/user_credentials.xlsx

If this file is missing or malformed, login-related tests will fail at runtime.

## Browser Configuration Behavior in This Project

The browser fixture is autouse and function-scoped.

Source reference:

1. Fixture declaration and browser option setup: conftest.py lines 20-66

Behavior implemented:

1. Chrome execution uses Incognito mode and disables password manager and autofill preferences.
2. Edge execution uses InPrivate mode and disables password manager and autofill preferences.
3. Firefox path is currently non-operational and explicitly marked unsupported.

~~~python
# Source citation: conftest.py lines 20-33 and 43-55
@pytest.fixture(scope="function", autouse=True)
def config_browser(browser):
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False,
        })
~~~

## Test Execution Commands

### Run login test

~~~powershell
.\selenium-venv\Scripts\python.exe -m pytest test/login_tests/test_login.py --maxfail=1 --disable-warnings -v
~~~

### Run add-to-cart test

Current location of cart tests is under home_page_tests.

~~~powershell
.\selenium-venv\Scripts\python.exe -m pytest test/home_page_tests/test_add_to_cart.py --maxfail=1 --disable-warnings -v
~~~

### Run remove-from-cart test

~~~powershell
.\selenium-venv\Scripts\python.exe -m pytest test/home_page_tests/test_remove_from_cart.py --maxfail=1 --disable-warnings -v
~~~

## Pytest HTML Report Configuration

### Command-level configuration for self-contained reports

Use the following command pattern to generate a standalone HTML artifact with embedded assets:

~~~powershell
.\selenium-venv\Scripts\python.exe -m pytest test/login_tests/test_login.py --html=reports/report.html --self-contained-html --maxfail=1 --disable-warnings -v
~~~

The --self-contained-html option is documented by pytest-html and embeds CSS and script content so the file can be opened independently.

### Project-level report enrichment in conftest hook

The repository adds report extras during test execution via pytest_runtest_makereport.

Source reference:

1. Hook and extras logic: conftest.py lines 69-106

Implemented report enrichments:

1. Base64 screenshot attached to report extras for each call phase.
2. Inline HTML block containing test name.
3. Additional screenshot attachment for failed tests.
4. Optional CI screenshot file creation and pipeline attachment when CI environment variables are set.

~~~python
# Source citation: conftest.py lines 75-82 and 96-106
if report.when == "call":
    driver = item.funcargs['config_browser']
    screenshot = driver.get_screenshot_as_base64()
    extras.append(pytest_html.extras.image(rf"{screenshot}"))
    extras.append(pytest_html.extras.html(rf"<div>TEST NAME: {item.name}</div>"))
    report.extras = extras
~~~

### Expected information in generated report

Based on current plugin configuration and observed execution behavior, the HTML report includes:

1. Test session summary counts.
2. Environment metadata table supplied by pytest and pytest-metadata plugin.
3. Per-test outcome rows and durations.
4. Embedded screenshots from extras attachments.
5. Embedded test name HTML fragment from hook logic.

## Recent Suite Maintenance Updates

1. Added `pytest.ini` and registered the `selenium` marker to remove unknown marker warnings and make marker usage explicit.
2. Refactored page-object-model test modules to rely on fixture injection instead of importing fixtures directly from `conftest.py`.
3. Added a session-scoped `base_url` fixture in `conftest.py` to centralize base URL usage.
4. Updated HTTP 200 verification in `src/pages/base_page.py` to:
    - Use TLS verification by default.
    - Fall back in controlled fashion for certificate-intercepted environments while suppressing noisy TLS warnings.

## Repository Tracking Hygiene for Local Execution

The repository ignores local environments, Python cache files, and generated report artifacts.

Source reference:

1. Ignore rules: .gitignore lines 1-23

~~~gitignore
# Source citation: .gitignore lines 1-17
__pycache__/
*.py[cod]
.venv/
selenium-venv/
mtt-venv/
.pytest_cache/
reports/**/*.html
reports/**/assets/
~~~

This policy allows local report generation and test execution without polluting version control history.

## Validation Checklist

After setup, a ready-to-run state is indicated by all of the following:

1. python --version returns a valid interpreter version.
2. Virtual environment activation modifies shell prompt context.
3. pip installation completes without unresolved package errors.
4. test/test_resources/user_credentials.xlsx is present and readable.
5. A test command completes and reports PASSED.
6. Optional HTML report command generates reports/report.html successfully.

## Troubleshooting Notes

1. If Python is not found, verify PATH and restart terminal session.
2. If pytest is not found, run commands through the environment interpreter path.
3. If browser login prompts interrupt tests, verify fixture browser options in conftest.py lines 22-55 are unchanged.
4. If report files are missing, verify pytest-html is installed and command includes --html and --self-contained-html.

## Maintenance Recommendation

For long-term reproducibility, add an explicit dependency lock file generated from the environment:

~~~powershell
python -m pip freeze > requirements-lock.txt
~~~

This repository currently documents verified versions in this guide; maintaining a generated lock file provides stronger automation and CI reproducibility.