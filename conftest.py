# conftest.py
from selenium import webdriver
import os
import platform
import json
import re
from datetime import datetime
from pathlib import Path
from html import escape
import pytest
import requests
import pytest_html


RUN_ARTIFACT_DIR = Path(os.getcwd()) / "reports" / "artifacts" / datetime.now().strftime("%Y%m%d_%H%M%S")

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


def _is_ci():
    return os.environ.get("CI") == "true" or os.environ.get("TF_BUILD") == "True"


def _slugify(value):
    return re.sub(r"[^a-zA-Z0-9_.-]", "_", value)


def _get_test_artifact_dir(item):
    test_id = _slugify(item.nodeid)
    path = RUN_ARTIFACT_DIR / test_id
    path.mkdir(parents=True, exist_ok=True)
    return path


def _write_json(path, payload):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)


def _safe_driver_log(driver, log_type):
    try:
        return driver.get_log(log_type)
    except Exception as err:
        return [{"error": f"Unable to fetch {log_type} logs", "details": str(err)}]


def _report_output_path(item):
    htmlpath = getattr(item.config.option, "htmlpath", None)
    if htmlpath:
        return Path(htmlpath).resolve()
    return (Path(os.getcwd()) / "reports" / "report.html").resolve()


def _relative_path_for_report(path, item):
    report_dir = _report_output_path(item).parent
    try:
        return path.resolve().relative_to(report_dir).as_posix()
    except ValueError:
        return os.path.relpath(path.resolve(), report_dir).replace("\\", "/")


def _resolve_video_url(item, driver):
    # Option 1: explicit URL from environment
    direct_url = os.environ.get("TEST_VIDEO_URL")
    if direct_url:
        return direct_url

    # Option 2: template URL that can reference test name
    template = os.environ.get("TEST_VIDEO_URL_TEMPLATE")
    if template:
        return template.format(test_name=item.name, nodeid=item.nodeid)

    # Option 3: best-effort extraction from driver capabilities (remote providers)
    try:
        caps = driver.capabilities or {}
    except Exception:
        caps = {}

    for key in ["video", "video_url", "videoUrl", "se:videoUrl"]:
        if caps.get(key):
            return str(caps.get(key))

    selenoid = caps.get("selenoid:options", {})
    if isinstance(selenoid, dict) and selenoid.get("videoName"):
        return str(selenoid.get("videoName"))

    return None


def _pretty_html_source(html_source):
    # Lightweight HTML pretty-printer for report readability.
    tokens = re.findall(r"<!--.*?-->|<![^>]*>|<[^>]+>|[^<]+", html_source, flags=re.DOTALL)
    void_tags = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr",
    }

    indent = 0
    pretty_lines = []

    for token in tokens:
        part = token.strip()
        if not part:
            continue

        if part.startswith("<!--"):
            pretty_lines.append(("  " * indent) + part)
            continue

        if part.startswith("<"):
            if re.match(r"</\s*[^>]+>", part):
                indent = max(0, indent - 1)
                pretty_lines.append(("  " * indent) + part)
                continue

            pretty_lines.append(("  " * indent) + part)

            if part.startswith("<!") or part.endswith("/>"):
                continue

            open_match = re.match(r"<\s*([a-zA-Z0-9:-]+)", part)
            close_match = re.match(r"<\s*/\s*([a-zA-Z0-9:-]+)", part)
            tag_name = open_match.group(1).lower() if open_match else ""
            closes_same_tag = close_match and open_match and close_match.group(1).lower() == tag_name

            if tag_name and tag_name not in void_tags and not closes_same_tag and not part.startswith("</"):
                indent += 1
            continue

        # Text content
        text = re.sub(r"\s+", " ", part).strip()
        if text:
            pretty_lines.append(("  " * indent) + text)

    return "\n".join(pretty_lines)


def _write_styled_page_source(path, *, page_source, test_name, nodeid, current_url, title):
    pretty_source = _pretty_html_source(page_source)
    styled_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>Page Source Viewer - {escape(test_name)}</title>
    <style>
        :root {{
            --bg: #f6f8fb;
            --panel: #ffffff;
            --text: #1f2d3d;
            --muted: #5b6b7c;
            --border: #d9e2ec;
            --accent: #1f7a8c;
            --code-bg: #0f1720;
            --code-text: #e5edf5;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            margin: 0;
            font-family: "Segoe UI", Tahoma, sans-serif;
            background: linear-gradient(135deg, #eef5ff, #f8fbff 45%, #eefbf7);
            color: var(--text);
        }}
        .wrap {{
            max-width: 1200px;
            margin: 24px auto;
            padding: 0 16px;
        }}
        .card {{
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(10, 35, 66, 0.08);
            overflow: hidden;
        }}
        .header {{
            padding: 16px 20px;
            border-bottom: 1px solid var(--border);
            background: linear-gradient(90deg, #f4f9ff, #f9fffb);
        }}
        .title {{
            margin: 0;
            font-size: 20px;
            font-weight: 700;
            color: #153b52;
        }}
        .meta {{
            margin-top: 10px;
            display: grid;
            grid-template-columns: 140px 1fr;
            gap: 6px 10px;
            font-size: 13px;
        }}
        .meta .key {{ color: var(--muted); font-weight: 600; }}
        .meta .val {{ word-break: break-word; }}
        .code-wrap {{
            background: var(--code-bg);
            color: var(--code-text);
            padding: 14px 16px;
            max-height: 75vh;
            overflow: auto;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
        }}
        pre {{
            margin: 0;
            white-space: pre;
            font-size: 12px;
            line-height: 1.45;
            font-family: Consolas, "Courier New", monospace;
        }}
    </style>
</head>
<body>
    <div class=\"wrap\">
        <div class=\"card\">
            <div class=\"header\">
                <h1 class=\"title\">Captured Page Source</h1>
                <div class=\"meta\">
                    <div class=\"key\">Test Name</div><div class=\"val\">{escape(test_name)}</div>
                    <div class=\"key\">Node ID</div><div class=\"val\">{escape(nodeid)}</div>
                    <div class=\"key\">Page Title</div><div class=\"val\">{escape(title)}</div>
                    <div class=\"key\">Page URL</div><div class=\"val\">{escape(current_url)}</div>
                </div>
            </div>
            <div class=\"code-wrap\">
                <pre>{escape(pretty_source)}</pre>
            </div>
        </div>
    </div>
</body>
</html>
"""
    path.write_text(styled_html, encoding="utf-8")


def _collect_test_artifacts(item, report, driver):
    artifact_dir = _get_test_artifact_dir(item)
    artifacts = {}

    screenshot_file = artifact_dir / "screenshot.png"
    driver.save_screenshot(str(screenshot_file))
    artifacts["screenshot_file"] = screenshot_file

    screenshot_b64 = driver.get_screenshot_as_base64()
    artifacts["screenshot_b64"] = screenshot_b64

    html_file = artifact_dir / "page_source.html"
    html_file.write_text(driver.page_source, encoding="utf-8")
    artifacts["page_source_file"] = html_file

    styled_html_file = artifact_dir / "page_source_viewer.html"
    _write_styled_page_source(
        styled_html_file,
        page_source=driver.page_source,
        test_name=item.name,
        nodeid=item.nodeid,
        current_url=driver.current_url,
        title=driver.title,
    )
    artifacts["page_source_viewer_file"] = styled_html_file

    browser_logs = _safe_driver_log(driver, "browser")
    browser_log_file = artifact_dir / "browser_console.json"
    _write_json(browser_log_file, browser_logs)
    artifacts["browser_log_file"] = browser_log_file
    artifacts["browser_log_count"] = len(browser_logs)

    performance_logs = _safe_driver_log(driver, "performance")
    perf_log_file = artifact_dir / "performance_log.json"
    _write_json(perf_log_file, performance_logs)
    artifacts["performance_log_file"] = perf_log_file
    artifacts["performance_log_count"] = len(performance_logs)

    metadata_file = artifact_dir / "test_metadata.json"
    _write_json(
        metadata_file,
        {
            "test_name": item.name,
            "nodeid": item.nodeid,
            "outcome": report.outcome,
            "duration_seconds": report.duration,
            "url": driver.current_url,
            "title": driver.title,
            "captured_at": datetime.now().isoformat(),
        },
    )
    artifacts["metadata_file"] = metadata_file

    video_url = _resolve_video_url(item, driver)
    if video_url:
        artifacts["video_url"] = video_url

    return artifacts



@pytest.fixture(scope="function", autouse=True)     
def config_browser(browser):
        if  browser == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--incognito")
            options.set_capability("goog:loggingPrefs", {"browser": "ALL", "performance": "ALL"})
            options.add_experimental_option(
                "prefs",
                {
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False,
                    "profile.password_manager_leak_detection": False,
                    "autofill.profile_enabled": False,
                    "autofill.credit_card_enabled": False,
                },
            )
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
            options.add_argument("--inprivate")
            options.set_capability("goog:loggingPrefs", {"browser": "ALL", "performance": "ALL"})
            options.add_experimental_option(
                "prefs",
                {
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False,
                    "profile.password_manager_leak_detection": False,
                    "autofill.profile_enabled": False,
                    "autofill.credit_card_enabled": False,
                },
            )
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
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when != "call":
        return

    driver = item.funcargs.get("config_browser")
    if driver is None:
        return

    artifacts = _collect_test_artifacts(item, report, driver)

    extras.append(
        pytest_html.extras.image(
            artifacts["screenshot_b64"],
            mime_type="image/png",
            extension="png",
        )
    )

    extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["screenshot_file"], item), name="Screenshot File"))
    extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["page_source_viewer_file"], item), name="Page Source (Styled)"))
    extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["page_source_file"], item), name="Page Source (Raw)"))
    extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["browser_log_file"], item), name="Browser Console Log"))
    extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["performance_log_file"], item), name="Performance Log"))
    extras.append(pytest_html.extras.url(_relative_path_for_report(artifacts["metadata_file"], item), name="Test Metadata"))

    if artifacts.get("video_url"):
        extras.append(pytest_html.extras.url(artifacts["video_url"], name="Video Artifact"))

    report.extras = extras

    if _is_ci():
        screenshots_dir = Path(os.getcwd()) / "screenshots"
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        screenshot_file = screenshots_dir / f"{_slugify(item.name)}.png"
        driver.save_screenshot(str(screenshot_file))

        try:
            add_attachment = item._request.getfixturevalue("add_pipelines_attachment")
            add_attachment(str(screenshot_file), f"Screenshot for test {item.name}")
        except Exception:
            pass

    xfail = hasattr(report, "wasxfail")
    if (report.skipped and xfail) or (report.failed and not xfail):
        failure_file = artifacts["screenshot_file"].with_name("failure_screenshot.png")
        driver.save_screenshot(str(failure_file))

        if _is_ci():
            try:
                add_attachment = item._request.getfixturevalue("add_pipelines_attachment")
                add_attachment(str(failure_file), f"Failure Screenshot for test {item.name}")
            except Exception:
                pass
        

class Config:
    BASE_URL = 'https://www.saucedemo.com/'





