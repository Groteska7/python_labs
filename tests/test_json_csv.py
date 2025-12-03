import csv
import json
from pathlib import Path
import pytest

from src.lab05.A import json_to_csv

def test_json_to_csv_basic(tmp_path: Path):
    start = tmp_path / "people.json"
    end = tmp_path / "people.csv"

    data = [
        {"Name": "Emily","Surname": "Johnson","Age": "24"},
        {"Name": "Daniel","Surname": "Williams","Age": "31"},
    ]
    start.write_text(json.dumps(data, ensure_ascii=False, indent=3), encoding="utf-8")

    json_to_csv(str(start), str(end))

    with end.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 3
    assert {"Name", "Surname", "Age"} <= set(rows[0].keys())
    assert rows[0]["Name"] == "Emily"
    assert rows[0]["Surname"] == "Johnson"
    assert rows[0]["Age"] == "24"
    assert rows[1]["Name"] == "Daniel"
    assert rows[1]["Surname"] == "Williams"
    assert rows[1]["Age"] == "31"
