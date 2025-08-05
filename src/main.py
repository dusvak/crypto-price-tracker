from src.api.api_client import get_symbol_price, get_top_symbols_by_price
from src.utils.formatter import format_price
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])

def index():    
    all_symbols = get_top_symbols_by_price()

    crypto = "BTC"
    base = "USDT"

    if request.method == 'POST':
        crypto = request.form.get('crypto_select', 'BTC').upper()
        base = request.form.get('base', 'USDT').upper()

    symbol = f"{crypto}{base}"
    price_data = get_symbol_price(symbol)

    context = {
        'all_symbols': all_symbols,
        'crypto': crypto,
        'base': base,
        'symbol': symbol,
        'price': 'Não encontrado'
    }

    if price_data and 'price' in price_data:
        price_prefix = "$ " if base == "USDT" else "R$ "
        formatted_price = format_price(price_data['price'], prefix=price_prefix)
        context['price'] = formatted_price

    return render_template('index.html', context=context)

@app.route('/api/price/<path:symbol>')
def get_price_api(symbol):
    price_data = get_symbol_price(symbol)

    if price_data and 'price' in price_data:
        base = 'USDT' 
        if symbol.endswith('BRL'):
            base = 'BRL'
        price_prefix = "$ " if base == "USDT" else "R$ "
        formatted_price = format_price(price_data['price'], prefix=price_prefix)

        return {
            'symbol': price_data['symbol'],
            'price': formatted_price
        }
    else:
        return {'error': 'Simbolo não encontrado'}, 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    #main()

