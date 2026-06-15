# Selenium + Pytest Educational Automation Framework

This repository is an educational UI test automation project for prospective QA automation engineers. It demonstrates a Page Object Model architecture on https://www.saucedemo.com using Selenium WebDriver, Pytest fixtures, and pytest-html reporting.

## 15-Minute New Engineer Walkthrough

If you are brand-new to this repository, run these steps in order:

1. Clone and enter project.
2. Create and activate `.venv`.
3. Install dependencies.
4. Run one smoke test.
5. Run full suite with report.

Windows PowerShell quick commands:

```powershell
git clone https://github.com/pearsonDaniel/automated_testing_example_selenium.git
cd automated_testing_example_selenium
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install selenium pytest pytest-html requests openpyxl Faker imageio-ffmpeg
python -m pytest test/login_tests/test_login.py -v
python -m pytest test --browser Chrome --html=reports/report.html --self-contained-html
```

What success looks like:

- Pytest discovers tests under `test/`
- Browser launches and closes cleanly per test
- `reports/report.html` is created
- Artifact folders appear under `reports/artifacts/`

## Documentation Map

Use these docs in order:

1. `docs/DOCUMENTATION-INDEX.md`
2. `docs/PROJECT_OVERVIEW.md`
3. `docs/setup/PROJECTSETUPLOCAL.md`
4. `docs/testing/TESTRUNNING.md`
5. `docs/testing/TESTRESULTS.md`
6. `docs/testing/TESTDEBUGERRORS.md`
7. `docs/testing/TESTCREATEMOD.md`
8. `docs/testing/TESTCOVERAGEGAPS.md`

## Current Architecture (Code-Verified)

- Test framework: Pytest (`pytest.ini` marker registration for `selenium`)
- Browser lifecycle: `conftest.py` fixture `config_browser` (function scope, autouse)
- Browser selector: CLI option `--browser` via `pytest_addoption`
- Supported browser modes in code: `Chrome`, `Edge` (Firefox branch currently returns `None`)
- Page object layer: `src/pages/`
- Locator layer: `locators/`
- Test layer: `test/`
- Reporting: `pytest_html` extras in `pytest_runtest_makereport`
- Artifacts: `reports/artifacts/<timestamp>/<test_nodeid>/`

## Quick Start

### 1) Clone

```powershell
git clone https://github.com/pearsonDaniel/automated_testing_example_selenium.git
cd automated_testing_example_selenium
```

### 2) Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies used by code

```powershell
python -m pip install --upgrade pip
python -m pip install selenium pytest pytest-html requests openpyxl Faker imageio-ffmpeg
```

### 4) Optional environment file for login-env test

```powershell
Copy-Item .env.example .env
```

Required by `test/login_tests/test_login_env.py`:

- `LOGIN_USERNAME`
- `LOGIN_PASSWORD`

### 5) Run suite + HTML report

```powershell
python -m pytest test --browser Chrome --html=reports/report.html --self-contained-html
```

## Frequently Used Commands

Run entire suite:

```powershell
python -m pytest test
```

Run one folder:

```powershell
python -m pytest test/login_tests -v
```

Run one file:

```powershell
python -m pytest test/shopping_cart_tests/test_checkout_shopping_cart.py -v
```

Run with Edge:

```powershell
python -m pytest test --browser Edge -v
```

Generate report:

```powershell
python -m pytest test --browser Chrome --html=reports/report.html --self-contained-html
```

## Environment Variables Used in Code

From `conftest.py`:

- `TEST_CAPTURE_LOCAL_VIDEO` (default `true`)
- `TEST_VIDEO_FPS` (default `20`)
- `TEST_VIDEO_URL`
- `TEST_VIDEO_URL_TEMPLATE`
- `CI`
- `TF_BUILD`

From `test/login_tests/test_login_env.py` path through `src/pages/login_page.py`:

- `LOGIN_USERNAME`
- `LOGIN_PASSWORD`

## Notes for Students

- The procedural demo in `test/procedural_demo/test_google_search.py` intentionally remains procedural for comparison with Page Object Model tests.
- `script.py` exists but contains legacy hardcoded paths and outdated flows; use documented Pytest commands instead.

