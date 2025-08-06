# Flask Crypto Price Tracker

A web application built with Python and Flask that displays real-time cryptocurrency prices, fetched from the public Binance API.

This project was developed as a portfolio item to demonstrate a set of back-end development skills, including:
- Consumption of REST APIs (Binance)
- Building web applications with the Flask framework
- Template rendering with Jinja2
- Data processing and filtering in Python
- Implementation of dynamic front-end updates with JavaScript (Fetch API)
- Writing automated tests with Pytest

## Features

*   **Refined Coin List:** Displays a dropdown with the top 50 cryptocurrencies by value (price) tradable on Binance, avoiding clutter with irrelevant coins.
*   **Interactive Query:** Allows the user to select a cryptocurrency and a base currency (USDT or BRL) for querying.
*   **Real-time Updates:** The price of the selected coin automatically updates every 1 second, without the need to refresh the page.
*   **Clean Interface:** Presents data clearly and objectively.

## Live Demo

*   You can access this project and see it running in real-time here: https://crypto-price-tracker-ixx7.onrender.com/

## Demo

![Gif_demo](assets/demo.gif)

## How to Run the Project Locally

### Prerequisites

*   Python 3.8 or higher
*   Git

### Installation

1.  Clone the repository to your machine:
    git clone https://github.com/dusvak/crypto-price-tracker

2.  Navigate to the project directory:
    cd crypto-price-tracker

3.  Create and activate a virtual environment:
    python -m venv .venv

    # Activate on Windows 
    .venv\Scripts\Activate.ps1

    # Activate on macOS/Linux
    source .venv/bin/activate

4.  Install project dependencies:
    pip install -r requirements.txt

### Execution

1.  With the virtual environment active and from the project's root folder, start the Flask server:
    python -m src.main

2.  Open your browser and access `http://127.0.0.1:5001` to view the application.

### Running the Tests

1.  To verify the integrity of utility functions, run Pytest in the project root:
    pytest

## Project Structure

´´´
binance-crypto-tracker/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   ├── api/
│   │   └── api_client.py      # Logic for communication with external APIs
│   ├── templates/
│   │   └── index.html         # Web page template
│   ├── utils/
│   │   └── formatter.py       # Utility functions (price formatting)
│   └── main.py                # Flask application (routes and main logic)
└── tests/
    └── test_formatter.py      # Tests for formatting functions
´´´