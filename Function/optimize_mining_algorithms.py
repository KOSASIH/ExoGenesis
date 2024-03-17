import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

def optimize_mining_algorithms(X, y, algorithm=RandomForestRegressor(), param_grid=None):
    """
    Function to optimize mining algorithms using GridSearchCV.
    
    Parameters:
    X (array-like): Input data, shape (n_samples, n_features)
    y (array-like): Target data, shape (n_samples,)
    algorithm (object): Algorithm to optimize, default is RandomForestRegressor
    param_grid (dict): Dictionary with parameters names as keys and list of parameter settings as values
    
    Returns:
    best_algorithm (object): Best algorithm after optimization
    """
    
    # Check if param_grid is provided
    if param_grid is None:
        raise ValueError("Parameter grid is required for optimization")
    
    # Initialize GridSearchCV
    grid_search = GridSearchCV(estimator=algorithm, param_grid=param_grid, cv=5, n_jobs=-1)
    
    # Fit GridSearchCV to data
    grid_search.fit(X, y)
    
    # Get the best algorithm after optimization
    best_algorithm = grid_search.best_estimator_
    
    return best_algorithm
