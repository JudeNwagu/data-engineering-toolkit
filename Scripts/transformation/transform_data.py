"""
Data Transformation Module
---------------------------
Provides reusable transformation functions for pandas DataFrames.
"""

import pandas as pd


def rename_columns(df: pd.DataFrame, column_mapping: dict) -> pd.DataFrame:
    """
    Rename columns using a dictionary mapping.
    """
    return df.rename(columns=column_mapping)


def filter_rows(df: pd.DataFrame, column_name: str, threshold: float) -> pd.DataFrame:
    """
    Filter rows where column value is greater than a threshold.
    """
    return df[df[column_name] > threshold]


def create_derived_column(df: pd.DataFrame, new_column: str, col1: str, col2: str) -> pd.DataFrame:
    """
    Create a new column by adding two existing columns.
    """
    df[new_column] = df[col1] + df[col2]
    return df


def aggregate_data(df: pd.DataFrame, group_by_column: str, agg_column: str) -> pd.DataFrame:
    """
    Group data and calculate sum of a column.
    """
    return df.groupby(group_by_column)[agg_column].sum().reset_index()
