"""
Data Loading Module
--------------------
Provides reusable functions for saving pandas DataFrames to files.
"""

import pandas as pd


def save_to_csv(df: pd.DataFrame, file_path: str) -> None:
    """
    Save DataFrame to a CSV file.
    """
    df.to_csv(file_path, index=False)


def save_to_excel(df: pd.DataFrame, file_path: str) -> None:
    """
    Save DataFrame to an Excel file.
    """
    df.to_excel(file_path, index=False)


def save_to_json(df: pd.DataFrame, file_path: str) -> None:
    """
    Save DataFrame to a JSON file.
    """
    df.to_json(file_path, orient="records", indent=4)


def save_data(df: pd.DataFrame, file_path: str, file_type: str) -> None:
    """
    Save data based on file type.
    
    Parameters:
        file_type (str): 'csv', 'excel', or 'json'
    """
    if file_type == "csv":
        save_to_csv(df, file_path)
    elif file_type == "excel":
        save_to_excel(df, file_path)
    elif file_type == "json":
        save_to_json(df, file_path)
    else:
        raise ValueError("Invalid file type. Use 'csv', 'excel', or 'json'.")
