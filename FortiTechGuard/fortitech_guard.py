import json

import requests


def fortitech_guard(exo_genesis_system, threat_data):
    """
    Utilizes advanced AI systems to fortify ExoGenesis systems against cyber threats and vulnerabilities.

    Parameters:
    exo_genesis_system (dict): A dictionary representing the ExoGenesis system to be protected.
    threat_data (dict): A dictionary containing threat data and potential vulnerabilities.

    Returns:
    str: A message indicating the status of the protection process.
    """

    # Define the API endpoint for FortiTechGuard
    api_endpoint = "https://api.fortitechguard.com/v1/protect"

    # Prepare the payload for the API request
    payload = {"exo_genesis_system": exo_genesis_system, "threat_data": threat_data}

    # Send the API request to FortiTechGuard
    response = requests.post(api_endpoint, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        response_json = json.loads(response.text)

        # Return the protection status message
        return response_json["message"]
    # Return an error message if the request was not successful
    return f"Error: {response.status_code} - {response.text}"
