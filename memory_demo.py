from memory import recall

query = """
Bhavani has a payment problem again.
What happened during her previous payment issue?
What error did she get?
What solution worked?
"""

memories = recall(query)

print("\n--- CUSTOMER MEMORY ---")

for memory in memories:
    print(f"- {memory.text}")