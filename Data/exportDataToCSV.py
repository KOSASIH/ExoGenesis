from azure.devops.connection import Connection
from azure.devops.v5_1.work_item_tracking.models import Wiql
from msrest.authentication import BasicAuthentication

def exportDataToCSV(organization_url, personal_access_token, project_name, query_id):
    # Create a connection to the Azure DevOps organization
    credentials = BasicAuthentication('', personal_access_token)
    connection = Connection(base_url=organization_url, creds=credentials)

    # Get a client to interact with the work item tracking service
    work_item_client = connection.clients.get_work_item_tracking_client()

    # Define the query to retrieve the desired work items
    wiql = Wiql(query=f"SELECT * FROM WorkItems WHERE [System.TeamProject] = '{project_name}' AND [System.Id] IN (SELECT [Id] FROM WorkItemLinks WHERE [Source].[System.Id] IN ({query_id}))")

    # Run the query and get the results
    query_results = work_item_client.query_by_wiql(wiql).work_items

    # Create a CSV file to store the exported data
    with open('exported_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Id', 'Title', 'State', 'Assigned To', 'Tags']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for work_item in query_results:
            row = {
                'Id': work_item.id,
                'Title': work_item.fields['System.Title'],
                'State': work_item.fields['System.State'],
                'Assigned To': work_item.fields['System.AssignedTo'].display_name,
                'Tags': ', '.join([tag.name for tag in work_item.fields['System.Tags']])
            }
            writer.writerow(row)
