import subprocess

def menu():
    print("Select an operation:")
    print("1. Run all browser tests")
    print("2. Run Chrome tests")
    print("3. Run Edge tests")
    print("4. Run Firefox tests")
    print("5. Run Admin tests")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter choice (1/2/3/4/5/6): ")
    if choice == '1':
        print("Running all browser tests...")
        commands = ["pytest --browser=Chrome --html=reports/chrome_report.html", 
                    "pytest --browser=Edge --html=reports/edge_report.html", 
                    "pytest --browser=Firefox --html=reports/firefox_report.html"]
        processes = []

        for command in commands:
            process = subprocess.Popen(command, shell=True)
            processes.append(process)

        for process in processes:
            process.wait()
    
    elif choice == '2':
            print("Running tests in Chrome")
            subprocess.run("pytest --browser=Chrome --html=reports/chrome_report.html")
            print("Chrome Tests Complete!")
    elif choice == '3':
            print("Running tests in Edge")
            subprocess.run("pytest --browser=Edge --html=reports/edge_report.html")
            print("Edge Tests Complete!")
    elif choice == '4':
            print("Running tests in Firefox")
            subprocess.run("pytest --browser=Firefox --html=reports/firefox_report.html")
            print("Firefox Tests Complete!")
    elif choice == '5':
            print("Running Admin tests - Prepare to choose a browser...")
            browser_choice = input("Enter browser: Chrome, Edge, Firefox, or All  ")
            if browser_choice == "Chrome":
                print("You chose Chrome - Running Admin tests...")
                subprocess.run("pytest -k test_admin --browser=Chrome --html=reports/chrome_admin_report.html")
            elif browser_choice == "Edge":
                print("You chose Edge - Running Admin tests...")
                subprocess.run("pytest -k test_admin --browser=Edge --html=reports/edge_admin_report.html")
            elif browser_choice == "Firefox":
                print("You chose Firefox - Running Admin tests...")
                subprocess.run("pytest -k test_admin --browser=Firefox --html=reports/firefox_admin_report.html")
            elif browser_choice == "All":
                print("Running all browser tests...")
                commands = ["pytest -k test_admin --browser=Chrome --html=reports/chrome_admin_report.html", 
                            "pytest -k test_admin --browser=Edge --html=reports/edge_admin_report.html", 
                            "pytest -k test_admin --browser=Firefox --html=reports/firefox_admin_report.html"]
                processes = []

                for command in commands:
                    process = subprocess.Popen(command, shell=True)
                    processes.append(process)

                for process in processes:
                    process.wait()
            else:
                 print("Invalid Choice, please choose a supported browser option.")

    elif choice == '6':
        print("Exiting the testing program. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 6.")














# commands = ["pytest --browser=Chrome --html=reports/chrome_report.html", "pytest --browser=Edge --html=reports/edge_report.html", "pytest --browser=Firefox --html=reports/firefox_report.html"]
# processes = []

# for command in commands:
#     process = subprocess.Popen(command, shell=True)
#     processes.append(process)

# for process in processes:
#     process.wait()




## OLD VERSION - BUT STILL WORKS, JUST PROCEDURALLY ##
# subprocess.run("pytest --browser=Chrome --html=reports/chrome_report.html")
# subprocess.run("pytest --browser=Edge --html=reports/edge_report.html")
# subprocess.run("pytest --browser=Firefox --html=reports/firefox_report.html")