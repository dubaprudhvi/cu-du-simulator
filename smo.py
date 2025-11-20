
import config.config as config
import connect.connect as connect
import fault.fault as fault
import kpi.kpi as kpi
import xmlfiles.kpixml as kpixml
import mplane.mplane as mplane

from utils.imports import *

def main_menu():
    while True:
        try:
            init_options = inquirer.select(
                            message="RAN CONTROLLER",
                            border=True,
                            choices=[
                                "CONNECT APP",
                                "FAULT MANAGEMENT",
                                "KPI METRICS",
                                "GENERATE XML FILES",
                                "M-PLANE",
                                "READ AND UPDATE CONFIGS",
                                Separator(),
                                "EXIT",
                            ],
                        ).execute()
            parse_init_options(init_options)
        
        except KeyboardInterrupt:
            print( "\nCtrl+C detected. Exiting the program...")
            sys.exit()
        except Exception as e:
            print( f"{e}")

def parse_init_options(choice):
    if choice == "CONNECT APP":
        connect.connect_app_menu()
    elif choice == "FAULT MANAGEMENT":
        fault.fault_app_menu()
    elif choice == "KPI METRICS":
        kpi.kpi_menu()
    elif choice == "GENERATE XML FILES":
        kpixml.kpi_xml_menu()
    elif choice == "M-PLANE":
        mplane.mplane_app_menu()
    elif choice == "READ AND UPDATE CONFIGS":
        config.config_menu()
    elif choice == "EXIT":
        print("Exiting the program")
        sys.exit()
    else:
        print("Invalid option. please try again.")

if __name__ == "__main__":
    main_menu()
