import pytest
from main import parse, Temperature, DewPoint


@pytest.mark.parametrize(
    ("message", "expected"),
    [
        ("", []),
        ("M01/M23", [Temperature(value=-1), DewPoint(value=-23)]),
        ("M01/", [Temperature(value=-1)]),
        ("01/M23", [Temperature(value=1), DewPoint(value=-23)]),
        ("20/12", [Temperature(value=10), DewPoint(value=12)]),
    ]
)
def test_main(message, expected):
    assert parse(message) == expected
