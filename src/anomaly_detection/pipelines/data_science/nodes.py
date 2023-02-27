"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.4
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

def train_model(train_df: pd.DataFrame, contamination_value: float):
    clf = IsolationForest(random_state=42, bootstrap=True, contamination=contamination_value)
    clf.fit(train_df.values)
    return clf

def predict(ml_model, test_df: pd.DataFrame):
    preds = ml_model.predict(test_df.values)
    
    preds_mod = np.array(list(map(lambda x: 1*(x==-1), preds)))

    anomaly_scores = ml_model.score_samples(test_df)
    anomaly_scores_mod = np.array([-x for x in anomaly_scores])

    test_df['ANOMALY_SCORE'] = anomaly_scores_mod
    test_df['ANOMALY'] = preds_mod
    return test_df