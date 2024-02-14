from pymavlink import mavutil


def send_command(conn, command, params):
    conn.mav.command_long_send(conn.target_system, conn.target_component, command, 0, *params)
    
def recieve_message(conn, msg_name):
    return conn.recv_match(type=msg_name, blocking=True)
