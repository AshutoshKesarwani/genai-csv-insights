import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_insights(summary: dict) -> str:
    prompt = f"""You are a business analyst. Given this statistical summary of a dataset,
write a clear, plain-English summary for a non-technical business audience.

Cover:
1. What the data broadly contains
2. Key trends or patterns
3. Any notable outliers or data quality issues
4. 2-3 actionable business recommendations

Statistical summary (JSON):
{json.dumps(summary, indent=2, default=str)}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    return response.choices[0].message.content