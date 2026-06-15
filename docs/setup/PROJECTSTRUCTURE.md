# Project Structure

This document describes the current repository layout and how components interact.

## Top-Level Files

- `conftest.py`: fixture lifecycle, browser setup, artifact collection, report hook
- `pytest.ini`: marker registration (`selenium`)
- `README.md`: onboarding entry point
- `.env.example`: environment variable template for env-based login
- `script.py`: legacy interactive runner with historical paths

## Source Layers

### Tests: `test/`

- `login_tests/`
- `home_page_tests/`
- `shopping_cart_tests/`
- `procedural_demo/`

### Page Objects: `src/pages/`

- `base_page.py`
- `login_page.py`
- `home_page.py`
- `cart_page.py`
- `checkout_page.py`

### Locators: `locators/`

- `login_locators.py`
- `homepage_locators.py`
- `cart_locators.py`
- `checkout_locators.py`
- `locators.py` (shared/base locators)

## Runtime Execution Chain

1. Pytest collects tests in `test/`
2. `pytest_addoption` registers `--browser`
3. `config_browser` fixture creates WebDriver and optional recorder
4. Test calls page methods
5. Page methods use locators
6. `pytest_runtest_makereport` stores and links artifacts

## Reporting and Artifacts

Report file target is usually set via:

```bash
--html=reports/report.html --self-contained-html
```

Artifacts are stored in timestamped test folders:

`reports/artifacts/<timestamp>/<test_nodeid>/`

Collected artifact types:

- screenshot.png
- page_source.html
- page_source_viewer.html
- browser_console.json
- performance_log.json
- test_metadata.json
- test_video.mp4 (when enabled)

## Educational Pattern in this Repository

- Page Object Model tests are the primary pattern.
- One procedural test remains intentionally (`test/procedural_demo/test_google_search.py`) for learning contrast.
- Coverage is intentionally incomplete in some areas; see `../testing/TESTCOVERAGEGAPS.md`.
