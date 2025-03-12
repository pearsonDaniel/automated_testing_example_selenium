import subprocess

commands = ["pytest --browser=Chrome --html=reports/chrome_report.html", "pytest --browser=Edge --html=reports/edge_report.html", "pytest --browser=Firefox --html=reports/firefox_report.html"]
processes = []

for command in commands:
    process = subprocess.Popen(command, shell=True)
    processes.append(process)

for process in processes:
    process.wait()




## OLD VERSION - BUT STILL WORKS, JUST PROCEDURALLY ##
# subprocess.run("pytest --browser=Chrome --html=reports/chrome_report.html")
# subprocess.run("pytest --browser=Edge --html=reports/edge_report.html")
# subprocess.run("pytest --browser=Firefox --html=reports/firefox_report.html")