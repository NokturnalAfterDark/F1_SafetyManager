import pandas as pd
import gym
import numpy as np
from qlearning_agent import QLearningAgent

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


def generate_recommendation(telemetry_data, gaze_data):
    # Convert telemetry and gaze data into a state representation suitable for the Q-learning model
    state = convert_data_to_state(telemetry_data, gaze_data)

    # Predict the optimal action using the Q-learning model
    action = QLearningAgent.act(state)

    # Convert the predicted action into a recommendation
    recommendation = convert_action_to_recommendation(action)

    return recommendation


def convert_data_to_state(telemetry_data, gaze_data):
    # Extract relevant features from telemetry and gaze data
    # For example, extract speed, steering angle, gaze position, etc.

    speed = telemetry_data.speed
    steering_angle = telemetry_data.steering
    x_gaze = gaze_data['x_gaze']
    y_gaze = gaze_data['y_gaze']

    # Format the extracted features into a state representation suitable for the Q-learning model
    # This may involve normalization, scaling, or encoding of features

    state = [speed, steering_angle, x_gaze, y_gaze]
    return state


def convert_action_to_recommendation(action):
    # Map the predicted action to a corresponding recommendation string
    # For instance, action 0 could correspond to "Brake earlier", action 1 could correspond to "Accelerate through the corner", etc.

    recommendation = ""
    if action == 0:
        recommendation = "Brake earlier and focus on the braking zone!"
    elif action == 1:
        recommendation = "Accelerate through the corner while maintaining racing line!"
    elif action == 2:
        recommendation = "Look ahead for upcoming braking zones!"
    elif action == 3:
        recommendation = "Adjust your steering angle to maintain racing line!"
    else:
        recommendation = "Keep up the good driving and monitor track conditions!"

    return recommendation