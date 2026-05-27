# Executive Summary

This repository contains a Selenium and Pytest-based UI automation framework. The current verified execution path includes login flow validation and shopping cart item addition on the Sauce Demo application. The framework is implemented with a Page Object Model structure and centralized Pytest fixture configuration.

# Project Purpose

The project objective is deterministic browser automation for regression-style validation of user workflows. Current tests use a shared browser fixture, page classes in `src/pages/`, and locator modules in `locators/` to reduce duplication and standardize interaction logic.

# Project Structure

- `conftest.py`: Pytest CLI options, autouse browser fixture, screenshot report hook, and base URL configuration.
- `src/pages/`: Page classes for reusable UI operations.
- `locators/`: Selector constants for page elements.
- `test/login_tests/`: Login-focused tests.
- `test/shopping_cart_tests/`: Cart workflow tests.
- `docs/`: Project and Git process documentation.
- `reports/`: Runtime-generated HTML reports and related assets (currently ignored by Git).

# Conventions Used

- Page Object Model is used for test behavior encapsulation.
- Browser configuration is fixture-driven and autouse for function scope.
- Browser password manager and autofill prompts are explicitly disabled through browser options to reduce non-deterministic interruption.
- Pytest HTML extras are attached in hook callbacks for observability.
- Repository hygiene controls are maintained in `.gitignore` to avoid committing generated files and local environments.

# Dependencies Utilized

- `selenium`: Browser automation driver.
- `pytest`: Test execution and fixture orchestration.
- `pytest-html`: HTML report and extras integration.
- `requests`: HTTP checks used by page verification methods.
- `openpyxl`: Spreadsheet-based credential loading in login page logic.
- `Faker`: Test data utility package.

# Current Fixes Verified

- Browser prompt mitigation: incognito/inprivate execution and password manager/autofill disable flags are configured in the fixture.
- Test organization: shopping cart coverage exists under `test/shopping_cart_tests/`.
- Tracking hygiene: bytecode caches, local virtual environments, and generated report artifacts are ignored by default and no longer tracked in Git.

# Current Limitations

- Firefox remains unimplemented in fixture logic.
- The shopping cart test file header comment currently identifies the file as `test_login.py` while the file path is `test/shopping_cart_tests/test_add_to_cart.py`.
- Report artifacts are intentionally excluded from version control, so historical HTML output is not preserved in the repository.

# Next Steps

- Implement Firefox support in the fixture branch currently marked as unsupported.
- Normalize naming consistency in test module headers.
- Add optional CI artifact publishing for generated HTML reports outside Git tracking.

# References

- Selenium: https://www.selenium.dev/documentation/
- Pytest: https://docs.pytest.org/en/stable/
- Pytest HTML: https://pytest-html.readthedocs.io/en/latest/

## Code Examples With Source Citations

```python
# conftest.py:20-33
@pytest.fixture(scope="function", autouse=True)
def config_browser(browser):
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
                "autofill.profile_enabled": False,
                "autofill.credit_card_enabled": False,
            },
        )
```

```python
# test/shopping_cart_tests/test_add_to_cart.py:13-29
@pytest.mark.selenium
def test_add_to_cart(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    login_page.login()
    home_page = HomePage(driver)
    home_page.add_item(HomePageLocators.ADD_BACKPACK_BUTTON, HomePageLocators.REMOVE_BACKPACK_BUTTON)
    home_page.add_item(HomePageLocators.ADD_BIKE_LIGHT_BUTTON, HomePageLocators.REMOVE_BIKE_LIGHT_BUTTON)
```

```gitignore
# .gitignore:1-17
__pycache__/
*.py[cod]
.venv/
selenium-venv/
mtt-venv/
.pytest_cache/
reports/**/*.html
reports/**/assets/
```
