import pytest
from src.lab03.text.normalize import normalize_f


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\\nМИр\\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\\r\\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize_f(source) == expected

def test_tokenize_basic(source, expected):
    
    pass

def test_count_freq_and_top_n():
    # TODO: Реализовать тесты частоты
    pass

def test_top_n_tie_breaker():
    # TODO: Реализовать тесты для топ_н
    pass