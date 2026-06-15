# Test Debugging and Common Errors

This guide maps common failure modes to concrete checks in this repository.

## 1) Pytest Launcher Errors

Symptom:

- Fatal launcher errors referencing an old Python path

Cause:

- Moved project path or stale entry point scripts in virtual environment

Fix:

```bash
python -m pytest test
```

If needed:

```bash
python -m pip install --force-reinstall pytest
```

## 2) Environment Variable Login Fails

Symptom:

- `Missing required environment variables LOGIN_USERNAME and LOGIN_PASSWORD.`

Cause:

- `.env` missing, not loaded, or variables unset

Fix:

1. Copy `.env.example` to `.env`
2. Set `LOGIN_USERNAME` and `LOGIN_PASSWORD`
3. Re-run `test/login_tests/test_login_env.py`

## 3) Browser Not Supported

Symptom:

- Browser value unsupported in fixture

Cause:

- Invalid `--browser` value

Fix:

Use only currently implemented values:

```bash
python -m pytest test --browser Chrome
python -m pytest test --browser Edge
```

## 4) HTTP Status Assertion Issues

Symptom:

- HTTP 200 verification fails

Context:

- `BasePage.verify_page_http_200_response` uses `requests.head` and has SSL fallback behavior

Checks:

1. Confirm target URL is reachable
2. Confirm network/proxy restrictions
3. Confirm certificate interception policies

## 5) Report Missing Artifacts

Symptom:

- Report generated but artifact links missing/broken

Checks:

1. Ensure run used `--html=reports/report.html`
2. Ensure hook in `conftest.py` is unchanged
3. Confirm artifact folders exist under `reports/artifacts/`

## 6) Video Not Present

Checks:

1. `TEST_CAPTURE_LOCAL_VIDEO` not disabled
2. ffmpeg process can run on host
3. Video file has non-zero size in artifact folder

## 7) Spreadsheet Credential Issues

Symptom:

- Login tests fail before UI login action

Cause:

- `test/test_resources/user_credentials.xlsx` missing or malformed

Fix:

- Verify workbook exists and row 2 column 1/2 values are valid
