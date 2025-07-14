"""
Feature engineering utilities for the project.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from typing import List, Union, Optional

def scale_features(
    df: pd.DataFrame,
    columns: List[str],
    scaler: Optional[StandardScaler] = None
) -> tuple[pd.DataFrame, StandardScaler]:
    """
    Scale numerical features using StandardScaler.
    
    Args:
        df: Input DataFrame
        columns: List of columns to scale
        scaler: Optional pre-fitted scaler
    
    Returns:
        tuple: (Scaled DataFrame, fitted scaler)
    """
    if scaler is None:
        scaler = StandardScaler()
        scaler.fit(df[columns])
    
    df_scaled = df.copy()
    df_scaled[columns] = scaler.transform(df[columns])
    return df_scaled, scaler

def encode_categorical(
    df: pd.DataFrame,
    columns: List[str],
    encoder: Optional[OneHotEncoder] = None,
    drop: str = 'first'
) -> tuple[pd.DataFrame, OneHotEncoder]:
    """
    One-hot encode categorical features.
    
    Args:
        df: Input DataFrame
        columns: List of columns to encode
        encoder: Optional pre-fitted encoder
        drop: Strategy for dropping categories
    
    Returns:
        tuple: (Encoded DataFrame, fitted encoder)
    """
    if encoder is None:
        encoder = OneHotEncoder(drop=drop, sparse_output=False)
        encoder.fit(df[columns])
    
    encoded = encoder.transform(df[columns])
    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out(columns),
        index=df.index
    )
    
    df_encoded = df.drop(columns=columns).join(encoded_df)
    return df_encoded, encoder

def create_time_features(
    df: pd.DataFrame,
    datetime_column: str
) -> pd.DataFrame:
    """
    Create time-based features from a datetime column.
    
    Args:
        df: Input DataFrame
        datetime_column: Name of the datetime column
    
    Returns:
        pd.DataFrame: DataFrame with added time features
    """
    df_time = df.copy()
    df_time[datetime_column] = pd.to_datetime(df_time[datetime_column])
    
    # Extract time components
    df_time[f'{datetime_column}_year'] = df_time[datetime_column].dt.year
    df_time[f'{datetime_column}_month'] = df_time[datetime_column].dt.month
    df_time[f'{datetime_column}_day'] = df_time[datetime_column].dt.day
    df_time[f'{datetime_column}_hour'] = df_time[datetime_column].dt.hour
    df_time[f'{datetime_column}_dayofweek'] = df_time[datetime_column].dt.dayofweek
    
    return df_time

def create_interaction_features(
    df: pd.DataFrame,
    columns: List[str],
    operation: str = 'multiply'
) -> pd.DataFrame:
    """
    Create interaction features between columns.
    
    Args:
        df: Input DataFrame
        columns: List of columns to create interactions from
        operation: Operation to perform ('multiply', 'add', 'subtract', 'divide')
    
    Returns:
        pd.DataFrame: DataFrame with added interaction features
    """
    df_interact = df.copy()
    
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            col1, col2 = columns[i], columns[j]
            if operation == 'multiply':
                df_interact[f'{col1}_{col2}_product'] = df[col1] * df[col2]
            elif operation == 'add':
                df_interact[f'{col1}_{col2}_sum'] = df[col1] + df[col2]
            elif operation == 'subtract':
                df_interact[f'{col1}_{col2}_diff'] = df[col1] - df[col2]
            elif operation == 'divide':
                df_interact[f'{col1}_{col2}_ratio'] = df[col1] / df[col2]
    
    return df_interact 