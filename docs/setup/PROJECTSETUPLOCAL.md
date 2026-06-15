# Project Setup (Local)

This guide is synchronized to the current repository implementation.

## 1. Prerequisites

- Git
- Python 3.12+
- Google Chrome and/or Microsoft Edge

## 2. Clone Repository

```bash
git clone https://github.com/pearsonDaniel/automated_testing_example_selenium.git
cd automated_testing_example_selenium
```

## 3. Create Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install selenium pytest pytest-html requests openpyxl Faker imageio-ffmpeg
```

These packages map directly to current imports in `conftest.py`, `src/pages/base_page.py`, `src/pages/login_page.py`, and test modules.

## 5. Verify Setup

```bash
python --version
python -m pytest --version
```

Optional quick check:

```bash
python -m pytest test/login_tests/test_login.py -v
```

## 6. Environment Data Options

### Option A: Spreadsheet-backed login (default path in code)

- File required: `test/test_resources/user_credentials.xlsx`
- Used by: `src/pages/login_page.py` method `login()`

### Option B: Environment-variable login

1. Copy template:

```bash
cp .env.example .env
```

Windows alternative:

```powershell
Copy-Item .env.example .env
```

2. Set values in `.env`:

- `LOGIN_USERNAME`
- `LOGIN_PASSWORD`

3. Run test using env credentials:

```bash
python -m pytest test/login_tests/test_login_env.py -v
```

Note: VS Code settings currently specify `.env` loading via `python.envFile` in `.vscode/settings.json`.

## 7. Browser and Driver Behavior

Implemented in `conftest.py` fixture `config_browser`:

- Chrome: supported
- Edge: supported
- Firefox: currently not active (fixture returns `None`)

Browser drivers are managed by Selenium Manager in current Selenium versions; no manual driver executable path is required in this repository.

## 8. Video Runtime Notes

Local test video recording uses ffmpeg via `imageio-ffmpeg` and is enabled by default.

Primary env vars:

- `TEST_CAPTURE_LOCAL_VIDEO` (default true)
- `TEST_VIDEO_FPS` (default 20)

If your environment blocks bundled ffmpeg provisioning, install ffmpeg manually for your OS.
