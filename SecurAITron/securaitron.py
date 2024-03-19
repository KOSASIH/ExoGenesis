from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def securaitron(data, labels):
    """
    Utilizes advanced AI technology to ensure unparalleled security for ExoGenesis systems.

    Parameters:
    data (np.array): Input data for training the AI model.
    labels (np.array): Corresponding labels for the input data.

    Returns:
    model (RandomForestClassifier): Trained AI model for predicting security threats.
    """

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        data, labels, test_size=0.2, random_state=42
    )

    # Initialize the AI model
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the AI model on the training data
    model.fit(X_train, y_train)

    # Evaluate the AI model's performance on the testing data
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Accuracy of SecurAItron: {accuracy}")

    return model
