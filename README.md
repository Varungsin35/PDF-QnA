# 📄 AI PDF Q&A Web App — Django + Ollama

An AI-powered web application that allows users to upload PDF files and ask natural language questions. Built with Django, FAISS, and local LLMs via [Ollama](https://ollama.com). No paid APIs. 100% open source and private.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.x-success?logo=django)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 🚀 Features

- 📤 Upload any PDF file
- 🧠 Extracts & chunks PDF text
- 🔍 Finds context using **FAISS**
- 🤖 Answers questions using **local LLMs** (like `llama3`, `mistral`, `phi3`)
- 🧪 No API keys, no internet needed — works fully offline!
- 🌐 Responsive UI (Bootstrap-based)

---

## 🖼️ Screenshots

> *(Add screenshots if available)*

| Upload Page | Question Page |
|-------------|---------------|
| ![upload](screenshots/upload.png) | ![ask](screenshots/ask.png) |

---

## 🧰 Tech Stack

| Layer       | Tools / Frameworks                         |
|-------------|---------------------------------------------|
| Backend     | Django, Python, FAISS                      |
| Frontend    | HTML, CSS, Bootstrap                       |
| AI Engine   | [Ollama](https://ollama.com) (`llama3`, `mistral`, etc.) |
| NLP         | Sentence Transformers (MiniLM)             |
| PDF Parsing | pdfplumber                                 |
| Storage     | SQLite + Django ORM                        |

---

## 🔧 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/pdf_QnA.git
cd pdf_QnA
