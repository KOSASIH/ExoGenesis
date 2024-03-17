import os
from opestom_functions import custom_functions

def build_satellite_infrastructure(satellite_designs, deployment_locations):
    """
    This function designs and deploys satellite-based infrastructure for various purposes.
    
    Parameters:
    satellite_designs (list): List of satellite designs to be deployed.
    deployment_locations (list): List of deployment locations for the satellite infrastructure.
    
    Returns:
    dict: A dictionary containing the deployed satellite infrastructure and their locations.
    """
    
    deployed_infrastructure = {}
    
    for design in satellite_designs:
        for location in deployment_locations:
            infrastructure = design(location)
            
            if location in deployed_infrastructure:
                deployed_infrastructure[location].append(infrastructure)
            else:
                deployed_infrastructure[location] = [infrastructure]
    
    return deployed_infrastructure
