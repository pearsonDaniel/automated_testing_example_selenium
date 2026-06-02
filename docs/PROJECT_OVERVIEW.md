# Selenium - QA Automation - Project Overview
### By: Dan Pearson - QA Automation Specialist
### Date: 28 May 2026

This repository is for educational purposes in the understanding of basic QA Automation concepts. The codebase contains a Selenium and Pytest-based UI automation framework. The current verified execution path includes login flow validation, inventory page interaction, & shopping cart/checkout interaction on the Sauce Demo application. The framework is implemented with a Page Object Model structure and centralized Pytest fixture configuration.

# Project Purpose

The project objective is to educate prospective QA Automation Engineers in basic deterministic browser automation for regression-style validation of user workflows. Current tests use a shared browser fixture, page classes in `src/pages/`, and locator modules in `locators/` to reduce duplication and standardize interaction logic.

## Project Organization
- `conftest.py`: Pytest configuration, fixtures, and browser setup logic.
- `pytest.ini`: Pytest marker registration and shared Pytest configuration.
- `src/pages/`: Page object classes, with a shared base class for common actions.
- `locators/`: All element selectors, organized by feature or page.
- `test/`: Test suites, organized by feature (e.g., login, shopping cart).
- `reports/`: HTML reports and assets (ignored by git).
- `.env.example`: Template for required environment variables (credentials, etc.).
- `.gitignore`: Excludes local environments, reports, and sensitive files from version control.
- `script.py`: Utility or runner script for automation tasks.


## Test Structure
- **Test logic is contained within methods**: Each test method performs a specific scenario, calling reusable page object methods for actions and assertions.
- **Tests call page object methods**: Test files import page classes and invoke their methods to interact with the UI, ensuring DRY and readable test code.
- **Fixtures and resources**: Pytest fixtures in `conftest.py` manage browser setup, teardown, and configuration. Test resources (such as test data or environment variables) are loaded as needed.
- **HTML reporting**: Test runs generate HTML reports using `pytest-html`, including screenshots and metadata for debugging and traceability.


## Page Objects and Locators
- **Page Object Model**: All UI logic is encapsulated in page classes under `src/pages/`. Each page class represents a screen or component and exposes methods for user actions and verifications.
- **Base Page**: All page objects inherit from a common `BasePage` superclass, which provides universal methods (e.g., navigation, element interaction, waits, assertions).
- **Locators**: All element locators are separated into dedicated modules under `locators/`, grouped by feature or page. This separation ensures maintainability and easy updates when UI changes.


## Conventions Used

- Page Object Model is used for test behavior encapsulation.
- Browser configuration is fixture-driven and autouse for function scope.
- Browser password manager and autofill prompts are explicitly disabled through browser options to reduce non-deterministic interruption.
- Pytest HTML extras are attached in hook callbacks for observability.
- `@pytest.mark.selenium` is registered in `pytest.ini` to keep marker usage explicit and warning-free.
- Non-procedural tests use fixture injection (`config_browser`, `base_url`) without importing fixtures from `conftest.py`.
- Local ffmpeg-driven video recording is started and stopped per test from fixture and hook lifecycle points.
- Repository hygiene controls are maintained in `.gitignore` to avoid committing generated files and local environments.
- Test profile data randomly generated using Faker and injected using Selenium WebDriver

## Current Instructional Split

- `test/procedural_demo/test_google_search.py` remains intentionally procedural as a baseline teaching example.
- Page-object-model suites under `test/home_page_tests/`, `test/login_tests/`, and `test/shopping_cart_tests/` reflect the refactored best-practice fixture usage.
- `src/pages/base_page.py` HTTP status verification now performs TLS verification first, with controlled fallback handling for intercepted or self-signed certificate chains in constrained environments.

## Dependencies Utilized

- `selenium`: Browser automation driver.
- `pytest`: Test execution and fixture orchestration.
- `pytest-html`: HTML report and extras integration.
- `requests`: HTTP checks used by page verification methods.
- `openpyxl`: Spreadsheet-based credential loading in login page logic.
- `Faker`: Test data utility package.
- `imageio-ffmpeg`: Bundled ffmpeg binary resolver used by local recording.
- `ffmpeg`: Video capture/encoding runtime used for per-test MP4 artifact creation.


## Reporting Enhancements

The pytest-html report includes rich, per-test artifacts, including screenshots and videos.

- Embedded screenshot preview (self-contained in report).
- Links column artifacts for each test:
  - Screenshot file
  - Page source (styled viewer)
  - Page source (raw HTML)
  - Browser console log (JSON)
  - Performance log (JSON)
  - Test metadata (JSON)
  - Test video (local MP4)
- Optional video artifact URL support via environment configuration.
- Styled page-source viewer with metadata header and code panel for easier inspection.
- Inline HTML5 video block is attached via pytest-html extras for in-report playback.

### Local Video Controls

- `TEST_CAPTURE_LOCAL_VIDEO`: enables/disables local per-test recording (default enabled).
- `TEST_VIDEO_FPS`: controls recording smoothness (default `20`). Higher values improve smoothness with higher CPU/storage cost.

Artifacts are written under `reports/artifacts/<timestamp>/<test_nodeid>/` and linked relative to `reports/report.html` so they open reliably.


# References

- Selenium: https://www.selenium.dev/documentation/
- Pytest: https://docs.pytest.org/en/stable/
- Pytest HTML: https://pytest-html.readthedocs.io/en/latest/

## Code Examples With Source Citations

```python
# conftest.py:20-33
# conftest.py (enhanced report artifacts)
extras.append(
    pytest_html.extras.image(
        artifacts["screenshot_b64"],
        mime_type="image/png",
        extension="png",
    )
)
extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["screenshot_file"], item), name="Screenshot File"))
extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["page_source_viewer_file"], item), name="Page Source (Styled)"))
extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["page_source_file"], item), name="Page Source (Raw)"))
extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["browser_log_file"], item), name="Browser Console Log"))
extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["performance_log_file"], item), name="Performance Log"))
extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["metadata_file"], item), name="Test Metadata"))
```

```python
# test/shopping_cart_tests/test_add_to_cart.py:13-29
# test/shopping_cart_tests/test_checkout_shopping_cart.py (Faker-driven checkout)
fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.postcode()

checkout_page.add_checkout_info(first_name, last_name, postal_code)
checkout_page.click_continue()
checkout_page.verify_payment_info("SauceCard #31337")
```

### .gitignore:1-17
### .gitignore (report and artifact output)
```
*.py[cod]
.venv/
selenium-venv/
mtt-venv/
.pytest_cache/
reports/**/*.html
reports/**/assets/
reports/artifacts/
```

