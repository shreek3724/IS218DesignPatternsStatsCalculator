import pytest
from calculator.inputs import read_csv_values


def test_different_csv_column(tmp_path):
    path = tmp_path / "measurements.csv"
    path.write_text("measurement\n10\n20\n30\n40\n50\n")

    assert read_csv_values(path, "measurement") == [10, 20, 30, 40, 50]


def test_missing_requested_column(tmp_path):
    path = tmp_path / "measurements.csv"
    path.write_text("wrong\n10\n20\n30\n")

    with pytest.raises(ValueError, match="measurement"):
        read_csv_values(path, "measurement")