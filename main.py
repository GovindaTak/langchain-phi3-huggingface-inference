from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Correct HuggingFace Endpoint usage (Phi-3)
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-1.1-2b-it",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    do_sample=False,
    return_full_text=False,
    max_new_tokens=1000,
)

# Correct ChatHuggingFace usage (No model_id needed here)
chat_model = ChatHuggingFace(llm=llm)

# Prepare message
messages = [HumanMessage(content="Explain what is Generative AI in 3 bullet points.")]

# Call the model
response = chat_model.invoke(messages)

# Print output
print("\nResponse from Gemma:\n", response.content)

messages.append(response)

prompt="what is Astrology ?"

messages.append(HumanMessage(content=prompt))
response=chat_model.invoke(messages)
print(response.content)
