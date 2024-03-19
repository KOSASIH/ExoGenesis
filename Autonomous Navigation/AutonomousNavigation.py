import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class AutonomousNavigation:
    def __init__(self, sensor_data, target_coordinates):
        self.sensor_data = sensor_data
        self.target_coordinates = target_coordinates
        self.model = RandomForestRegressor()

    def train_model(self):
        X = self.sensor_data
        y = self.target_coordinates
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def navigate(self, current_coordinates):
        X = np.array([current_coordinates]).reshape(1, -1)
        predicted_coordinates = self.model.predict(X)
        return predicted_coordinates[0]

# Example usage
sensor_data = [...]  # Sensor data for navigation
target_coordinates = [...]  # Target coordinates for navigation

navigation_system = AutonomousNavigation(sensor_data, target_coordinates)
navigation_system.train_model()

current_coordinates = [...]  # Current coordinates of the spacecraft or rover
predicted_coordinates = navigation_system.navigate(current_coordinates)
