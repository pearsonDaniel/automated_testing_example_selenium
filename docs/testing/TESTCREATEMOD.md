# Create and Modify Tests

This guide explains how to add new tests using the current project pattern.

## Standard Test Pattern

1. Use fixture injection in test function signature
2. Navigate with `base_url`
3. Instantiate page objects with `driver`
4. Reuse locator constants from `locators/`
5. Keep assertions in test or page methods

## Minimal New Test Scaffold

```python
import pytest
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.login_locators import LoginPageLocators


@pytest.mark.selenium
def test_example_flow(config_browser, base_url):
    driver = config_browser
    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    login_page.login()

    home_page = HomePage(driver)
    home_page.verify_inventory_title()
```

## Where to Add Code

- New tests: `test/<feature>_tests/`
- New page methods: `src/pages/<page>_page.py`
- New locators: `locators/<feature>_locators.py`

## Modification Rules

- Keep fixture names unchanged unless framework refactor is intentional
- Prefer adding page methods over duplicating Selenium calls in tests
- Keep locator updates isolated to locator modules
- Keep test names explicit and scenario-oriented

## Checklist Before Committing

1. Test runs with `python -m pytest <target> -v`
2. Imports follow current folder conventions
3. `@pytest.mark.selenium` is present
4. Report still generates artifacts for modified tests
