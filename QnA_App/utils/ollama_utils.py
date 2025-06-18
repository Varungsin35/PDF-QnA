import subprocess

def ask_ollama(question, context):
    prompt = f"Context:\n{context}\n\nQuestion:\n{question}\nAnswer:"
    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama3'],  # or 'llama3' / 'phi3'
            input=prompt,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'  # ✅ fix for Windows encoding issue
        )
        return result.stdout.strip()
    except Exception as e:
        return f"❌ Error getting response from Ollama: {str(e)}"
