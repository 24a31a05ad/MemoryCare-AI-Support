from memory import remember

customer_history = """
Customer: Bhavani

Previous support incident:
- Issue: Payment failed.
- Error code: 4032.
- Product: Mobile App.
- First troubleshooting step: Clear browser cache.
- Outcome: Payment succeeded after clearing the browser cache.

Customer preferences:
- Preferred language: Telugu.
- Communication style: Clear and simple.

Important support context:
- If Bhavani reports the same Error 4032 again, check the previous successful troubleshooting step before suggesting a new solution.
"""

remember(customer_history)

print("Customer support history stored successfully!")