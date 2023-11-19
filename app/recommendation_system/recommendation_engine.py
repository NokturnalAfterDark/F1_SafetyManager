import pandas as pd

def generate_recommendation(telemetry_data, gaze_data):
    # Analyze telemetry_data and gaze_data to generate a recommendation string
    # Example:

    # Check for braking and gaze position
    if telemetry_data.brake_pressure > 0.8 and gaze_data['y_gaze'] < 0.2:
        recommendation = "Brake earlier and look ahead for the corner!"

    # Check for acceleration, speed, and gaze position
    elif telemetry_data.speed < 100 and telemetry_data.steering > 0.5 and gaze_data['x_gaze'] > 0.8:
        recommendation = "Accelerate through the corner while maintaining racing line!"

    # Check for speed and gaze position
    elif telemetry_data.speed > 150 and gaze_data['x_gaze'] < 0.2:
        recommendation = "Look ahead for upcoming braking zones!"

    # Check for steering and gaze position
    elif telemetry_data.steering > 0.5 and gaze_data['x_gaze'] < 0.2:
        recommendation = "Adjust your steering angle to maintain racing line!"

    # Check for gaze position and track apex
    elif gaze_data['x_gaze'] > 0.7 and gaze_data['y_gaze'] < 0.3:
        recommendation = "Aim for the apex of the corner!"

    else:
        # Existing recommendation logic
        recommendation = "Keep up the good driving and monitor track conditions!"

    # Append additional recommendations based on gaze-based metrics
    if telemetry_data.brake_pressure > 0.8 and gaze_data['y_gaze'] < 0.2 and gaze_data['dwell_time'] > 0.5:
        recommendation += "\nProlonged gaze on braking zone. Consider braking earlier and maintaining focus."

    if telemetry_data.speed < 100 and telemetry_data.steering > 0.5 and gaze_data['x_gaze'] > 0.8 and gaze_data['transition_frequency'] < 0.5:
        recommendation += "\nFocused gaze on track ahead while accelerating. Maintain attention and avoid distractions."

    if telemetry_data.speed > 150 and gaze_data['x_gaze'] < 0.2 and gaze_data['anticipation_time'] > 0.5:
        recommendation += "\nAnticipatory gaze for upcoming braking zones. Maintain focus and adjust speed accordingly."

    if telemetry_data.steering > 0.5 and gaze_data['x_gaze'] < 0.2 and gaze_data['gaze_steering_correlation'] > 0.8:
        recommendation += "\nSynchronized gaze and steering. Maintain focus on the apex of the corner."

    if gaze_data['consistency_score'] < 0.5 and gaze_data['pupil_size'] > 4:
        recommendation += "\nInconsistent gaze pattern and elevated pupil size. Minimize distractions and focus on essential cues."

    return recommendation