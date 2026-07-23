def get_internal_stock_price(ticker: str):
    """
    Primary internal stock database.

    Use this tool first whenever the user asks for
    a stock price.

    This tool may occasionally fail because the
    internal database could be unavailable.
    """

    raise Exception("Database Timeout")


def search_public_web(query: str):
    """
    Backup search tool.

    Use this tool whenever the internal stock
    database is unavailable.

    Returns publicly available stock information.
    """

    if "apple" in query.lower():
        return "Apple stock is currently trading around $170."

    if "microsoft" in query.lower():
        return "Microsoft stock is currently trading around $520."

    return "No public stock data found."