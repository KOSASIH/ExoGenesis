import numpy as np
from scipy.spatial import KDTree

def developAdaptiveRoutingAlgorithms(satellite_positions, target_positions, obstacle_positions=None):
    """
    Develop adaptive routing algorithms for satellites and spacecraft in complex space environments.
    
    Parameters:
    satellite_positions (list of tuples): List of tuples representing the positions of satellites in space.
    target_positions (list of tuples): List of tuples representing the target positions for the satellites.
    obstacle_positions (list of tuples, optional): List of tuples representing the positions of obstacles in space. Default is None.
    
    Returns:
    list of tuples: List of tuples representing the optimal trajectories for each satellite to reach its target position.
    """
    
    # Convert positions to numpy arrays for easier manipulation
    satellite_positions = np.array(satellite_positions)
    target_positions = np.array(target_positions)
    
    # Create KDTree for efficient nearest neighbor search
    tree = KDTree(satellite_positions)
    
    # Initialize list to store optimal trajectories
    optimal_trajectories = []
    
    # Iterate over each satellite and its target position
    for satellite_position, target_position in zip(satellite_positions, target_positions):
        
        # Find the nearest neighbor of the current satellite
        _, nearest_neighbor_index = tree.query(satellite_position)
        
        # Initialize the current trajectory with the nearest neighbor
        current_trajectory = [satellite_position, satellite_positions[nearest_neighbor_index]]
        
        # Iterate until the target position is reached
        while np.linalg.norm(current_trajectory[-1] - target_position) > 1e-6:
            
            # Find the nearest neighbor of the current trajectory endpoint
            _, nearest_neighbor_index = tree.query(current_trajectory[-1])
            
            # Calculate the direction vector from the current trajectory endpoint to the nearest neighbor
            direction_vector = satellite_positions[nearest_neighbor_index] - current_trajectory[-1]
            
            # Calculate the next point on the trajectory as a step in the direction vector
            next_point = current_trajectory[-1] + 0.1 * direction_vector
            
            # Check for obstacles and avoid them if necessary
            if obstacle_positions is not None:
                obstacle_distances = np.linalg.norm(np.array(obstacle_positions) - next_point, axis=1)
                if np.min(obstacle_distances) < 1e-6:
                    # Find the closest obstacle and calculate the avoidance vector
                    closest_obstacle_index = np.argmin(obstacle_distances)
                    avoidance_vector = np.array(obstacle_positions[closest_obstacle_index]) - next_point
                    avoidance_vector /= np.linalg.norm(avoidance_vector)
                    next_point += 0.1 * avoidance_vector
                
            # Append the next point to the trajectory
            current_trajectory.append(next_point)
            
        # Append the optimal trajectory to the list
        optimal_trajectories.append(current_trajectory)
    
    return optimal_trajectories
