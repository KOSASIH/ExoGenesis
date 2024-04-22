import requests


class AstroMesh:
    def __init__(self, network="testnet"):
        self.network = network
        self.base_url = f"https://horizon-{self.network}.stellar.org"

    def get_account_info(self, account_id):
        url = f"{self.base_url}/accounts/{account_id}"
        response = requests.get(url)
        return response.json()

    def get_payment_history(self, account_id, limit=20):
        url = f"{self.base_url}/accounts/{account_id}/payments?limit={limit}"
        response = requests.get(url)
        return response.json()

    def submit_transaction(self, transaction):
        url = f"{self.base_url}/transactions"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=transaction, headers=headers)
        return response.json()


# Example usage
astro_mesh = AstroMesh()
account_info = astro_mesh.get_account_info(
    "GABC7KQ2W526B7562J23YV762BX53TQZ3T3S6K3K4XB52XM7"
)
payment_history = astro_mesh.get_payment_history(
    "GABC7KQ2W526B7562J23YV762BX53TQZ3T3S6K3K4XB52XM7"
)
transaction = {...}  # create a transaction object
submitted_transaction = astro_mesh.submit_transaction(transaction)
