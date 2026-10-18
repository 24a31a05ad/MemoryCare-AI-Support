from memory import recall
from llm import generate_response


def support_agent(user_message):
    # 1. Search Hindsight for relevant customer memory
    memories = recall(user_message)

    # 2. Give the memories + current question to the LLM
    response = generate_response(
        user_message=user_message,
        memories=memories
    )

    return response