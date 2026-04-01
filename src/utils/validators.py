import re

def validate_order_id(order_id: str) -> bool:
    """
    Guards the internal transactional database by ensuring the LLM 
    did not hallucinate a malformed Order ID.
    Expected format: ORD-XXXXX (e.g., ORD-12345)
    """
    # Strict regex pattern validation
    pattern = re.compile(r"^ORD-\d{5}$")
    return bool(pattern.match(order_id))

def sanitize_input(user_input: str) -> str:
    """Removes potentially malicious characters before processing."""
    # Basic sanitization example
    return user_input.replace("<", "").replace(">", "").strip()
