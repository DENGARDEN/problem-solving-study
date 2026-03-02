import pytest


@pytest.mark.parametrize(
    "kwargs",
    [
        pytest.param({"a": None, "result": None}, id="test_case_1"),
        pytest.param({"a": None, "result": None}, id="test_case_2"),
    ],
)
def test_solution(kwargs):
    # from src.best_solution import solution as best_solution
    from src.solution import solution  # Import the solution function here

    result = kwargs.pop("result")
    assert solution(**kwargs) == result, f"Failed for input (kwargs={kwargs})"
