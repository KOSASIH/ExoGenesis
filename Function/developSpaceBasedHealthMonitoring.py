import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def developSpaceBasedHealthMonitoring(data, labels):
    """
    Develop systems for monitoring the health and performance of astronauts and spacecraft in real-time.
    
    Parameters:
    data (DataFrame): A pandas DataFrame containing the features for monitoring.
    labels (Series): A pandas Series containing the labels for the features.
    
    Returns:
    model (RandomForestClassifier): A trained Random Forest Classifier model for predicting the health and performance of astronauts and spacecraft.
    """
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    # Create a Random Forest Classifier model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model on the training data
    model.fit(X_train, y_train)
    
    # Make predictions on the testing data
    y_pred = model.predict(X_test)
    
    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    
    # Print the accuracy of the model
    print(f"Accuracy of the model: {accuracy}")
    
    # Return the trained model
    return model
