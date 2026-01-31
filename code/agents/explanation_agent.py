def generate_explanation(bug_info):
    doc = bug_info.get("doc_text", "")
    context = bug_info.get("context", "")

    if doc:
        clean = doc.replace("\n", " ").replace("\r", " ").strip()
        sentence = clean.split(".")[0]

        # Normalize wording
        if "changed" in sentence.lower():
            return sentence + "."
        else:
            return f"Incorrect usage related to {sentence}."

    return f"Incorrect usage related to {context}."
