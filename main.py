import os
import sys
import json
from dotenv import load_dotenv

from ocr import extract_text_from_pdf
from prompt_builder import build_prompt
from openai_client import get_structured_report

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True, help="Path to input PDF (scanned clinical report)")
    parser.add_argument("--dictionary", required=True, help="Path to dictionary (JSON)")
    parser.add_argument("--prompt", required=True, help="Prompt template (txt/js)")
    parser.add_argument("--output", required=True, help="Path for output JSON")
    args = parser.parse_args()

    load_dotenv()
    print("Running OCR...")
    report_text = extract_text_from_pdf(args.pdf)

    with open(args.dictionary, "r", encoding="utf-8-sig") as f:
        dictionary = json.load(f)

    with open(args.prompt, "r", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = build_prompt(report_text, dictionary, prompt_template)

    print("Calling OpenAI GPT-4...")
    result = get_structured_report(prompt)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"Structured output saved to {args.output}")

if __name__ == "__main__":
    main()
