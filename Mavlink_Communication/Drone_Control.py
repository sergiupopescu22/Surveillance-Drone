from pymavlink import mavutil
import time

from Flight_Commands.MakeConnection import *
from Flight_Commands.Arm import *
from Flight_Commands.Disarm import *
from Flight_Commands.Taskeoff import *
from Flight_Commands.Land import *
from Flight_Commands.SetPosition import *
from Flight_Commands.WayPointMission import *
from Flight_Commands.ACK import *

import Flight_Commands.global_variables as GVar


def show_messages(the_connection):
    while True:
        # msg = the_connection.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
        msg = the_connection.recv_match()
        if msg is not None:
            print("")
            print(msg)
        # print(msg.relative_alt)
        # time.sleep(1)
        

def main():

    print("\n-----------------------")
    print("Welcome to the drone control center!")
    print("-----------------------")
    GVar.action_type = "real-life-rb"
    master = create_connection()
    
    
    while True:

        print("\n-----------------------")
        print("Pick an option:")
        print("--- 1. Arm the drone")
        print("--- 2. Disarm the drone")
        print("--- 3. Takeoff")
        print("--- 4. Land")
        print("--- 5. Show received messages")
        print("--- 6. Go to Specified Location")
        print("--- 7. Create Mission")
        print("--- 8. Return")
        print("--- 9. Exit program")

        print("\n-----------------------")
        option = int(input ("Select an option: "))
        print("selected option: ", option)

        if option == 1:
            arm_drone(master)
        elif option == 2:
            disarm_drone(master)
        elif option == 3:
            takeoff(master)
        elif option == 4:
            land(master)
        elif option == 5:
            show_messages(master)
        elif option == 6:
            # go_to_location()
            print("Option not working yet! :(")
        elif option == 7:
            waypoint_mission(master)
        elif option == 8:
            # set_return(master)
            pass
        elif option == 9:
            break
        else:
            print("Option not implemented yet!")
    
if __name__ == "__main__":
    main()


