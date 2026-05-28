
# Selenium & Pytest UI Automation Framework

This repository demonstrates a modern, maintainable UI automation framework using Selenium and Pytest. It is structured for clarity and educational value, focusing on best practices in test automation.

## Quick Start

**Requirements:**
- Python 3.12+
- Git
- Google Chrome and/or Microsoft Edge
- PowerShell (for Windows users)

**Setup:**
1. Clone the repository:
	```powershell
	git clone https://github.com/pearsonDaniel/automated_testing_example_selenium.git
	cd automated_testing_example_selenium
	```
2. Create and activate a virtual environment:
	```powershell
	python -m venv selenium-venv
	Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
	.\selenium-venv\Scripts\Activate.ps1
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	```
3. Copy `.env.example` to `.env` and fill in any required environment variables (credentials, etc.).

**Run all tests and generate an HTML report:**
```powershell
pytest --html=reports/report.html --self-contained-html
```

## Project Structure
- `conftest.py`: Pytest configuration, fixtures, and browser setup logic.
- `src/pages/`: Page object classes, with a shared base class for common actions.
- `locators/`: All element selectors, organized by feature or page.
- `test/`: Test suites, organized by feature (e.g., login, shopping cart).
- `reports/`: HTML reports and assets (ignored by git).
- `.env.example`: Template for required environment variables.
- `.gitignore`: Excludes local environments, reports, and sensitive files from version control.
- `script.py`: Utility or runner script for automation tasks.

## Test & Page Object Model
- **Test logic is contained within methods**: Each test method performs a specific scenario, calling reusable page object methods for actions and assertions.
- **Tests call page object methods**: Test files import page classes and invoke their methods to interact with the UI, ensuring DRY and readable test code.
- **Fixtures and resources**: Pytest fixtures in `conftest.py` manage browser setup, teardown, and configuration. Test resources (such as test data or environment variables) are loaded as needed.
- **Page Object Model**: All UI logic is encapsulated in page classes under `src/pages/`, each inheriting from a shared `BasePage` for universal actions.
- **Locators**: All element locators are separated into dedicated modules under `locators/`, grouped by feature or page.

## Dependencies
- selenium
- pytest
- pytest-html
- requests
- openpyxl
- Faker

## References
- Selenium: https://www.selenium.dev/documentation/
- Pytest: https://docs.pytest.org/en/stable/
- Pytest HTML: https://pytest-html.readthedocs.io/en/latest/
