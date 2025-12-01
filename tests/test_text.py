import pytest

from src.lab03.text.normalize import normalize_f
from src.lab03.text.tokenize import tokenize_f


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлки", "ежик, елки"),
        ("HeLlo\r\nWorld", "hello world"),
        ("  двойные      пробелы     ", "двойные пробелы"),
        ("", ""),
        ("\n\r\t", ""),
        ("123", "123"),
    ],
)

def test_normalize(source: str,expected: str)->None:
    assert normalize_f(source) == expected


