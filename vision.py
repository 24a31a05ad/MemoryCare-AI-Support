import os
import base64

from dotenv import load_dotenv
from groq import Groq


# ============================================================
# LOAD ENVIRONMENT
# ============================================================

load_dotenv()


# ============================================================
# GROQ CLIENT
# ============================================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# ============================================================
# SCREENSHOT ANALYZER
# ============================================================

def analyze_screenshot(
    image_bytes,
    mime_type="image/png"
):

    # Convert image to Base64
    image_data = base64.b64encode(
        image_bytes
    ).decode("utf-8")


    # ========================================================
    # GROQ VISION REQUEST
    # ========================================================

    response = client.chat.completions.create(

        # CURRENT GROQ VISION MODEL
        model="qwen/qwen3.8-27b",

        messages=[
            {
                "role": "user",

                "content": [

                    {
                        "type": "text",

                        "text": """
You are MemoryCare's customer-support
screenshot analyzer.

Analyze ONLY information that is actually
visible in the screenshot.

Extract:

1. Error message
2. Error code
3. Product or application name
4. Important visible details
5. Payment amount if visible
6. Suggested issue category

Do NOT invent information.

Return a concise support diagnosis.

Use this format:

Error:
Error Code:
Product:
Amount:
Category:
Important Details:
"""
                    },

                    {
                        "type": "image_url",

                        "image_url": {
                            "url": (
                                f"data:{mime_type};"
                                f"base64,{image_data}"
                            )
                        }
                    }

                ]
            }
        ],

        max_completion_tokens=500
    )


    # ========================================================
    # RETURN VISION RESULT
    # ========================================================

    return response.choices[0].message.content