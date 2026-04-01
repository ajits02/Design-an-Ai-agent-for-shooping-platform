def get_order_status(order_id: str) -> dict:
    """
    Mock function representing an API call to the transactional SQL/NoSQL database.
    """
    mock_db = {
        "ORD-12345": {"status": "Shipped", "delivery_date": "2024-05-20"},
        "ORD-99887": {"status": "Processing", "delivery_date": "2024-05-25"}
    }
    return mock_db.get(order_id, {"error": "Order not found in the system."})
