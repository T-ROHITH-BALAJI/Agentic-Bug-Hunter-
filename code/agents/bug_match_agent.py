from agents.retrieval_agent import retrieve_docs

def match_bug(context):
    docs = retrieve_docs(context)

    best_doc = ""
    if docs:
        best_doc = docs[0].get("text", "")

    return {
        "context": context,
        "doc_text": best_doc
    }
