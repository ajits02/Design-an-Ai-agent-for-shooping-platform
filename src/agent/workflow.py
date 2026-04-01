from src.agent.state import AgentState
from src.agent.router import classify_intent
from src.utils.validators import validate_order_id
from src.tools.database import get_order_status
from src.tools.knowledge_base import search_policies

def run_agent_workflow(state: AgentState) -> AgentState:
    """The core decision flow of the AI Agent."""
    
    # Step 1: Reason about the intent
    state["query_intent"] = classify_intent(state["latest_user_input"])
    
    # Step 2: Route to appropriate service based on reasoning
    if state["query_intent"] == "ESCALATION":
        state["requires_human"] = True
        state["final_response"] = "I understand your frustration. I am escalating this to a human agent immediately."
        # Trigger handoff API here...
        
    elif state["query_intent"] == "INFORMATIONAL":
        # Contact maintained knowledge sources (RAG)
        policy_info = search_policies(state["latest_user_input"])
        state["final_response"] = f"Based on our policies: {policy_info}"
        
    elif state["query_intent"] == "OPERATIONAL":
        # Evaluate if sufficient user info is available
        if not state["extracted_order_id"]:
            state["final_response"] = "I can help with your order. Please provide your Order ID (e.g., ORD-12345)."
            return state
            
        # Validate identifiers before accessing internal services
        if not validate_order_id(state["extracted_order_id"]):
            state["final_response"] = "The Order ID format is invalid. It must be 'ORD-' followed by 5 numbers."
            return state
            
        # Access internal transactional service
        order_data = get_order_status(state["extracted_order_id"])
        state["final_response"] = f"Here is your order status: {order_data}"
        
    return state
