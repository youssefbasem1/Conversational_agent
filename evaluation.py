import csv
import os
from conversational_agent import run_conversation, client

def extract_last_assistant_response(messages):
    """
    Extracts the last response from the assistant.
    Args:
        messages (list): List of message history
    Returns:
        str: The last assistant response or an error message if not found
    """
    for msg in reversed(messages):  # Start from the most recent message
        if isinstance(msg, dict) and msg.get("role") == "assistant" and msg.get("content"):
            return msg["content"]  # Return the most recent assistant response
    return "No valid response found"
def evaluate_agents():
    """Runs all agents for a given input and compares responses."""
    queries = ["What's the weather in Paris?", "Solve 25 + 67", "Explain climate change."]
    agent_types = {"1": "Basic", "2": "Chain of Thought", "3": "ReAct"}
    responses = {}
    
    for agent_type in agent_types:
        print(f"\nTesting {agent_types[agent_type]} Agent:")
        responses[agent_types[agent_type]] = run_conversation(client, agent_type)
    
    with open("evaluation_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Agent Type", "User Query", "Response", "User Rating (1-5)"])
        
        for agent, response in responses.items():
            for query in queries:
                print(f"\n{agent} response to '{query}': {response}")
                rating = input("Rate this response (1-5): ")
                final_response = extract_last_assistant_response(response)  # Get only the last assistant message
                writer.writerow([agent, query, final_response, rating])  # Save clean response
    
    print("Evaluation saved in evaluation_results.csv")

if __name__ == "__main__":
    evaluate_agents()