from kedro.pipeline import Pipeline, node, pipeline

from .nodes import clean_data, preprocess_data, download_dataset


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=download_dataset,
                inputs={"url": "url", "destination": "destination"},
                outputs=None
            ),
            node(
                func=clean_data,
                inputs="study_performance",
                outputs=["X_processed_1", "y"]
            ),
            node(
                func=preprocess_data,
                inputs="X",
                outputs="X_processed_2"
            )
        ]
    )
