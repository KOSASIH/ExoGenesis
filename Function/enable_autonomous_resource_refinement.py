import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def enable_autonomous_resource_refinement(data, labels):
    """
    Enable autonomous systems capable of refining raw extraterrestrial resources into usable materials on-site.

    Parameters:
    data (numpy array): Input data for training the model.
    labels (numpy array): Corresponding labels for the input data.

    Returns:
    autonomous_system (dict): A dictionary containing the autonomous resource refinement system.
    """

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        data, labels, test_size=0.2, random_state=42
    )

    # Initialize a list to store the performance of each refinement mechanism
    refinement_mechanism_performance = []

    # Iterate through different refinement mechanisms
    for refinement_mechanism in [
        "material_separation",
        "material_refining",
        "material_storage",
    ]:
        # Train a random forest regressor on the input data
        regressor = RandomForestRegressor(n_estimators=100, random_state=42)
        regressor.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = regressor.predict(X_test)

        # Calculate the mean squared error of the predictions
        mse = np.mean((y_pred - y_test) ** 2)

        # Store the performance of the current refinement mechanism
        refinement_mechanism_performance.append(mse)

        # Implement the autonomous resource refinement system
        autonomous_system = {"regressor": regressor, "mechanism": refinement_mechanism}

    # Determine the best refinement mechanism based on the lowest mean squared error
    best_refinement_mechanism = np.argmin(refinement_mechanism_performance)

    # Set the best refinement mechanism in the autonomous system
    autonomous_system["mechanism"] = [
        "material_separation",
        "material_refining",
        "material_storage",
    ][best_refinement_mechanism]

    return autonomous_system
