# Test Running Guide

This guide lists valid commands for the current repository.

## Activate Environment

Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

## Core Commands

### Full suite (all tests under test/)

```bash
python -m pytest test
```

### Full suite with report

```bash
python -m pytest test --browser Chrome --html=reports/report.html --self-contained-html
```

### Targeted folder

```bash
python -m pytest test/login_tests -v
python -m pytest test/home_page_tests -v
python -m pytest test/shopping_cart_tests -v
```

### Targeted file

```bash
python -m pytest test/login_tests/test_login.py -v
python -m pytest test/shopping_cart_tests/test_checkout_shopping_cart.py -v
```

### Browser-specific runs

```bash
python -m pytest test --browser Chrome -v
python -m pytest test --browser Edge -v
```

Note: Firefox is not currently an active target in fixture logic.

### Marker runs

```bash
python -m pytest -m selenium -v
```

## Report Viewing

After generation:

- Open `reports/report.html` in a browser
- Use the Links column per test for artifacts

## Environment Variables Used at Runtime

From `conftest.py`:

- `TEST_CAPTURE_LOCAL_VIDEO`
- `TEST_VIDEO_FPS`
- `TEST_VIDEO_URL`
- `TEST_VIDEO_URL_TEMPLATE`
- `CI`
- `TF_BUILD`

From env login path (`login_env`):

- `LOGIN_USERNAME`
- `LOGIN_PASSWORD`
