import os
from mistralai import Mistral, UserMessage, SystemMessage

# central dataset input via intake catalog
import intake
from analytics_framework import INTAKE_LOC
from pathlib import Path

df_input_coral = catalog["global_coral_bleaching"].read()
summary_coral = df_input_coral.describe().to_string()

client = Mistral(
    api_key=os.environ["GITHUB_TOKEN"],
    server_url="https://models.inference.ai.azure.com"
)

response = client.chat(
    model="Mistral-large-2407",
    messages=[
        SystemMessage(content="You are a Data Scientist specializing is crafting great story"),
        UserMessage(
            content=f"Here is a dataset summary:\n{summary_coral}\nCan you provide top 03 bleached countries and damage cause?"),

    ],
    temperature=0.8,
    max_tokens=2048,
    top_p=0.1
)

print(response.choices[0].message.content)
