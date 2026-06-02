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
    python -m pip install selenium pytest pytest-html requests openpyxl Faker imageio-ffmpeg
    ```
3. Copy `.env.example` to `.env` and fill in any required environment variables (credentials, etc.).

**Video runtime note:**
- Local video capture uses ffmpeg through `imageio-ffmpeg`.
- In most environments, no separate global ffmpeg install is required.
- If your environment blocks the bundled binary download, install ffmpeg manually (Windows examples):
    ```powershell
    winget install Gyan.FFmpeg
    # or
    choco install ffmpeg
    ```

**Run all tests and generate an HTML report:**
```powershell
pytest --html=reports/report.html --self-contained-html
```

## Project Structure
- `conftest.py`: Pytest configuration, fixtures, and browser setup logic.
- `pytest.ini`: Pytest marker registration and shared run configuration.
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
- **Fixtures and resources**: Pytest fixtures in `conftest.py` manage browser setup, teardown, and configuration.
- **Fixture injection best practice**: Page-object-model tests now consume fixtures through function arguments (for example, `config_browser` and `base_url`) without importing fixtures directly from `conftest.py`.
- **Page Object Model**: All UI logic is encapsulated in page classes under `src/pages/`, each inheriting from a shared `BasePage` for universal actions.
- **Locators**: All element locators are separated into dedicated modules under `locators/`, grouped by feature or page.

## Recent Updates
- Registered `@pytest.mark.selenium` in `pytest.ini` to remove unknown-marker warnings.
- Added a session-scoped `base_url` fixture in `conftest.py` and refactored non-procedural tests to use fixture injection.
- Updated HTTP 200 verification in `src/pages/base_page.py` to use verified TLS first, with a controlled fallback for environments that present intercepted/self-signed certificate chains.
- Added full local video capture using an ffmpeg process during test execution, with per-test MP4 artifacts linked and embedded in the pytest-html report.
- Retained the procedural demo test (`test/procedural_demo/test_google_search.py`) as a baseline instructional example, including direct `conftest` imports by design.

## Enhanced Reporting
- The `pytest-html` report embeds a screenshot preview for each test in self-contained mode.
- The report `Links` column includes artifact links per test:
    - Screenshot File
    - Page Source (Styled)
    - Page Source (Raw)
    - Browser Console Log (JSON)
    - Performance Log (JSON)
    - Test Metadata (JSON)
    - Test Video (local MP4)
- Artifacts are stored under `reports/artifacts/<timestamp>/<test_nodeid>/`.
- `Page Source (Styled)` opens a readable viewer with metadata and pretty-printed HTML in a code panel.
- Optional video links can be attached via environment variables (`TEST_VIDEO_URL` or `TEST_VIDEO_URL_TEMPLATE`).
- Local video capture controls:
    - `TEST_CAPTURE_LOCAL_VIDEO` (`true` by default): enable or disable local recording.
    - `TEST_VIDEO_FPS` (`20` by default): adjust capture smoothness and file size.

## Local Video Capture Notes
- Local recording uses ffmpeg desktop capture during each test and writes `test_video.mp4` into that test's artifact folder.
- The report includes both a clickable `Test Video` link and an inline HTML5 video player block in the extras section.
- `--self-contained-html` still produces links to artifact files (including video) because binary MP4 assets are not inlined.

## Dependencies
- selenium
- pytest
- pytest-html
- requests
- openpyxl
- Faker
- imageio-ffmpeg
- ffmpeg (runtime used by local test video capture; typically provisioned via imageio-ffmpeg)

## References
- Selenium: https://www.selenium.dev/documentation/
- Pytest: https://docs.pytest.org/en/stable/
- Pytest HTML: https://pytest-html.readthedocs.io/en/latest/

