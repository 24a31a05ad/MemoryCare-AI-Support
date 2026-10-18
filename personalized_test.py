from agent import support_agent

question = """
My payment is failing again. Can you check what happened last time
and tell me what I should try first?
"""

answer = support_agent(question)

print("\n--- MEMORYCARE PERSONALIZED RESPONSE ---")
print(answer)