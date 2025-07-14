"""
Visualization utilities for the project.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Optional, Union
from pathlib import Path

def plot_distribution(
    data: Union[pd.Series, np.ndarray],
    title: str,
    xlabel: str,
    bins: int = 30,
    figsize: tuple = (10, 6),
    save_path: Optional[Union[str, Path]] = None
) -> None:
    """
    Plot the distribution of a numerical variable.
    
    Args:
        data: Input data
        title: Plot title
        xlabel: X-axis label
        bins: Number of histogram bins
        figsize: Figure size
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=figsize)
    sns.histplot(data=data, bins=bins, kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()

def plot_correlation_matrix(
    df: pd.DataFrame,
    title: str = 'Correlation Matrix',
    figsize: tuple = (12, 8),
    save_path: Optional[Union[str, Path]] = None
) -> None:
    """
    Plot a correlation matrix heatmap.
    
    Args:
        df: Input DataFrame
        title: Plot title
        figsize: Figure size
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=figsize)
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.2f',
        cmap='coolwarm',
        center=0,
        square=True
    )
    plt.title(title)
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()

def plot_time_series(
    df: pd.DataFrame,
    time_column: str,
    value_column: str,
    title: str,
    figsize: tuple = (12, 6),
    save_path: Optional[Union[str, Path]] = None
) -> None:
    """
    Plot a time series.
    
    Args:
        df: Input DataFrame
        time_column: Name of the time column
        value_column: Name of the value column
        title: Plot title
        figsize: Figure size
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=figsize)
    plt.plot(df[time_column], df[value_column])
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()

def plot_boxplots(
    df: pd.DataFrame,
    columns: List[str],
    title: str = 'Box Plots',
    figsize: tuple = (12, 6),
    save_path: Optional[Union[str, Path]] = None
) -> None:
    """
    Plot box plots for multiple columns.
    
    Args:
        df: Input DataFrame
        columns: List of columns to plot
        title: Plot title
        figsize: Figure size
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=figsize)
    df[columns].boxplot()
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()

def plot_scatter_matrix(
    df: pd.DataFrame,
    columns: List[str],
    title: str = 'Scatter Matrix',
    figsize: tuple = (12, 12),
    save_path: Optional[Union[str, Path]] = None
) -> None:
    """
    Plot a scatter matrix for multiple columns.
    
    Args:
        df: Input DataFrame
        columns: List of columns to plot
        title: Plot title
        figsize: Figure size
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=figsize)
    pd.plotting.scatter_matrix(
        df[columns],
        diagonal='kde',
        figsize=figsize
    )
    plt.suptitle(title)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show() 