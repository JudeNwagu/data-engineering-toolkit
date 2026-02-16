"""
Data Cleaning Module
--------------------
Provides reusable functions for cleaning pandas DataFrames.
"""

import pandas as pd


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from a DataFrame.
    """
    return df.drop_duplicates()


def handle_missing_values(df: pd.DataFrame, strategy: str = "drop") -> pd.DataFrame:
    """
    Handle missing values in a DataFrame.

    Parameters:
        strategy (str): "drop" to remove rows with nulls,
                        "fill_zero" to replace nulls with 0
    """
    if strategy == "drop":
        return df.dropna()
    elif strategy == "fill_zero":
        return df.fillna(0)
    else:
        raise ValueError("Invalid strategy. Use 'drop' or 'fill_zero'.")


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert column names to lowercase and replace spaces with underscores.
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all cleaning steps in sequence.
    """
    df = standardize_column_names(df)
    df = remove_duplicates(df)
    df = handle_missing_values(df, strategy="drop")
    return df
