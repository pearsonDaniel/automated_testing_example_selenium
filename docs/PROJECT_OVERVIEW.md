# Project Overview

This repository teaches foundational Selenium + Pytest automation design using a layered architecture and reproducible reporting.

## Intended Audience

- Prospective QA automation engineers
- Early-career SDET learners
- Teams introducing fixture-driven test architecture

## Architecture Summary

### Layering

1. Tests in `test/`
2. Page objects in `src/pages/`
3. Locators in `locators/`
4. Framework runtime in `conftest.py`

### Execution flow

1. Pytest starts and registers `--browser` through `pytest_addoption`.
2. `config_browser` fixture creates and configures WebDriver (Chrome or Edge).
3. Test functions receive `config_browser` and `base_url` fixtures.
4. Tests call page-object methods, which reference locator constants.
5. `pytest_runtest_makereport` collects artifacts and enriches pytest-html output.
6. Fixture teardown stops recording and quits browser.

### Browser and driver strategy

- `Chrome`: supported and actively used
- `Edge`: supported and actively used
- `Firefox`: branch exists but currently returns `None` in fixture; not an active run target

### Reporting outputs

For each executed test call, the framework captures:

- Screenshot (file + embedded base64 preview)
- Raw page source
- Styled page-source viewer HTML
- Browser console log JSON
- Performance log JSON
- Metadata JSON
- Local MP4 test video when enabled
- Optional remote video URL when configured

Artifacts are organized under:

`reports/artifacts/<run_timestamp>/<sanitized_test_nodeid>/`

## Test Suite Scope (Current)

- Login tests in `test/login_tests/`
- Home/inventory tests in `test/home_page_tests/`
- Shopping cart/checkout tests in `test/shopping_cart_tests/`
- One intentionally procedural demo in `test/procedural_demo/test_google_search.py`

## Data and configuration model

- Base URL source: `Config.BASE_URL` in `conftest.py`
- Credential model A: spreadsheet in `test/test_resources/user_credentials.xlsx`
- Credential model B: environment variables `LOGIN_USERNAME` and `LOGIN_PASSWORD`
- Optional runtime control via environment variables in `conftest.py`:
  - `TEST_CAPTURE_LOCAL_VIDEO`
  - `TEST_VIDEO_FPS`
  - `TEST_VIDEO_URL`
  - `TEST_VIDEO_URL_TEMPLATE`
  - `CI`
  - `TF_BUILD`

## Where to go next

- Setup instructions: `docs/setup/PROJECTSETUPLOCAL.md`
- Project structure details: `docs/setup/PROJECTSTRUCTURE.md`
- Test execution commands: `docs/testing/TESTRUNNING.md`
- Reporting behavior: `docs/testing/TESTRESULTS.md`
- Troubleshooting guide: `docs/testing/TESTDEBUGERRORS.md`
- How to create/modify tests: `docs/testing/TESTCREATEMOD.md`
- Intentional learning gaps: `docs/testing/TESTCOVERAGEGAPS.md`

