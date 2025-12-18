from utils.imports import *
import mplane.fault.mplanefault as mplanefault
import mplane.performance.mplaneperformance as mplaneperformance

def mplane_app_menu():
    try:
        while True:
            choice = inquirer.select(
                            message="RU-MANAGEMENT PLANE CLIENT",
                            border=True,
                            choices=[
                                "CONNECTIONS",
                                "FAULTS",
                                "PERFORMANCE METRICS",
                                Separator(),
                                "BACK",
                                "EXIT",
                            ],
                        ).execute()
            if choice == "CONNECTIONS":
                print("CONNECTIONS Function is Not implemented")
            elif choice == "FAULTS":
                mplanefault.mplane_fault()
            elif choice == "PERFORMANCE METRICS":
                mplaneperformance.mplane_performance()
            elif choice == "BACK":
                break
            elif choice == "EXIT":
                sys.exit()
            else:
                print("Invalid option. please try again")
    except KeyboardInterrupt:
        print( "\nCtrl+C detected. Exiting the program...")
        sys.exit()
    except Exception as e:
        print( f"{e}")

