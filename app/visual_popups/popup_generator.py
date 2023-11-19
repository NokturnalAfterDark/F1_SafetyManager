import tkinter as tk
import socket
import struct
import pandas
from app.telemetry.udp_listener import TelemetryData
from app.visual_popups.popup_generator import generate_recommendation, generate_visual_popup
from app.recommendation_system.recommendation_engine import generate_recommendation
from app.gaze_tracking.gaze_analyzer import analyze_gaze

def show_popup(recommendation):
    # Create a visual popup with the recommendation text
    root = tk.Tk()
    root.title("F1 23 Telemetry Recommendation")
    label = tk.Label(root, text=recommendation, font=("Arial", 16))
    label.pack(pady=10)
    root.geometry("300x50")
    root.mainloop()


def generate_visual_popup(recommendation):
    # Implement logic to generate visual popups during racing
    # For example, print the visual popup message
    print(f"Visual Popup: {recommendation}")


def listen_udp_and_show_popup():
    UDP_IP = "127.0.0.1"  # Replace with the IP address of your F1 game instance
    UDP_PORT = 20777  # Default port for F1 2022/2023

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        telemetry_data = TelemetryData(*struct.unpack("<iiiiiiiiIIIIIIffffffffff", data))

        # Read gaze data from gaze analyzer
        gaze_data = analyze_gaze('gaze_tracking_data.csv')

        # Merge telemetry and gaze data
        merged_data = {
            'telemetry_data': telemetry_data,
            'gaze_data': gaze_data
        }

        # Generate recommendation based on merged data
        recommendation = generate_recommendation(merged_data['telemetry_data'], merged_data['gaze_data'])
        show_popup(recommendation)
        generate_visual_popup(recommendation)

if __name__ == "__main__":
    listen_udp_and_show_popup()