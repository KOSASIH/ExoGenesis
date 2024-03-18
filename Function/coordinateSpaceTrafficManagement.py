import numpy as np
from scipy.spatial import KDTree

def coordinateSpaceTrafficManagement(satellite_positions, satellite_velocities, satellite_radii, maneuver_duration, max_speed, max_acceleration):
    """
    Coordinates the traffic management of spacecraft and satellites in orbit.
    
    Parameters:
    satellite_positions (list of 3D vectors): Positions of satellites in meters.
    satellite_velocities (list of 3D vectors): Velocities of satellites in meters per second.
    satellite_radii (list of floats): Radii of satellites in meters.
    maneuver_duration (float): Duration of maneuver in seconds.
    max_speed (float): Maximum speed of satellites in meters per second.
    max_acceleration (float): Maximum acceleration of satellites in meters per second squared.
    
    Returns:
    maneuver_plans (list of 3D vectors): Maneuver plans for each satellite.
    """
    
    # Create KDTree for efficient nearest neighbor search
    tree = KDTree(satellite_positions)
    
    # Initialize maneuver plans for each satellite
    maneuver_plans = [np.zeros(3) for _ in range(len(satellite_positions))]
    
    # Iterate over each satellite
    for i, (position, velocity, radius) in enumerate(zip(satellite_positions, satellite_velocities, satellite_radii)):
        
        # Find nearest neighbors within a safety distance
        safety_distance = 2 * max_speed * maneuver_duration + 2 * max_acceleration * maneuver_duration ** 2
        neighbors = tree.query_ball_point(position, safety_distance)
        
        # Calculate relative positions and velocities of neighbors
        relative_positions = [satellite_positions[j] - position for j in neighbors]
        relative_velocities = [satellite_velocities[j] - velocity for j in neighbors]
        
        # Calculate the closest approach distance for each neighbor
        closest_approach_distances = [np.linalg.norm(relative_position - np.dot(relative_velocity, maneuver_duration) / np.linalg.norm(relative_velocity) * relative_velocity) for relative_position, relative_velocity in zip(relative_positions, relative_velocities)]
        
        # Find the closest neighbor
        closest_neighbor_index = np.argmin(closest_approach_distances)
        closest_neighbor = neighbors[closest_neighbor_index]
        
        # Calculate the relative position and velocity of the closest neighbor
        relative_position = relative_positions[closest_neighbor_index]
        relative_velocity = relative_velocities[closest_neighbor_index]
        
        # Calculate the time to closest approach
        ttc = np.linalg.norm(relative_position) / np.linalg.norm(relative_velocity)
        
        # Calculate the relative position and velocity at closest approach
        relative_position_ca = relative_position - np.dot(relative_velocity, ttc) / np.linalg.norm(relative_velocity) * relative_velocity
        relative_velocity_ca = relative_velocity - np.dot(relative_velocity, ttc) / np.linalg.norm(relative_velocity) * np.linalg.norm(relative_velocity) * relative_position / np.linalg.norm(relative_position)
        
        # Calculate the minimum safe distance
        min_safe_distance = radius + satellite_radii[closest_neighbor] + safety_distance
        
        # Check if the closest approach distance is less than the minimum safe distance
        if np.linalg.norm(relative_position_ca) < min_safe_distance:
            
            # Calculate the required maneuver to avoid collision
            maneuver = np.cross(relative_velocity_ca, relative_position_ca) / np.linalg.norm(relative_position_ca) ** 2
            maneuver_plans[i] = maneuver * min_safe_distance / np.linalg.norm(maneuver)
            
    # Optimize maneuver plans for efficiency
    for i, item in enumerate(satellite_positions):
        
        # Calculate the new velocity after applying the maneuver plan
        new_velocity = satellite_velocities[i] + maneuver_plans[i]
        
        # Calculate the new position after applying the maneuver plan
        new_position = item + new_velocity * maneuver_duration
        
        # Calculate the new velocity after applying the maneuver plan
        new_velocity = new_velocity + np.sign(new_velocity) * max_acceleration * maneuver_duration
        
        # Calculate the new position after applying the maneuver plan
        new_position = new_position + new_velocity * maneuver_duration
        
        # Calculate the new maneuver plan
        maneuver_plans[i] = new_velocity - satellite_velocities[i]
        
    return maneuver_plans
