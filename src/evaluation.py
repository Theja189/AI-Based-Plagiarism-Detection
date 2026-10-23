
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)


def evaluate_predictions(y_true, y_pred) -> dict:
    """Calculate standard binary classification evaluation metrics."""
    if len(y_true) == 0:
        raise ValueError("Evaluation data cannot be empty.")

    if len(y_true) != len(y_pred):
        raise ValueError("True labels and predictions must have equal lengths.")

    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(
            precision_score(y_true, y_pred, zero_division=0)
        ),
        "recall": float(
            recall_score(y_true, y_pred, zero_division=0)
        ),
        "f1_score": float(
            f1_score(y_true, y_pred, zero_division=0)
        ),
        "confusion_matrix": confusion_matrix(
            y_true, y_pred, labels=[0, 1]
        ).tolist(),
    }
