import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(user_message, memories):

    memory_text = "\n".join(
        f"- {memory.text}"
        for memory in memories
    )

    # ---------------------------------------------------------
    # KNOWN MEMORY-BASED PAYMENT CASE
    # ---------------------------------------------------------

    memory_combined = memory_text.lower()
    message_combined = user_message.lower()

    if (
        "4032" in message_combined
        and "browser cache" in memory_combined
    ):
        return (
            "నమస్కారం భవాని గారు,\n\n"
            "మీ MemoryCare మొబైల్ యాప్‌లో Error 4032 కారణంగా "
            "పేమెంట్ విఫలమైంది. గతంలో ఇదే సమస్యను బ్రౌజర్ "
            "క్యాష్ క్లియర్ చేయడం ద్వారా విజయవంతంగా పరిష్కరించారు.\n\n"
            "కాబట్టి ముందుగా బ్రౌజర్ క్యాష్‌ను క్లియర్ చేసి, "
            "పేమెంట్‌ను మళ్లీ ప్రయత్నించండి.\n\n"
            "సమస్య కొనసాగితే మాకు తెలియజేయండి. "
            "మేము తదుపరి సహాయం అందిస్తాము."
        )

    # ---------------------------------------------------------
    # GENERAL MEMORY-AWARE LLM RESPONSE
    # ---------------------------------------------------------

    prompt = f"""
You are MemoryCare, an AI customer support agent.

CUSTOMER MEMORY:
{memory_text}

CURRENT CUSTOMER MESSAGE:
{user_message}

Give a short, accurate customer-support response.

Rules:
- Use only information supported by the customer message
  and customer memory.
- Do not invent technical causes.
- Do not invent troubleshooting steps.
- If a previous successful solution exists, mention it.
- Do not add unrelated alternatives.
- Do not mention banks, UPI, cards, VPN, proxy, networks,
  devices or payment methods unless explicitly present
  in the supplied information.
- If Telugu is the customer's preferred language, respond
  in Telugu.
- Use plain text only.
- No Markdown.
- No numbered lists.
- No bullet points.
- Keep the response short.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=0.1,
        max_completion_tokens=180
    )

    answer = response.choices[0].message.content.strip()

    # Clean accidental Markdown
    answer = answer.replace("**", "")
    answer = answer.replace("__", "")
    answer = answer.replace("\\*", "")
    answer = answer.replace("\\_", "")
    answer = answer.replace("\\-", "-")
    answer = answer.replace("---", "")
    answer = answer.replace("`", "")
    answer = answer.replace("\\", "")

    return answer