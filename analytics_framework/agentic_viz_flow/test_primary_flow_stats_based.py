from langchain.agents import initialize_agent, Tool
# from langchain_deepseek import ChatDeepSeek
from langchain.llms import OpenAI
import pandas as pd
import matplotlib.pyplot as plt
import io
import os
import base64

# NOTE: Using GitHub models here (add your preferred token attribute)
# Refer analytics_framework/langchain/hello_world_lc.py for using GitHub token for auth

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "DeepSeek-R1"

def test_func(int: model_name, param_value =None)-> int():
    return 0

llm = OpenAI(base_url=endpoint, temperature=0, api_key=token, model=model_name)  # You MUST set your OpenAI key!
tools = [
    Tool(
        name="SuggestVisualization",
        func=test_func,
        description="Suggests an appropriate visualization type based on the provided DataFrame.",
    ),
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)


try:
    df = pd.read_csv("../intake/data/TWLO_stock.csv")  # Replace with your CSV file.
    df_summary = df.describe()
    result = agent.run(f"Given this dataset summary, suggest and generate a draft visualization: {df_summary.to_string()}")
    print(result)
except FileNotFoundError:
    print("Error: dataset not found. Please provide a valid CSV file.")
except Exception as e:
    print(f"An error occurred: {e}")
