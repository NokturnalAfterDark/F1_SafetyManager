import socket
import struct
import pandas as pd

# Define the telemetry data structure
class TelemetryData:
    def __init__(self, packet_id, session_uid, lap_time, lap_distance, sector_time, lap_number,
                 engine_rpms, engine_gears, throttle, steering, speed, brake_pressure, car_damage,
                 last_lap_time, last_lap_distance, current_lap_distance, car_position):
        self.packet_id = packet_id
        self.session_uid = session_uid
        self.lap_time = lap_time
        self.lap_distance = lap_distance
        self.sector_time = sector_time
        self.lap_number = lap_number
        self.engine_rpms = engine_rpms
        self.engine_gears = engine_gears
        self.throttle = throttle
        self.steering = steering
        self.speed = speed
        self.brake_pressure = brake_pressure
        self.car_damage = car_damage
        self.last_lap_time = last_lap_time
        self.last_lap_distance = last_lap_distance
        self.current_lap_distance = current_lap_distance
        self.car_position = car_position

def listen_udp():
    UDP_IP = "127.0.0.1"  # Replace with the IP address of your F1 game instance
    UDP_PORT = 20777  # Default port for F1 2022/2023

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    print(f"Listening for telemetry data on {UDP_IP}:{UDP_PORT}")

    telemetry_data_list = []

    try:
        while True:
            data, addr = sock.recvfrom(1024)  # Adjust buffer size based on your needs
            process_telemetry_data(data, telemetry_data_list)
            # Print the telemetry data
            print(f"Received telemetry data: {data}")

            # Convert the telemetry data list to a pandas DataFrame
            telemetry_data_df = pd.DataFrame(telemetry_data_list)

            # Save the DataFrame to a CSV file
            telemetry_data_df.to_csv('telemetry_data.csv', index=False)

    except KeyboardInterrupt:
        print("UDP listener terminated by user.")

def process_telemetry_data(data, telemetry_data_list):
    # Implement the logic to parse and process the telemetry data
    # You'll need to refer to the F1 2022/2023 UDP telemetry documentation
    # to understand the data structure and extract relevant information.
    # print(f"Received telemetry data: {data.decode()}")

    # Unpack the data into a TelemetryData object
    telemetry_data = TelemetryData(*struct.unpack("<iiiiiiiiIIIIIIffffffffff", data))

    # Add the telemetry data to the list
    telemetry_data_list.append(telemetry_data)

if __name__ == "__main__":
    listen_udp()