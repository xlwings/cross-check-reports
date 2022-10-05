from pathlib import Path

import pytest
import xlwings as xw

@pytest.fixture(scope="module")
def reports():
    for f in (Path(".") / "reports").glob("[!~]*.xls*"):
        print(f.name)
        if f.name.endswith("1.xlsx"):
            report1 = xw.Book(f, mode="r")
        elif f.name.endswith("2.xlsx"):
            report2 = xw.Book(f, mode="r")
    yield report1, report2


def test_same_value_one(reports):
    report1, report2 = reports
    assert report1.sheets[0]['A1'].value == report2.sheets[0]['A1'].value


def test_same_value_five(reports):
    report1, report2 = reports
    assert report1.sheets[0]['A5'].value == report2.sheets[0]['A5'].value