import os
import pandas as pd
from openai import OpenAI
import intake
from analytics_framework import INTAKE_LOC
from pathlib import Path

# Data read via intake catalog
CATALOG_LOC = Path.joinpath(INTAKE_LOC, "catalog_entry.yml")
catalog = intake.open_catalog(CATALOG_LOC)

# Load the token and endpoint from environment variables
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

# Initialize OpenAI client
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


def analyze_data(intake_catalog_entry):
    # Load the data via intake
    try:
        df_input = catalog[intake_catalog_entry].read()
        print(f"Data loaded successfully {df_input.head()}")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Prepare the data for analysis (simple description of the dataset)
    summary = df_input.describe().to_string()

    # Create the system and user messages for the model
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant skilled in analyzing data.",
        },
        {
            "role": "user",
            "content": f"Here is a summary of my data:\n{summary}\nProvide an analysis of this dataset, "
                       f"provide 03 recommendation regarding investment options",
        }
    ]

    try:
        response = client.chat.completions.create(
            messages=messages,
            model=model_name,
            temperature=5.0,
            max_tokens=2000,
            top_p=1.0
        )

        # Output the analysis from the model
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error generating response: {e}")


# Example usage (other datasets available via intake catalog)
intake_catalog_entry = "twilio_stock_price"
analyze_data(intake_catalog_entry)
