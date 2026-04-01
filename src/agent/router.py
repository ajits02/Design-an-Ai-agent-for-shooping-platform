def classify_intent(user_input: str) -> str:
    """
    Simulates an LLM evaluating the user's prompt to determine the routing path.
    """
    input_lower = user_input.lower()
    
    # Detect Problem Scenarios / Escalation
    escalation_keywords = ["angry", "human", "agent", "terrible", "stolen", "lost"]
    if any(word in input_lower for word in escalation_keywords):
        return "ESCALATION"
        
    # Detect Operational Scenarios (Transactional)
    operational_keywords = ["where is", "order", "track", "cancel", "status"]
    if any(word in input_lower for word in operational_keywords):
        return "OPERATIONAL"
        
    # Default to Informational (Knowledge Base)
    return "INFORMATIONAL"
