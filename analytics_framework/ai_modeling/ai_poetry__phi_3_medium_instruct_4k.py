import os
import pandas as pd
import intake
from analytics_framework import INTAKE_LOC
from pathlib import Path
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Data read via intake catalog
CATALOG_LOC = Path.joinpath(INTAKE_LOC, "catalog_entry.yml")
catalog = intake.open_catalog(CATALOG_LOC)

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Phi-3-medium-4k-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    stream=True,
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="Write a poem based on how AI is NOT going to take over humanity, under 100 words"),
    ],
    model=model_name,
)

for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()
