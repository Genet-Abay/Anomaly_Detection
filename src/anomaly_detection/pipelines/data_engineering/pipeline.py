"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import my_train_test_split

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=my_train_test_split,
            inputs="creditcard",
            outputs=["train_data", "test_data", "test_labels"],
            name="node_train_test_split"
            ),
    ])