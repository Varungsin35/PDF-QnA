from django.shortcuts import render, redirect
from .models import PDF, QAHistory
from .utils.pdf_utils import extract_text_from_pdf
from .utils.embedding_utils import chunk_text, embed_and_index, get_relevant_chunk, model
from .utils.ollama_utils import ask_ollama

pdf_text_chunks = []
faiss_index = None

def upload_pdf(request):
    global faiss_index, pdf_text_chunks

    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf = PDF.objects.create(file=request.FILES['pdf_file'])
        text = extract_text_from_pdf(pdf.file)
        chunks = chunk_text(text)
        faiss_index, embeddings, pdf_text_chunks = embed_and_index(chunks)
        return redirect('ask_question')

    return render(request, 'upload.html')

def ask_question(request):
    global faiss_index, pdf_text_chunks
    answer = None

    if faiss_index is None or not pdf_text_chunks:
        return render(request, 'question.html', {
            'answer': "❌ Please upload a PDF first from the homepage."
        })

    if request.method == 'POST':
        question = request.POST.get('question')
        context = get_relevant_chunk(question, faiss_index, pdf_text_chunks, model)
        answer = ask_ollama(question, context)

    return render(request, 'question.html', {'answer': answer})

