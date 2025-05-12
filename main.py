from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
HUGGINGFACEHUB_API_TOKEN=os.getenv("HUGGINGFACEHUB_API_TOKEN")

repo_id="microsoft/Phi-3-mini-4k-instruct"

llm=HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.5,
    max_new_tokens=1000,
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
)

phi3_prompt="""<|user|>Explain what is Generative AI in 3 bullet point<|end|>\n<|assistant|>"""

response=llm.invoke(phi3_prompt)

print("\nResponse from Phi-3 :\n",response)
