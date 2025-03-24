import pytest


@pytest.mark.parametrize(
    "kwargs",
    [
        pytest.param({"slice": 7, "n": 10, "result": 2}, id="test_case_1"),
        pytest.param({"slice": 4, "n": 12, "result": 3}, id="test_case_2"),
    ],
)
def test_solution(kwargs):
    from src.solution import solution

    result = kwargs.pop("result")
    assert solution(**kwargs) == result, f"Failed for input (kwargs={kwargs})"
