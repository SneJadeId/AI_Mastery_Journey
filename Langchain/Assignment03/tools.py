def refund_order(transaction_id: str):

    """
    Use ONLY when the user wants a refund for a completed payment.

    Examples:
    - refund
    - money back
    - reverse charge
    - wrong payment
    - mistaken transaction

    Never use for stopping future subscription payments.
    """

    return f"Refund initiated successfully for Transaction ID {transaction_id}"


def cancel_subscription(email: str):

    """
    Use ONLY when the user wants to stop future recurring subscription charges.

    Examples:
    - stop charging
    - cancel subscription
    - don't renew
    - stop taking money
    - cancel membership

    Never use this tool for refund requests.
    """

    return f"Subscription cancelled successfully for {email}"