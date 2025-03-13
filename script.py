import subprocess
import os
import webbrowser

def menu():
    print("#########################################################################")
    print("#########################################################################")
    print("Welcome to the MTT Automated Testing Suite - Featuring Selenium Webdriver with pytest")
    print("-------------------------------------------------------------------------")
    print("Select an operation:")
    print("1. Test all browsers")
    print("2. Test one browser")
    print("3. 200 Status tests")
    print("4. Run single test")
    print("5. Create MIPR test")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == '1':
        print("Running all browser tests...")
        commands = ["pytest --browser=Chrome --html=reports/browser_reports/chrome/chrome_report.html", 
                    "pytest --browser=Edge --html=reports/browser_reports/edge/edge_report.html", 
                    "pytest --browser=Firefox --html=reports/browser_reports/firefox/firefox_report.html"]
        processes = []

        for command in commands:
            process = subprocess.Popen(command, shell=True)
            processes.append(process)

        for process in processes:
            process.wait()
        
        chrome_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\browser_reports\chrome\chrome_report.html'
        edge_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\browser_reports\edge\edge_report.html'
        firefox_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\browser_reports\firefox\firefox_report.html'
        webbrowser.open_new_tab(f'{os.path.realpath(chrome_file_path)}')
        webbrowser.open_new_tab(f'{os.path.realpath(edge_file_path)}')
        webbrowser.open_new_tab(f'{os.path.realpath(firefox_file_path)}')
        print("Testing Complete. Please see specific browser reports in '/reports/browser_reports.'")


    elif choice == '2':
            browser_choice = input("Select a browser to test (Chrome, Edge, or Firefox):  ")
            if browser_choice == "Chrome":
                print("You chose Chrome - Running tests...")
                subprocess.run("pytest --browser=Chrome --html=reports/browser_reports/chrome/chrome_report.html")
                print("Testing Complete. Please see Chrome browser report in '/reports/browser_reports/chrome.'")
                chrome_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\browser_reports\chrome\chrome_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(chrome_file_path)}')

            elif browser_choice == "Edge":
                print("You chose Edge - Running tests...")
                subprocess.run("pytest --browser=Edge --html=reports/browser_reports/edge/edge_report.html")
                print("Testing Complete. Please see Edge browser report in '/reports/browser_reports/edge/.'")
                edge_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\browser_reports\edge\edge_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(edge_file_path)}')

            elif browser_choice == "Firefox":
                print("You chose Firefox - Running tests...")
                subprocess.run("pytest --browser=Firefox --html=reports/browser_reports/firefox/firefox_report.html")
                print("Testing Complete. Please see Firefox browser report in '/reports/browser_reports/firefox/.'")
                firefox_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\browser_reports\firefox\firefox_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(firefox_file_path)}')

            else:
                 print("Invalid choice, please select an approved browser.")


    elif choice == '3':
            browser_choice = input("Select a browser to test (Chrome, Edge, Firefox, or All):  ")
            if browser_choice == "Chrome":
                print("You chose Chrome - Running tests...")
                subprocess.run("pytest -k test_200 --browser=Chrome --html=reports/status_reports/chrome_200_status_report.html")
                print("200 Status Testing Complete. Please see Chrome report in '/reports/status_reports.'")
                chrome_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\status_reports\chrome_200_status_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(chrome_file_path)}')

            elif browser_choice == "Edge":
                print("You chose Edge - Running tests...")
                subprocess.run("pytest -k test_200 --browser=Edge --html=reports/status_reports/edge_200_status_report.html")
                print("200 Status Testing Complete. Please see Edge report in '/reports/status_reports.'")
                edge_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\status_reports\edge_200_status_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(edge_file_path)}')

            elif browser_choice == "Firefox":
                print("You chose Firefox - Running tests...")
                subprocess.run("pytest -k test_200 --browser=Firefox --html=reports/status_reports/firefox_200_status_report.html")
                print("200 Status Testing Complete. Please see Firefox report in '/reports/status_reports.'")
                firefox_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\status_reports\firefox_200_status_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(firefox_file_path)}')

            elif browser_choice == "All":
                print("You chose All Browsers - Running tests...")
                commands = ["pytest -k test_200 --browser=Chrome --html=reports/status_reports/chrome_200_status_report.html", 
                            "pytest -k test_200 --browser=Edge --html=reports/status_reports/edge_200_status_report.html", 
                            "pytest -k test_200 --browser=Firefox --html=reports/status_reports/firefox_200_status_report.html"]
                processes = []

                for command in commands:
                    process = subprocess.Popen(command, shell=True)
                    processes.append(process)

                for process in processes:
                    process.wait()

                chrome_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\browser_reports\chrome\chrome_report.html'
                edge_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\browser_reports\edge\edge_report.html'
                firefox_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\browser_reports\firefox\firefox_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(chrome_file_path)}')
                webbrowser.open_new_tab(f'{os.path.realpath(edge_file_path)}')
                webbrowser.open_new_tab(f'{os.path.realpath(firefox_file_path)}')
                print("200 Status Testing Complete. Please see reports in '/reports/status_reports.'")

            else:
                print("Invalid choice, please select an approved browser.")


    elif choice == '4':
            test_choice = input("Enter a test name (please include file extension '.py'): ")
            print("You have submitted: " + str(test_choice))         
            print("Please choose one browser or all browsers")
            browser_choice = input("Enter browser (Chrome, Edge, Firefox, or All):  ")
            if browser_choice == "Chrome":
                print("Running test " + str(test_choice) + " with Chrome ...")
                subprocess.run("pytest -k " + str(test_choice) + " --browser=Chrome --html=reports/single_tests/chrome_single_test_report.html")
                print("Testing Complete. Please see Chrome browser report in '/reports.'")
                chrome_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\single_tests\chrome_single_test_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(chrome_file_path)}')
            elif browser_choice == "Edge":
                print("Running test " + str(test_choice) + " with Edge ...")
                subprocess.run("pytest -k " + str(test_choice) + " --browser=Edge --html=reports/single_tests/edge_single_test_report.html")
                print("Testing Complete. Please see Edge browser report in '/reports.'")
                edge_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\single_tests\edge_single_test_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(edge_file_path)}')
            elif browser_choice == "Firefox":
                print("Running test " + str(test_choice) + " with Firefox ...")
                subprocess.run("pytest -k " + str(test_choice) + " --browser=Firefox --html=reports/single_tests/firefox_single_test_report.html")
                print("Testing Complete. Please see Firefox browser report in '/reports.'")
                firefox_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\single_tests\firefox_single_test_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(firefox_file_path)}')
            elif browser_choice == "All":
                print("Running test " + str(test_choice) + " with all browsers...")
                commands = ["pytest -k " + str(test_choice) + " --browser=Chrome --html=reports/single_tests/chrome_single_test_report.html", 
                            "pytest -k " + str(test_choice) + " --browser=Edge --html=reports/single_tests/edge_single_test_report.html", 
                            "pytest -k " + str(test_choice) + " --browser=Firefox --html=reports/single_tests/firefox_single_test_report.html"]
                processes = []

                for command in commands:
                    process = subprocess.Popen(command, shell=True)
                    processes.append(process)

                for process in processes:
                    process.wait()

                chrome_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\single_tests\chrome_single_test_report.html'
                edge_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\single_tests\edge_single_test_report.html'
                firefox_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\single_tests\firefox_single_test_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(chrome_file_path)}')
                webbrowser.open_new_tab(f'{os.path.realpath(edge_file_path)}')
                webbrowser.open_new_tab(f'{os.path.realpath(firefox_file_path)}')
                    
            else:
                 print("Invalid choice, please select an approved browser.")



    elif choice == '5':
            print("Running Create MIPR test...")
            browser_choice = input("Enter browser (Chrome, Edge, Firefox, or All):  ")
            if browser_choice == "Chrome":
                print("You chose Chrome - Creating MIPR...")
                subprocess.run("pytest -k test_create_mipr.py --browser=Chrome --html=reports/mipr_creation/chrome_create_mipr_report.html")
                print("Testing Complete. Please see Chrome browser report in '/reports.'")
                chrome_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\mipr_creation\chrome_create_mipr_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(chrome_file_path)}')

            elif browser_choice == "Edge":
                print("You chose Edge - Creating MIPR...")
                subprocess.run("pytest -k test_create_mipr.py --browser=Edge --html=reports/mipr_creation/edge_create_mipr_report.html")
                print("Testing Complete. Please see Edge browser report in '/reports.'")
                edge_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\mipr_creation\edge_create_mipr_report.html'
                webbrowser.open_new_tab(f'{os.path.realpath(edge_file_path)}')

            elif browser_choice == "Firefox":
                print("You chose Firefox - Creating MIPR...")
                subprocess.run("pytest -k test_create_mipr.py --browser=Firefox --html=reports/firefox_create_mipr_report.html")
                print("Testing Complete. Please see Firefox browser report in '/reports.'")
                firefox_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\mipr_creation\firefox_create_mipr_report.htmll'
                webbrowser.open_new_tab(f'{os.path.realpath(firefox_file_path)}')

            elif browser_choice == "All":
                print("Creating MIPRs with all browsers...")
                commands = ["pytest -k test_create_mipr.py --browser=Chrome --html=reports/chrome_create_mipr_report.html", 
                            "pytest -k test_create_mipr.py --browser=Edge --html=reports/edge_create_mipr_report.html", 
                            "pytest -k test_create_mipr.py --browser=Firefox --html=reports/firefox_create_mipr_report.html"]
                processes = []

                for command in commands:
                    process = subprocess.Popen(command, shell=True)
                    processes.append(process)

                for process in processes:
                    process.wait()

                chrome_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\mipr_creation\chrome_create_mipr_report.html'
                edge_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\mipr_creation\edge_create_mipr_report.html'
                firefox_file_path = r'C:\Users\daniel.pearson\OneDrive - Akima\Desktop\Projects\MTT_4.0\reports\mipr_creation\firefox_create_mipr_report.htmll'
                webbrowser.open_new_tab(f'{os.path.realpath(chrome_file_path)}')
                webbrowser.open_new_tab(f'{os.path.realpath(edge_file_path)}')
                webbrowser.open_new_tab(f'{os.path.realpath(firefox_file_path)}')



            else:
                 print("Invalid choice, please select an approved browser.")


    elif choice == '6':
        print("Exiting the testing suite. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 6.")

