
import pytest

from src.evaluation import evaluate_predictions


def test_evaluation_metrics_for_correct_predictions():
    result = evaluate_predictions([0, 1, 0, 1], [0, 1, 0, 1])

    assert result["accuracy"] == pytest.approx(1.0)
    assert result["precision"] == pytest.approx(1.0)
    assert result["recall"] == pytest.approx(1.0)
    assert result["f1_score"] == pytest.approx(1.0)
    assert result["confusion_matrix"] == [[2, 0], [0, 2]]


def test_evaluation_metrics_for_mixed_predictions():
    result = evaluate_predictions([0, 1, 0, 1], [0, 1, 1, 0])

    assert result["accuracy"] == pytest.approx(0.5)
    assert result["confusion_matrix"] == [[1, 1], [1, 1]]


def test_empty_evaluation_data_raises_error():
    with pytest.raises(ValueError):
        evaluate_predictions([], [])


def test_different_lengths_raise_error():
    with pytest.raises(ValueError):
        evaluate_predictions([0, 1], [0])


def test_precision_handles_no_positive_predictions():
    result = evaluate_predictions([0, 1, 0], [0, 0, 0])

    assert result["precision"] == pytest.approx(0.0)
    assert result["recall"] == pytest.approx(0.0)
