import subprocess

subprocess.run("pytest --browser=Chrome --html=reports/chrome_report.html")
subprocess.run("pytest --browser=Edge --html=reports/edge_report.html")
subprocess.run("pytest --browser=Firefox --html=reports/firefox_report.html")