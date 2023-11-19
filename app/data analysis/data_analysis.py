import pandas as pd
import matplotlib.pyplot as plt

def analyze_gaze_distribution(telemetry_data, gaze_data):
    # Calculate gaze dwell time in each zone of interest (ZoI)
    zois = ["apex", "braking_zone", "side_mirrors"]  # Define ZoIs

    dwell_times = {}
    for zone in zois:
        zone_dwell_time = 0
        for gaze_entry in gaze_data:
            if gaze_entry['x_gaze'] > 0.7 and gaze_entry['y_gaze'] < 0.3:
                zone_dwell_time += gaze_entry['gaze_duration']

        dwell_times[zone] = zone_dwell_time

    # Calculate proportion of gaze time in each ZoI
    total_gaze_time = sum(gaze_entry['gaze_duration'] for gaze_entry in gaze_data)
    gaze_proportions = {}
    for zone, dwell_time in dwell_times.items():
        gaze_proportions[zone] = dwell_time / total_gaze_time

    # Correlate gaze proportions with driving performance metrics
    lap_times = telemetry_data['lap_time']
    correlation_coefficients = {}
    for zone, gaze_proportion in gaze_proportions.items():
        correlation_coefficients[zone] = np.corrcoef(gaze_proportion, lap_times)[0, 1]

    return gaze_proportions, correlation_coefficients

def visualize_gaze_distribution(gaze_proportions):
    # Create a pie chart representing the proportion of gaze time in each ZoI
    zone_labels = gaze_proportions.keys()
    zone_values = gaze_proportions.values()

    plt.pie(zone_values, labels=zone_labels, autopct="%1.1f%%")
    plt.title("Distribution of Gaze Time")
    plt.show()

def main():
    # Load telemetry and gaze data
    telemetry_data = pd.read_csv('telemetry_data.csv')
    gaze_data = pd.read_csv('gaze_data.csv')

    # Analyze gaze distribution
    gaze_proportions, correlation_coefficients = analyze_gaze_distribution(telemetry_data, gaze_data)

    # Visualize gaze distribution
    visualize_gaze_distribution(gaze_proportions)

if __name__ == "__main__":
    main()
