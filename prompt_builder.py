import json

def build_prompt(report_text, dictionary, prompt_template):
    if "groundTruth" in dictionary:
        dictionary_str = json.dumps(dictionary["groundTruth"], indent=2, ensure_ascii=False)
    else:
        dictionary_str = json.dumps(dictionary, indent=2, ensure_ascii=False)

    if "const systemPrompt" in prompt_template:
        sys_start = prompt_template.index('`')+1
        sys_end = prompt_template.index('`', sys_start)
        system_prompt = prompt_template[sys_start:sys_end]
        user_prompt = prompt_template[prompt_template.index('const userPrompt'):].split('`')[1]

        final_prompt = (
            f"{system_prompt}\n\n"
            f"{user_prompt}\n\n"
            "Referti di laboratorio OCR estratto:\n"
            f"{report_text}\n\n"
            "Esempi ground truth analитов:\n"
            f"{dictionary_str}\n"
        )
        return final_prompt
    else:
        return prompt_template + "\nOCR:\n" + report_text + "\n\nDizionario:\n" + dictionary_str
