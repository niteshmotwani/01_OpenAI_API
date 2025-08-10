from openai import OpenAI
from dotenv import load_dotenv
import os
import httpx
load_dotenv()

insecure_httpx = httpx.Client(verify=False)

apiKey = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=apiKey,
    http_client=insecure_httpx
)

response = client.responses.create(
    model="gpt-5-nano",
    input="My first openAI API call hurray! what do you say?"

)
print(response.output_text)