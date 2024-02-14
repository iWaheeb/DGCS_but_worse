from connection import connect
from command import *

from pymavlink import mavutil

conn = connect()
recieve_heartbeat(conn)
arm(conn)
# disarm(conn)
print(mav_command_result(conn))
