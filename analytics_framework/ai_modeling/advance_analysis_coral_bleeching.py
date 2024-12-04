import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# central dataset input via intake catalog
import intake
from analytics_framework import INTAKE_LOC
from pathlib import Path

CATALOG_LOC = Path.joinpath(INTAKE_LOC, "catalog_entry.yml")
catalog = intake.open_catalog(CATALOG_LOC)
df_input_coral = catalog["global_coral_bleaching"].read()
summary_coral = df_input_coral.describe().to_string()

client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

response = client.complete(
    messages=[
        UserMessage(
            content=f"Here is a dataset summary:\n{summary_coral}\nCan you provide top 03 bleached countries and damage cause?")
    ],
    model="Meta-Llama-3-8B-Instruct",
    temperature=0.8,
    max_tokens=2048,
    top_p=0.1
)
print(response.choices[0].message.content)
