from pymavlink import mavutil


def connect():
    conn = mavutil.mavlink_connection('127.0.0.1:14559')

    
    return conn

# Receiving messages from the drone
# while True:
#     attitude_msg = the_connection.recv_match(type='GPS_RAW_INT', blocking=True)
#     print(attitude_msg.v_acc)
