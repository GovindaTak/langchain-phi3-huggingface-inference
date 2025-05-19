# 🧠 LangChain with Hugging Face & OpenAI | Prompt Engineering Practice

This project demonstrates how to use **LangChain** with **Hugging Face (Phi-3 Mini)** and **OpenAI (GPT-3.5 Turbo)** for prompt engineering tasks, specifically focused on invoking models and comparing their behavior with similar prompts.

---

## 📌 Objective

To explore and compare how Hugging Face’s Phi-3 Mini and OpenAI’s GPT-3.5 respond to prompt engineering using LangChain’s `HuggingFaceEndpoint` and `ChatOpenAI` wrappers.

---

## 🧪 What This Project Includes

* ✅ Installation & environment setup for LangChain, HuggingFace, OpenAI
* ✅ Use of `.env` for securely loading API keys
* ✅ Loading Phi-3 Mini (`microsoft/Phi-3-mini-4k-instruct`) via Hugging Face
* ✅ Prompt testing with OpenAI’s GPT-3.5 Turbo & GPT-3.5 Turbo Instruct
* ✅ Comparative outputs for the same prompts
* ✅ Focus on practical GenAI skill-building with LLMs

---

## 🔧 Tech Stack

* Python 3.11
* LangChain `0.3.11`
* LangChain OpenAI & HuggingFace integrations
* Hugging Face Transformers `4.46.3`
* OpenAI API
* Google Colab or local Jupyter setup

---

## 🧠 Skills Learned

* Setting up Hugging Face API with secure access
* Using `HuggingFaceEndpoint` from LangChain for model inference
* Invoking OpenAI GPT models using `ChatOpenAI` and `OpenAI`
* Comparing structured and conversational responses
* Prompt crafting for LLMs and formatting responses
* Fine-tuning generation parameters (temperature, max tokens, etc.)

---

## 🚀 Setup Instructions

### 1. Install dependencies

```bash
pip install langchain==0.3.11
pip install langchain-openai==0.2.12
pip install langchain-community==0.3.11
pip install langchain-huggingface
pip install huggingface_hub==0.26.5
pip install transformers==4.46.3
```

### 2. Load your API keys securely

```python
from getpass import getpass
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = getpass("Enter HuggingFace Token: ")
os.environ["OPENAI_API_KEY"] = getpass("Enter OpenAI API Key: ")
```

---

## 🧪 How It Works

### Hugging Face Setup

```python
from langchain_huggingface import HuggingFaceEndpoint

repo_id = "microsoft/Phi-3-mini-4k-instruct"
phi3_prompt = """<|user|>Explain what is Generative AI in 3 bullet points<|end|>\n<|assistant|>"""

llm = HuggingFaceEndpoint(repo_id=repo_id, temperature=0.5, max_new_tokens=1000)
response = llm.invoke(phi3_prompt)
print(response)
```

### OpenAI GPT-3.5 Turbo (Instruct)

```python
from langchain_openai import OpenAI

chatgpt = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
response = chatgpt.invoke("Explain what is Generative AI in 3 bullet points")
print(response)
```

### OpenAI ChatGPT (Chat Interface)

```python
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
response = chat_model.invoke("Explain what is Generative AI in 3 bullet points")
print(response.content)
```

---

## 📊 Output Comparison (Sample)

| Model            | Output Style          | Structure      |
| ---------------- | --------------------- | -------------- |
| Phi-3 Mini       | Bullet points (basic) | Informative    |
| GPT-3.5 Instruct | Formal and direct     | Clear bullets  |
| GPT-3.5 Turbo    | Conversational        | Natural & rich |

---

## 🧠 Learnings Recap

* How to use Hugging Face models via LangChain
* LangChain’s unified LLM interface across providers
* Prompt formatting and structuring for consistent results
* Comparative behavior of LLMs for the same query
* Token usage monitoring and response control

---

## 📌 Next Steps

* ✅ Wrap responses with chains and agents
* ✅ Add memory or document input (RAG)
* 🔜 Build a prompt evaluation dashboard
* 🔜 Try other models like Mistral, Llama 3 via Hugging Face

---

## 📜 License

MIT License

---


