def format_price(price_str: str, prefix: str = "$ ") -> str:
    try:
        price_float = float(price_str)
        return f"{prefix}{price_float:,.2f}"
    except (ValueError, TypeError):
        return price_str