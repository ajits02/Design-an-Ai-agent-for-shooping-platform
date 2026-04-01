def search_policies(query: str) -> str:
    """
    Mock function representing a semantic search against a Vector Database (like Pinecone).
    """
    if "return" in query.lower():
        return "You have 30 days to return standard items, and 14 days for electronics."
    elif "shipping" in query.lower():
        return "Standard shipping takes 3-5 business days."
    return "Please check our FAQ page for more details."
  
