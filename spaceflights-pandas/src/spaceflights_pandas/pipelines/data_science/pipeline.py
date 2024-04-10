from kedro.pipeline import Pipeline, node, pipeline

from .nodes import plot_scatter, evaluate_model, train_model, save_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=train_model,
                inputs={"X": "X", "y": "y"},
                outputs=["model", "X_test", "y_test"]
            ),
            node(
                func=evaluate_model,
                inputs={"true": "true", "predicted": "predicted"},
                outputs=["mae", "rmse", "r2_square"]
            ),
            node(
                func=save_model,
                inputs={"model": "model", "output_dir": "output_dir"},
                outputs=None
            ),
            node(
                func=plot_scatter,
                inputs={"y_test": "y_test", "y_pred": "y_pred"},
                outputs=None
            )
        ]
    )
