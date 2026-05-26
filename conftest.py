# conftest.py
from selenium import webdriver
import os
import platform
import pytest
import requests
import pytest_html

def pytest_addoption(parser):
     parser.addoption(
         "--browser",
         action="store",
         default="Chrome",
         help="Specify the browser: Chrome or Edge"
      )
@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
     
@pytest.fixture(scope="function", autouse=True)     
def config_browser(browser):
        if  browser == "Chrome":
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless")
            print("Session User: " + str(os.getlogin()))
            print("OS Name: " + str(platform.system()))
            print("OS Version: " + str(platform.version()))
            print("Browser: " + browser)
            driver = webdriver.Chrome(options=options)
            yield driver
            driver.quit()
        elif browser == "Edge":
            options = webdriver.EdgeOptions()
            print("Session User: " + str(os.getlogin()))
            print("OS Name: " + str(platform.system()))
            print("OS Version: " + str(platform.version()))
            print("Browser: " + browser)
            driver = webdriver.Edge(options=options)
            yield driver
            driver.quit()
        elif browser == "Firefox":
            print("Firefox - Nope")
        else:
            raise ValueError(f"Browser '{browser}' is not supported.")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Retrieve Test Run IDs from the environment variable
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # Always add these items to report
        driver = item.funcargs['config_browser']
        # Take a Screenshot in base 64 and embed directly into report
        screenshot = driver.get_screenshot_as_base64()
        extras.append(pytest_html.extras.image(rf"{screenshot}"))
        extras.append(pytest_html.extras.html(rf"<div>TEST NAME: {item.name}</div>"))
        report.extras = extras
        #If CI
        if os.environ.get('CI') == 'true' or os.environ.get('TF_BUILD') == 'True':
                # Create a directory to store screenshots, if it doesn't exist.
                screenshots_dir = os.path.join(os.getcwd(), "screenshots")
                os.makedirs(screenshots_dir, exist_ok=True)
                # Save a screenshot to file.
                screenshot_file = os.path.join(screenshots_dir, f"{item.name}.png")
                driver.save_screenshot(screenshot_file)
                 # Use item._request to get the add_pipelines_attachment fixture
                add_attachment = item._request.getfixturevalue("add_pipelines_attachment")
                # Attach the screenshot file to the Azure DevOps test result.
                add_attachment(screenshot_file, f"Screenshot for test {item.name}")
        # In case of Report Failure
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs['config_browser']
            # Take a screenshot
            screenshot = driver.get_screenshot_as_base64()
            extras.append(pytest_html.extras.image(rf"{screenshot}"))
            report.extras = extras
            if os.environ.get('CI') == 'true' or os.environ.get('TF_BUILD') == 'True':
                failure_screenshot_file = os.path.join(screenshots_dir, f"{item.name}_failed.png")
                driver.save_screenshot(failure_screenshot_file)
                add_attachment(failure_screenshot_file, f"Failure Screenshot for test {item.name}")
        

class Config:
    BASE_URL = 'https://www.saucedemo.com/'





