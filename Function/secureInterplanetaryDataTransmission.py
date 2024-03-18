import hashlib
import hmac


def secureInterplanetaryDataTransmission(data, secret_key):
    """
    Secures interplanetary data transmission by implementing security measures to protect data transmitted between different celestial bodies.

    Parameters:
    data (str): The data to be transmitted.
    secret_key (str): The secret key used for encryption and authentication.

    Returns:
    secure_data (tuple): A tuple containing the secure data and its corresponding authentication code.
    """

    # Encrypt the data using a hash-based message authentication code (HMAC)
    hash_object = hashlib.sha256(data.encode())
    hmac_object = hmac.new(secret_key.encode(), hash_object.digest(), hashlib.sha256)
    secure_data = (data, hmac_object.hexdigest())

    return secure_data
