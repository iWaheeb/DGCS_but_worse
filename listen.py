from pymavlink import mavutil

# Start a connection listening on a UDP port
the_connection = mavutil.mavlink_connection('127.0.0.1:14559')

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print(f"Heartbeat from system (system {the_connection.target_system} component {the_connection.target_component})")
