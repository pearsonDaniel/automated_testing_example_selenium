# SauceDemo Coverage Gaps: Student Implementation Guide

## Purpose

This document intentionally keeps selected coverage areas open so students can implement them as structured learning exercises.

Each gap includes two guidance modes:

- Clue Path: high-level implementation direction
- Help Path: direct, step-by-step guidance in low-technical language

## POM Implementation Rules (Required)

Use these rules for every exercise in this guide:

1. Keep UI interaction logic in page-object methods, not in test bodies.
2. Keep tests orchestration-focused: arrange state, call page methods, assert outcomes.
3. Add new locators only when current locator modules do not already provide required selectors.
4. Place new locators in the existing feature locator file unless a new page/component boundary justifies a new locator file.
5. Add new behavior to existing page objects first; create a new page object only when the behavior belongs to a distinct page/component with its own responsibilities.
6. Follow existing codebase conventions: WebDriverWait usage, explicit assertion messages, fixture injection, and selenium marker usage.
7. Prefer small, single-responsibility page methods with names that describe observable behavior.

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

1. Create a new negative-login test that reuses the existing login setup flow.
2. Extend LoginPage with methods that encapsulate negative-login actions and error-state observation.
3. Add or update login locators only if an error banner/message locator is missing.
4. Keep test logic limited to method calls plus high-value assertions.
5. Validate two outcomes: error feedback is observable and inventory transition did not occur.

### Help Path (detailed)

1. Create a new file named test/login_tests/test_login_negative.py.
2. In src/pages/login_page.py, add a method such as submit_login_with_credentials(username, password) that performs field entry and click.
3. In locators/login_locators.py, add locator(s) for login error feedback only if not already present.
4. In src/pages/login_page.py, add methods such as is_login_error_visible() and get_login_error_text().
5. In the test file, define a test function with config_browser and base_url fixtures.
6. Open the application using driver.get(base_url), then call existing response verification.
7. Call the new page-object login method with invalid credential input.
8. Assert using page-object methods, not direct Selenium calls in the test.
9. Assert URL/state remains in login boundary and does not reach inventory.
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

    page.submit_login_with_credentials("locked_out_user", "secret_sauce")

    # TODO: implement these page-object methods in LoginPage
    assert page.is_login_error_visible(), "Expected login error feedback to be visible"
    assert "inventory" not in driver.current_url, "User should not reach inventory after invalid login"
```

## Gap 2: Cart Integrity and Badge State

### What we are lacking

Current tests validate add/remove actions but do not validate quantitative cart badge behavior over sequential state changes.

### What to implement

Implement at least one test that verifies badge count progression across add and remove events.

Suggested student test:

- test_cart_badge_count_updates_with_add_and_remove

### Clue Path (high-level)

1. Reuse existing add/remove page methods and extend HomePage with cart badge state methods.
2. Add badge locator(s) in homepage locators only if required selector is missing.
3. Encapsulate badge parsing and empty-state handling inside HomePage.
4. Keep test assertions focused on sequence-level outcomes rather than raw DOM details.
5. Validate progression across both increment and decrement transitions.

### Help Path (detailed)

1. Create a new file named test/shopping_cart_tests/test_cart_badge_count.py.
2. In locators/homepage_locators.py, add cart badge locator if missing.
3. In src/pages/home_page.py, add methods such as get_cart_badge_count() and is_cart_badge_visible().
4. Implement badge parsing in HomePage so tests do not convert strings or handle missing elements directly.
5. Reuse fixture injection (config_browser, base_url) and login through existing LoginPage method.
6. Add/remove items using existing HomePage methods.
7. Assert badge values by calling HomePage methods only.
8. Confirm empty-cart behavior through page-object method output.
9. Keep assertion messages explicit so failure reports identify transition stage.

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

    # TODO: implement in HomePage: get_cart_badge_count()
    assert home.get_cart_badge_count() == 0

    home.add_item(HomePageLocators.ADD_BACKPACK_BUTTON, HomePageLocators.REMOVE_BACKPACK_BUTTON)
    assert home.get_cart_badge_count() == 1

    home.add_item(HomePageLocators.ADD_BIKE_LIGHT_BUTTON, HomePageLocators.REMOVE_BIKE_LIGHT_BUTTON)
    assert home.get_cart_badge_count() == 2

    home.remove_item(HomePageLocators.REMOVE_BIKE_LIGHT_BUTTON, HomePageLocators.ADD_BIKE_LIGHT_BUTTON)
    assert home.get_cart_badge_count() == 1

    home.remove_item(HomePageLocators.REMOVE_BACKPACK_BUTTON, HomePageLocators.ADD_BACKPACK_BUTTON)
    assert home.get_cart_badge_count() == 0
```

## Gap 3: Checkout Validation and Alternate Paths

### What we are lacking

Checkout coverage is currently limited to successful completion and does not verify required-field validation behavior.

### What to implement

Implement at least one checkout validation test for missing required fields.

Suggested student test:

- test_checkout_requires_first_name

### Clue Path (high-level)

1. Reuse current happy-path setup and extend CheckoutPage for validation-path actions.
2. Encapsulate partial form submission and error retrieval in CheckoutPage methods.
3. Add checkout validation locators only if missing in checkout locator file.
4. Keep test body focused on scenario orchestration and outcome assertions.
5. Validate both feedback visibility and workflow boundary behavior.

### Help Path (detailed)

1. Create a new file named test/shopping_cart_tests/test_checkout_validation.py.
2. In locators/checkout_locators.py, add error-banner or error-text locators if absent.
3. In src/pages/checkout_page.py, add methods such as submit_checkout_missing_first_name(...) and get_checkout_error_text().
4. Reuse existing setup: login, add one item, open cart, click checkout.
5. Call new CheckoutPage method that omits one required field.
6. Assert error visibility/text through CheckoutPage methods, not direct selector use in tests.
7. Assert the page remains on checkout information stage.
8. Extend with sibling methods/tests for missing last name and missing postal code.

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
    page.submit_checkout_missing_first_name(last_name="Student", postal_code="12345")

    # TODO: implement these page-object methods in CheckoutPage
    assert page.is_checkout_error_visible(), "Expected checkout validation feedback"
    assert "First Name" in page.get_checkout_error_text()
    assert page.is_on_checkout_information_step(), "Expected to remain on information step"
```

## Gap 4: Cross-Browser Behavioral Parity

### What we are lacking

The framework supports browser selection, but explicit parity checks between Chrome and Edge are not yet codified.

### What to implement

Implement at least one parity smoke test and execute it under both active browser modes.

Suggested student test:

- test_parity_login_inventory_title

### Clue Path (high-level)

1. Select a stable behavior path and represent readiness checks as page-object methods.
2. Keep parity assertions browser-agnostic and behavior-oriented.
3. Avoid direct selector logic in test bodies; place reusable checks in page objects.
4. Execute identical test flow in Chrome and Edge.
5. Compare outcomes and artifact consistency.

### Help Path (detailed)

1. Create a new file named test/home_page_tests/test_browser_parity.py.
2. Reuse fixture injection so browser choice is provided by --browser.
3. In existing page objects, add any missing readiness method needed for parity validation.
4. Implement one concise scenario: login then verify inventory-ready state.
5. Keep assertions delegated to page-object methods where feasible.
6. Run once with --browser Chrome and once with --browser Edge.
7. Review report artifacts for each run and compare outcome equivalence.
8. If behavior diverges, record reproducible observations before modifying implementation logic.

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

    home_page = HomePage(driver)
    home_page.verify_inventory_title()
    # TODO: optionally add a page-object method like home_page.is_inventory_ready()
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
