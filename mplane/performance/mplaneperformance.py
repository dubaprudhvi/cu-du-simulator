from utils.imports import *

import mplane.performance.mplaneperformanceinterval as mplaneperformanceinterval
import mplane.performance.mplaneperformancelimit as mplaneperformancelimit

def mplane_performance():
    try:
        while True:
            choice = inquirer.select(
                            message="MPLANE PERFORMANCE METRICS",
                            border=True,
                            choices=[
                                "BASED ON INTERVAL",
                                "BASED ON LIMIT",
                                Separator(),
                                "BACK",
                                "EXIT",
                            ],
                        ).execute()
            if choice == "BASED ON INTERVAL":
                mplaneperformanceinterval.mplane_performance_interval()
            elif choice == "BASED ON LIMIT":
                mplaneperformancelimit.mplane_performance_limit()
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
      