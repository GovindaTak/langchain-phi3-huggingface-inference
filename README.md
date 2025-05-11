# langchain-phi3-huggingface-inference
Run Hugging Face's Phi-3 Mini model using LangChain in a Python project via VS Code. This project demonstrates prompt execution using langchain-huggingface and Inference API with token security via .env.
---
```markdown
# 🧠 LangChain + Phi-3 Mini (HuggingFace Inference)

This project demonstrates how to use [LangChain](https://python.langchain.com/) with Hugging Face's `microsoft/Phi-3-mini-4k-instruct` model via the Hugging Face Inference API. It's structured for secure and modular local development using Python.

---

## 🚀 Features

- ✅ Call Phi-3 Mini through HuggingFace Inference API using LangChain.
- ✅ Secure your API key with `.env` using `python-dotenv`.
- ✅ Lightweight and modular code for easy integration into future apps.
- ✅ Ideal for testing LLM prompts, building chains, or extending to agents.

---

## 🧩 Tech Stack

- **Python 3.10+**
- **LangChain 0.3.11**
- **Hugging Face Inference API**
- **HuggingFaceHub 0.26.5**
- **python-dotenv**

---

## 📁 Folder Structure

```

langchain-phi3-mini-hf-inference/
├── main.py               # Core logic to invoke GPT model
├── .env                  # API token file (not committed)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YourUsername/langchain-phi3-mini-hf-inference.git
cd langchain-phi3-mini-hf-inference
````

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your API Key to `.env`

Create a `.env` file in the root directory:

```
HUGGINGFACEHUB_API_TOKEN=your_actual_token
```

🔗 [Get your token here](https://huggingface.co/settings/tokens)

### 5️⃣ Run the Script

```bash
python main.py
```

---

## 💡 Example Output

```
Response from Phi-3:

• Generative AI refers to AI models that can create content such as text, images, and music.
• It uses deep learning techniques like transformers and large language models.
• Applications include chatbots, content generation, image synthesis, and more.
```

---

## 🔐 Security Best Practices

Make sure `.env` is in your `.gitignore`:

```bash
.env
```

Never push your secret keys to GitHub.

---

## 📌 Future Enhancements

* Integrate LangChain Prompt Templates
* Wrap with `LLMChain`
* Build a minimal Streamlit web app
* Add tools & memory to build autonomous agents

---

## 🙌 What I Learned

* How to use LangChain with Hugging Face-hosted models
* How to design secure API-based apps in Python
* Prompt formatting with LangChain's LLM wrappers
* Effective logging and API response handling
* Best practices for environment setup and modular code

---

## 🧠 Author

👤 Govinda Tak
📫 Email: [govindatak19@gmail.com](mailto:govindatak19@gmail.com)
🔗 GitHub: [GovindaTak](https://github.com/GovindaTak)

---

## 📜 License

Licensed under the MIT License.


