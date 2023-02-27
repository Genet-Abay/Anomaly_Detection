"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.4
"""
import pandas as pd
from datetime import timedelta, datetime as dt
from sklearn.model_selection import train_test_split

def my_train_test_split(processed_df: pd.DataFrame) -> pd.DataFrame:
    X = processed_df.drop(['Class'], axis=1)
    Y = processed_df['Class']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
    return X_train, X_test, Y_test


