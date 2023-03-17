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

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


def show_messages():
    while True:
        # msg = master.recv_match(type='LOCAL_POSITION_NED', blocking=True)
        msg = master.recv_match()
        print(msg)

def setup():
    global master

    print("\n-----------------------")
    print("Welcome to the drone control center!")
    print("-----------------------")

    master = create_connection()

class Command(BaseModel):
    type: int

@app.post("/command/")
async def read_root(command: Command):

    # global master

    # master = create_connection()

    option = command.type
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
        show_messages()
    elif option == 6:
        # go_to_location()
        print("Option not working yet! :(")
    elif option == 7:
        waypoint_mission(master)
    elif option == 8:
        set_return(master)
    else:
        print("Option not implemented yet!")
    
if __name__ == "__main__":

    setup()

    uvicorn.run("Drone_Control_Server:app", host="0.0.0.0", port=8000, log_level="info")


