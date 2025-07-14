"""
Model training and evaluation utilities for the project.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_squared_error,
    r2_score
)
from typing import Any, Dict, List, Optional, Tuple, Union
import mlflow
import mlflow.sklearn
from pathlib import Path

def train_test_split_data(
    X: pd.DataFrame,
    y: Union[pd.Series, np.ndarray],
    test_size: float = 0.2,
    random_state: int = 42
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Split data into training and testing sets.
    
    Args:
        X: Features
        y: Target variable
        test_size: Proportion of data to use for testing
        random_state: Random seed for reproducibility
    
    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    return train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state
    )

def evaluate_classification(
    y_true: Union[pd.Series, np.ndarray],
    y_pred: Union[pd.Series, np.ndarray],
    average: str = 'weighted'
) -> Dict[str, float]:
    """
    Evaluate classification model performance.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        average: Averaging strategy for multi-class metrics
    
    Returns:
        dict: Dictionary of metric names and values
    """
    return {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average=average),
        'recall': recall_score(y_true, y_pred, average=average),
        'f1': f1_score(y_true, y_pred, average=average)
    }

def evaluate_regression(
    y_true: Union[pd.Series, np.ndarray],
    y_pred: Union[pd.Series, np.ndarray]
) -> Dict[str, float]:
    """
    Evaluate regression model performance.
    
    Args:
        y_true: True values
        y_pred: Predicted values
    
    Returns:
        dict: Dictionary of metric names and values
    """
    return {
        'mse': mean_squared_error(y_true, y_pred),
        'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
        'r2': r2_score(y_true, y_pred)
    }

def cross_validate_model(
    model: Any,
    X: pd.DataFrame,
    y: Union[pd.Series, np.ndarray],
    cv: int = 5,
    scoring: str = 'accuracy'
) -> Dict[str, float]:
    """
    Perform cross-validation on a model.
    
    Args:
        model: Model to evaluate
        X: Features
        y: Target variable
        cv: Number of cross-validation folds
        scoring: Scoring metric
    
    Returns:
        dict: Dictionary of cross-validation results
    """
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
    return {
        'mean_score': scores.mean(),
        'std_score': scores.std(),
        'scores': scores
    }

def log_mlflow_experiment(
    model: Any,
    params: Dict[str, Any],
    metrics: Dict[str, float],
    experiment_name: str,
    run_name: Optional[str] = None,
    model_name: Optional[str] = None
) -> None:
    """
    Log model training results to MLflow.
    
    Args:
        model: Trained model
        params: Model parameters
        metrics: Evaluation metrics
        experiment_name: Name of the MLflow experiment
        run_name: Optional name for this run
        model_name: Optional name for the model
    """
    mlflow.set_experiment(experiment_name)
    
    with mlflow.start_run(run_name=run_name):
        # Log parameters
        mlflow.log_params(params)
        
        # Log metrics
        mlflow.log_metrics(metrics)
        
        # Log model
        if model_name:
            mlflow.sklearn.log_model(model, model_name)
        else:
            mlflow.sklearn.log_model(model, "model")

def save_model(
    model: Any,
    filepath: Union[str, Path],
    format: str = 'joblib'
) -> None:
    """
    Save a trained model to disk.
    
    Args:
        model: Trained model
        filepath: Path to save the model
        format: Format to save the model in ('joblib' or 'pickle')
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    if format == 'joblib':
        import joblib
        joblib.dump(model, filepath)
    elif format == 'pickle':
        import pickle
        with open(filepath, 'wb') as f:
            pickle.dump(model, f)
    else:
        raise ValueError(f"Unsupported format: {format}")

def load_model(
    filepath: Union[str, Path],
    format: str = 'joblib'
) -> Any:
    """
    Load a trained model from disk.
    
    Args:
        filepath: Path to the saved model
        format: Format the model was saved in ('joblib' or 'pickle')
    
    Returns:
        The loaded model
    """
    filepath = Path(filepath)
    
    if format == 'joblib':
        import joblib
        return joblib.load(filepath)
    elif format == 'pickle':
        import pickle
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    else:
        raise ValueError(f"Unsupported format: {format}") 