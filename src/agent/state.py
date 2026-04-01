from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    """
    Maintains the conversation state and tracks extracted entities.
    This allows the agent to evaluate if it has sufficient information.
    """
    chat_history: List[dict]       # Full conversation history
    latest_user_input: str         # The most recent message
    query_intent: Optional[str]    # 'INFORMATIONAL', 'OPERATIONAL', 'ESCALATION'
    extracted_order_id: Optional[str] # Evaluated during Operational queries
    requires_human: bool           # Escalation trigger flag
    final_response: Optional[str]  # The message to send back to the user
