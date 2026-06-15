# Test Results and Reporting

This project uses `pytest-html` with custom enrichment from `conftest.py`.

## How Reports Are Produced

Run:

```bash
python -m pytest test --browser Chrome --html=reports/report.html --self-contained-html
```

The hook `pytest_runtest_makereport` executes on test call phase and appends pytest-html extras.

## What Is Captured Per Test

- Embedded screenshot preview
- Link to screenshot file
- Link to raw page source
- Link to styled page-source viewer
- Link to browser console JSON log
- Link to performance JSON log
- Link to metadata JSON
- Link to local MP4 video (if enabled)
- Link to remote video URL (if configured)

## Artifact Storage Layout

`reports/artifacts/<timestamp>/<test_nodeid>/`

Each folder contains the evidence bundle for exactly one test node id.

## Video Capture Controls

- `TEST_CAPTURE_LOCAL_VIDEO`: on/off
- `TEST_VIDEO_FPS`: numeric frame rate

If local recorder is active, video file is `test_video.mp4`.

## CI Behavior

When `CI=true` or `TF_BUILD=True`, additional screenshot files are created and the hook attempts pipeline attachment via fixture lookup.

## Reading Failures Efficiently

1. Open failed row in report
2. Check screenshot first
3. Open page-source viewer
4. Inspect browser console log
5. Inspect performance log
6. Confirm URL/title in metadata JSON
