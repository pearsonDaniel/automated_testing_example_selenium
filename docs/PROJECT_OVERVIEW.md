# Selenium - QA Automation - Project Overview
### By: Dan Pearson - QA Automation Specialist
### Date: 28 May 2026

This repository is for educational purposes in the understanding of basic QA Automation concepts. The codebase contains a Selenium and Pytest-based UI automation framework. The current verified execution path includes login flow validation, inventory page interaction, & shopping cart/checkout interaction on the Sauce Demo application. The framework is implemented with a Page Object Model structure and centralized Pytest fixture configuration.

# Project Purpose

The project objective is to educate prospective QA Automation Engineers in basic deterministic browser automation for regression-style validation of user workflows. Current tests use a shared browser fixture, page classes in `src/pages/`, and locator modules in `locators/` to reduce duplication and standardize interaction logic.

## Project Organization
- `conftest.py`: Pytest configuration, fixtures, and browser setup logic.
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


# Conventions Used

- Page Object Model is used for test behavior encapsulation.
- Browser configuration is fixture-driven and autouse for function scope.
- Browser password manager and autofill prompts are explicitly disabled through browser options to reduce non-deterministic interruption.
- Pytest HTML extras are attached in hook callbacks for observability.
- Repository hygiene controls are maintained in `.gitignore` to avoid committing generated files and local environments.
- Test profile data randomly generated using Faker and injected using Selenium WebDriver

# Dependencies Utilized

- `selenium`: Browser automation driver.
- `pytest`: Test execution and fixture orchestration.
- `pytest-html`: HTML report and extras integration.
- `requests`: HTTP checks used by page verification methods.
- `openpyxl`: Spreadsheet-based credential loading in login page logic.
- `Faker`: Test data utility package.

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






This repository demonstrates a modern, maintainable UI automation framework using Selenium and Pytest. The codebase is structured for clarity and educational value, focusing on best practices in test automation.

