# Executive Summary

This codebase implements an automated testing framework for the MIPR Tracking Tool (MTT) web application, utilizing Selenium WebDriver and Pytest. The framework is designed to facilitate robust, repeatable browser-based testing, including login, navigation, and UI validation, with extensible support for multiple browsers and detailed HTML reporting.

# Project Purpose

The primary objective of this project is to provide automated end-to-end testing for the MIPR Tracking Tool, ensuring application reliability and rapid feedback during development and deployment cycles. The framework supports cross-browser testing (Chrome, Edge) and integrates with CI environments for continuous quality assurance.

# Project Structure

- **conftest.py**: Central Pytest configuration, browser fixtures, and test hooks.
- **script.py**: Interactive CLI for running test suites and opening reports.
- **locators/**: Page element locators for maintainable selectors.
- **src/pages/**: Page Object Model (POM) classes encapsulating UI logic.
- **test/**: Test cases organized by feature and browser.
- **reports/**: Generated HTML reports and assets.
- **selenium-venv/**: Isolated Python environment for dependencies.

# Conventions Used

- **Page Object Model (POM)**: Each page is represented by a class (e.g., `LoginPage`, `HomePage`) encapsulating element interactions and verifications.
- **Pytest Fixtures**: Used for browser setup/teardown and configuration.
- **Locator Classes**: All selectors are centralized in `locators/` for maintainability.
- **HTML Reporting**: Test runs generate detailed HTML reports with embedded screenshots.
- **CI Integration**: Hooks for Azure DevOps and other CI systems (see `conftest.py`, lines 61–120).

# Dependencies Utilized

- **selenium**: Browser automation
- **pytest**: Test runner
- **pytest-html**: HTML reporting
- **requests**: HTTP status checks
- **openpyxl**: Excel credential management
- **Faker**: Test data generation

# Current Limitations

- Firefox browser support is not implemented.
- Some file paths in `script.py` are hardcoded and may require adjustment for different environments.
- Test data is read from Excel files, which may limit scalability.
- Some legacy/archived tests remain in the codebase.

# Next Steps Forwards

- Implement Firefox and additional browser support.
- Refactor hardcoded paths for portability.
- Expand test coverage and modularize test data management.
- Remove or refactor archived tests.
- Enhance CI/CD integration and reporting.

# References

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Pytest-HTML Documentation](https://pytest-html.readthedocs.io/en/latest/)

---

## Example: Login Test (test/login_tests/test_login.py)
```python
# test/login_tests/test_login.py (lines 1-18)
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from locators.login_locators import LoginPageLocators
import pytest

@pytest.mark.selenium
def test_login(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    login_page.login()
    login_page.verify_title()
    print("###########################################################")
```

## Example: Browser Fixture (conftest.py)
```python
# conftest.py (lines 10-38)
@pytest.fixture(scope="function", autouse=True)
def config_browser(browser):
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()
    elif browser == "Edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)
        yield driver
        driver.quit()
    elif browser == "Firefox":
        print("Firefox - Nope")
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")
```
