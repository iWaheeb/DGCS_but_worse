from functions_abstract import send_command, recieve_message

def recieve_heartbeat(conn):
    conn.wait_heartbeat()
    print(f"Heartbeat from system (system {conn.target_system} component {conn.target_component})")

def arm(conn):
    command = 400
    params = [0] * 7

    params[0] = 1
    send_command(conn, command, params)

def disarm(conn):
    command = 400
    params = [0] * 7

    params[0] = 0
    send_command(conn, command, params)

def mav_command_result(conn):
    mav_results = {0:"MAV_RESULT_ACCEPTED", 1:"MAV_RESULT_TEMPORARILY_REJECTED", 2:"MAV_RESULT_DENIED", 
            3:"MAV_RESULT_UNSUPPORTED", 4:"MAV_RESULT_FAILED", 5:"MAV_RESULT_IN_PROGRESS", 
            6:"MAV_RESULT_CANCELLED", 7:"MAV_RESULT_COMMAND_LONG_ONLY", 8:"MAV_RESULT_COMMAND_INT_ONLY", 
            9:"MAV_RESULT_COMMAND_UNSUPPORTED_MAV_FRAME"}
    
    value = recieve_message(conn, "COMMAND_ACK").result
    return mav_results[value]

#TODO: add System Information
