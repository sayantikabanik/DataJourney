from langchain.agents import initialize_agent, Tool
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

def suggest_visualization(dataframe):
    """Suggests a visualization type based on the characteristics of the data.
    :param dataframe: A pandas DataFrame containing the data.
    :return: A string representing the suggested visualization type"""

    num_numerical_cols = len(dataframe.select_dtypes(include=['number']).columns)
    num_categorical_cols = len(dataframe.select_dtypes(exclude=['number']).columns)

    if num_numerical_cols == 1 and num_categorical_cols == 0:
        return "histogram"  # Or boxplot, density plot
    elif num_numerical_cols == 2 and num_categorical_cols == 0:
        return "scatter plot"
    elif num_categorical_cols > 0 and num_numerical_cols == 0:
        return "bar chart"  # Or pie chart
    elif num_categorical_cols > 0 and num_numerical_cols == 1:
        return "boxplot" # Or violinplot
    elif num_categorical_cols == 0 and num_numerical_cols > 2:
        return "pairplot" # Or correlation matrix
    else:
        return "generic plot"  # Default if no clear match

def generate_visualization_draft(dataframe, visualization_type):
    """Generates a quick draft of the suggested visualization using matplotlib.
    :param dataframe: A pandas DataFrame containing the data.
    :param visualization_type: A string representing the type of visualization to generate.
    :return: A string containing the base64-encoded PNG image of the visualization."""

    plt.figure()  # Create a new figure for each plot
    if visualization_type == "histogram":
        col_name = dataframe.select_dtypes(include=['number']).columns[0]
        dataframe[col_name].hist()
        plt.title(f"Histogram of {col_name}")

    elif visualization_type == "scatter plot":
        col1 = dataframe.select_dtypes(include=['number']).columns[0]
        col2 = dataframe.select_dtypes(include=['number']).columns[1]
        dataframe.plot.scatter(x=col1, y=col2)
        plt.title(f"Scatter plot of {col1} vs {col2}")

    elif visualization_type == "bar chart":
        col = dataframe.select_dtypes(exclude=['number']).columns[0]
        dataframe[col].value_counts().plot(kind='bar')
        plt.title(f"Bar chart of {col}")

    elif visualization_type == "boxplot":
        num_col = dataframe.select_dtypes(include=['number']).columns[0]
        cat_col = dataframe.select_dtypes(exclude=['number']).columns[0]
        dataframe.boxplot(column=num_col, by=cat_col)
        plt.title(f"Boxplot of {num_col} by {cat_col}")
    elif visualization_type == "pairplot":
        import seaborn as sns
        sns.pairplot(dataframe)
        plt.title("Pairplot")

    elif visualization_type == "generic plot":
        plt.plot(dataframe)  # Basic line plot as a fallback
        plt.title("Generic Plot")

    # Convert the plot to a PNG image in memory
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_png = img_buf.getvalue()
    img_b64 = base64.b64encode(img_png).decode()
    plt.close() # Close the plot to free memory

    return f'<img src="data:image/png;base64,{img_b64}" alt="Visualization Draft">'


# LangChain setup via github AI models
llm = OpenAI(base_url=endpoint, temperature=0, api_key=token, model=model_name)  # You MUST set your OpenAI key!
tools = [
    Tool(
        name="SuggestVisualization",
        func=suggest_visualization,
        description="Suggests an appropriate visualization type based on the provided DataFrame.",
    ),
    Tool(
        name="GenerateVisualizationDraft",
        func=generate_visualization_draft,
        description="Generates a draft visualization using Matplotlib. Input can be the summary stats of the dataset. Choose wisely",
    ),
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Example usage (replace with your data loading):
try:
    df = pd.read_csv("../intake/data/TWLO_stock.csv")  # Replace with your CSV file.
    result = agent.run(f"Given this dataset (represented as a Pandas DataFrame), suggest and generate a draft visualization: {df.to_string()}")
    print(result)
except FileNotFoundError:
    print("Error: dataset not found. Please provide a valid CSV file.")
except Exception as e:
    print(f"An error occurred: {e}")
