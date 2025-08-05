from src.utils.formatter import format_price

def test_format_price_basic():
    input_price = "1234.5678"
    formatted_result = format_price(input_price)

    assert formatted_result == "$ 1,234.57"

def test_format_price_with_brl_prefix():
    input_price = "500.78"
    formatted_result = format_price(input_price, prefix="R$ ")

    assert formatted_result == "R$ 500.78"

def test_format_price_with_many_decimals():
    assert format_price("9876.599283") == "$ 9,876.60"

def test_format_price_with_invalid_input():
    assert format_price("não é um número") == "não é um número"