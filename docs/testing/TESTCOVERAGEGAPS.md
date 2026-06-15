# SauceDemo Coverage Gaps: Student Implementation Guide

## Purpose

This document intentionally keeps selected coverage areas open so students can implement them as structured learning exercises.

Each gap includes two guidance modes:

- Clue Path: high-level implementation direction
- Help Path: direct, step-by-step guidance in low-technical language

## Current Coverage Snapshot

| Area | Covered | Existing Files |
|---|---|---|
| Login success | Yes | test/login_tests/test_login.py, test/login_tests/test_login_env.py |
| Inventory page title | Yes | test/home_page_tests/test_verify_inventory_title.py |
| Add/remove cart items | Yes | test/home_page_tests/test_add_to_cart.py, test/home_page_tests/test_remove_from_cart.py |
| Open cart view | Yes | test/shopping_cart_tests/test_open_shopping_cart.py |
| Checkout happy path | Yes | test/shopping_cart_tests/test_checkout_shopping_cart.py |

## Gap 1: Authentication Negative Paths

### What we are lacking

Current coverage confirms successful authentication only. It does not verify the system response when credentials are invalid.

### What to implement

Implement at least one negative authentication test.

Suggested student test:

- test_login_invalid_credentials_shows_error

### Clue Path (high-level)

1. Create a new test in the login test folder.
2. Reuse the same setup pattern as positive login tests.
3. Submit a controlled invalid credential combination.
4. Observe the error state after submission.
5. Validate two outcomes: error feedback is visible and navigation to inventory did not occur.

### Help Path (detailed)

1. Create a new file named test/login_tests/test_login_negative.py.
2. Import pytest, LoginPage, and LoginPageLocators.
3. Define a test function with config_browser and base_url fixtures.
4. Open the application using driver.get(base_url).
5. Run the existing HTTP response check through LoginPage.
6. Add a new page-object action that accepts manual username/password inputs and submits login.
7. Pass at least one invalid input combination.
8. Add an assertion that confirms an error signal is visible on the login experience.
9. Add an assertion that confirms the browser did not transition to inventory.html.
10. Execute this file alone first, then include it in full-suite runs.

Starter code block:

```python
import pytest
from src.pages.login_page import LoginPage
from locators.login_locators import LoginPageLocators


@pytest.mark.selenium
def test_login_invalid_credentials_shows_error(config_browser, base_url):
    driver = config_browser
    driver.get(base_url)

    page = LoginPage(driver)
    page.verify_page_http_200_response(LoginPageLocators.URL)

    # TODO: submit invalid credentials with a new LoginPage helper method
    # TODO: assert error message/indicator is visible
    # TODO: assert user did not navigate to inventory page
    assert "saucedemo.com" in driver.current_url
```

## Gap 2: Cart Integrity and Badge State

### What we are lacking

Current tests validate add/remove actions but do not validate quantitative cart badge behavior over sequential state changes.

### What to implement

Implement at least one test that verifies badge count progression across add and remove events.

Suggested student test:

- test_cart_badge_count_updates_with_add_and_remove

### Clue Path (high-level)

1. Start from a valid logged-in state.
2. Add two items and read cart badge state.
3. Remove items one by one and read badge state after each change.
4. Compare observed progression against expected sequence.
5. Handle empty-cart condition as a meaningful state (badge absent or zero-equivalent).

### Help Path (detailed)

1. Create a new file named test/shopping_cart_tests/test_cart_badge_count.py.
2. Reuse fixture injection (config_browser, base_url).
3. Log in through LoginPage.login and instantiate HomePage.
4. Add one HomePage helper that reads the badge text and returns an integer.
5. If badge is absent, return zero instead of failing immediately.
6. Add first product and assert badge becomes 1.
7. Add second product and assert badge becomes 2.
8. Remove one product and assert badge becomes 1.
9. Remove final product and assert badge returns to zero-equivalent state.
10. Keep assertion messages explicit so failure reports identify which transition failed.

Starter code block:

```python
import pytest
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.homepage_locators import HomePageLocators


@pytest.mark.selenium
def test_cart_badge_count_updates_with_add_and_remove(config_browser, base_url):
    driver = config_browser
    driver.get(base_url)

    LoginPage(driver).login()
    home = HomePage(driver)
    home.add_item(HomePageLocators.ADD_BACKPACK_BUTTON, HomePageLocators.REMOVE_BACKPACK_BUTTON)
    home.add_item(HomePageLocators.ADD_BIKE_LIGHT_BUTTON, HomePageLocators.REMOVE_BIKE_LIGHT_BUTTON)

    # TODO: assert badge count is 2
    home.remove_item(HomePageLocators.REMOVE_BIKE_LIGHT_BUTTON, HomePageLocators.ADD_BIKE_LIGHT_BUTTON)
    # TODO: assert badge count is 1
    home.remove_item(HomePageLocators.REMOVE_BACKPACK_BUTTON, HomePageLocators.ADD_BACKPACK_BUTTON)
    # TODO: assert badge is absent or zero-equivalent
    assert True
```

## Gap 3: Checkout Validation and Alternate Paths

### What we are lacking

Checkout coverage is currently limited to successful completion and does not verify required-field validation behavior.

### What to implement

Implement at least one checkout validation test for missing required fields.

Suggested student test:

- test_checkout_requires_first_name

### Clue Path (high-level)

1. Reuse existing happy-path steps until checkout information page appears.
2. Leave one required input empty and continue.
3. Capture the resulting validation response.
4. Validate that workflow does not advance to overview.

### Help Path (detailed)

1. Create a new file named test/shopping_cart_tests/test_checkout_validation.py.
2. Import LoginPage, HomePage, CartPage, CheckoutPage, and needed locators.
3. Reuse existing setup: login, add one item, open cart, click checkout.
4. Add a CheckoutPage helper that submits partial data with one required field omitted.
5. Add a locator for validation feedback text if one does not already exist.
6. After clicking Continue, assert validation text is visible.
7. Assert current checkout stage remains on information step (no overview transition).
8. Extend with additional tests for missing last name and missing postal code.

Starter code block:

```python
import pytest
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from locators.login_locators import LoginPageLocators
from locators.homepage_locators import HomePageLocators


@pytest.mark.selenium
def test_checkout_requires_first_name(config_browser, base_url):
    driver = config_browser
    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    login_page.login()

    home = HomePage(driver)
    home.add_item(HomePageLocators.ADD_BACKPACK_BUTTON, HomePageLocators.REMOVE_BACKPACK_BUTTON)
    home.click_shopping_cart()
    CartPage(driver).click_checkout()

    page = CheckoutPage(driver)
    # TODO: submit with first name omitted
    # TODO: assert validation message is visible and informative
    # TODO: assert no transition to checkout overview
    assert True
```

## Gap 4: Cross-Browser Behavioral Parity

### What we are lacking

The framework supports browser selection, but explicit parity checks between Chrome and Edge are not yet codified.

### What to implement

Implement at least one parity smoke test and execute it under both active browser modes.

Suggested student test:

- test_parity_login_inventory_title

### Clue Path (high-level)

1. Select a stable behavior path already verified in existing tests.
2. Keep assertions browser-agnostic and behavior-based.
3. Execute same test with Chrome and Edge.
4. Compare outcomes and artifact quality for consistency.

### Help Path (detailed)

1. Create a new file named test/home_page_tests/test_browser_parity.py.
2. Reuse fixture injection so browser choice is provided by --browser.
3. Implement one concise scenario: login then verify inventory title.
4. Add one assertion for title/state that should be identical across browsers.
5. Run once with --browser Chrome and once with --browser Edge.
6. Review report artifacts for each run to ensure both executions produce equivalent evidence quality.
7. If behavior diverges, record a reproducible observation before applying code changes.

Starter code block:

```python
import pytest
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.login_locators import LoginPageLocators


@pytest.mark.selenium
def test_parity_login_inventory_title(config_browser, base_url):
    driver = config_browser
    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    login_page.login()
    HomePage(driver).verify_inventory_title()
```

## Suggested Student Progression

1. Gap 1: Authentication negative paths
2. Gap 3: Checkout validation
3. Gap 2: Cart badge integrity
4. Gap 4: Cross-browser parity

## Instructor Note

Coverage gaps in this document are intentionally retained as instructional opportunities.

They are not classified as defects in the educational design. They are controlled exercises for practicing:

- requirement-to-assertion translation
- safe page-object extension
- centralized locator discipline
- reproducible cross-browser reasoning

## Related Documents

- TESTCREATEMOD.md
- TESTRUNNING.md
- TESTRESULTS.md
- TESTDEBUGERRORS.md
- ../setup/PROJECTSTRUCTURE.md
