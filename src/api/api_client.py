import requests

BASE_URL = "https://api.binance.com/api/v3"

def get_symbol_price(symbol):
    url = f"{BASE_URL}/ticker/price"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    params = {"symbol": symbol}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro de HTTP: {http_err}")
    except Exception as err:
        print(f"Ocorrou um outro erro: {err}")
    
    return None

EXCHANGE_INFO_CACHE = {}

def get_top_symbols_by_price(limit=50):

    if "top_symbols" in EXCHANGE_INFO_CACHE:
        return EXCHANGE_INFO_CACHE["top_symbols"]
    
    url = f"{BASE_URL}/ticker/price"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        all_tickers = response.json()

        usdt_tickers = [t for t in all_tickers if t['symbol'].endswith('USDT')]

        sorted_tickers = sorted(usdt_tickers, key=lambda x: float(x['price']), reverse=True)

        top_symbols = [ticker['symbol'].replace('USDT', '') for ticker in sorted_tickers[:limit]]

        EXCHANGE_INFO_CACHE["top_symbols"] = top_symbols
        print(f"INFO: Lista de top {limit} moedas por preço carregada e em cache.")
        return top_symbols

    except Exception as err:
        print(f"Ocorreu um outro erro ao buscar informações da exchange: {err}")
        return ["BTC", "ETH", "BNB"]
    