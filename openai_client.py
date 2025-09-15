import os
import openai
import json
import re

def get_structured_report(prompt: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a Healthcare specialist capable of extracting information from Italian Referti di laboratorio. Output ONLY the JSON array as specified."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=4096
    )
    content = response.choices[0].message.content.strip()

   
    match = re.search(r'(\[.*\])', content, re.DOTALL)
    if match:
        json_text = match.group(1)
    else:
        json_text = content.strip('"\'')

    try:
        obj = json.loads(json_text)
    except Exception as e:
        obj = json.loads(json.loads(json_text))

    return json.dumps(obj, ensure_ascii=False, indent=2)
