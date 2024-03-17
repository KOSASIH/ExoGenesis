import requests
import json

def processPullRequest(pull_request_url, access_token):
    """
    Processes a pull request from a contributor, reviewing changes and merging them into the main codebase.

    :param pull_request_url: The URL of the pull request to process.
    :param access_token: The access token for the repository.
    """

    # Get the pull request details
    headers = {"Authorization": f"token {access_token}"}
    response = requests.get(pull_request_url, headers=headers)
    pull_request_data = response.json()

    # Check if the pull request is mergeable
    if pull_request_data["mergeable"]:
        # Merge the pull request into the main codebase
        merge_url = pull_request_data["url"] + "/merge"
        merge_data = {"commit_title": "Merge pull request", "merge_method": "merge"}
        merge_response = requests.put(merge_url, headers=headers, data=json.dumps(merge_data))

        if merge_response.status_code == 200:
            print("Pull request merged successfully.")
        else:
            print("Failed to merge pull request. Error:", merge_response.text)
    else:
        print("Pull request is not mergeable. Please resolve conflicts and try again.")
