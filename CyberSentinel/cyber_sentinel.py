import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def cyber_sentinel(data, labels):
    """
    Function to train and evaluate CyberSentinel, an AI-powered cybersecurity tool.
    
    Parameters:
    data (numpy array): Input data for training and evaluation.
    labels (numpy array): Corresponding labels for the input data.
    
    Returns:
    float: Accuracy score of the trained CyberSentinel model.
    """
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    # Initialize the Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the classifier on the training data
    clf.fit(X_train, y_train)
    
    # Make predictions on the testing data
    y_pred = clf.predict(X_test)
    
    # Calculate the accuracy score of the trained model
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy
