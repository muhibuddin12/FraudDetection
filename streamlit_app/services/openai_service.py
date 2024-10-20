from pandasai.llm.openai import OpenAI
from pandasai import SmartDataframe
import pandas as pd
import os
from dotenv import load_dotenv
import openai

load_dotenv()

class PandasAIChatBot:
    def __init__(self, api_key=None):
        self.llm = OpenAI(api_token=api_key or os.getenv("OPENAI_API_KEY"))
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def chat_with_dataframe(self, data, question):
        df = pd.DataFrame(data)
        
        sdf = SmartDataframe(df, config={"llm": self.llm})
        
        response = sdf.chat(question)
        return response

    def chat_with_dataframe_to_analyse(self, dataframe: pd.DataFrame, prompt: str):
        """Send a DataFrame and a prompt to the OpenAI API for analysis."""
        
        # Convert the DataFrame to a string to be sent to the LLM
        data_str = dataframe.to_csv(index=False)
        
        # Combine the prompt and the DataFrame contents
        full_prompt = f"{prompt}\n\nHere is the data:\n{data_str}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the chat model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that can analyze data."},
                {"role": "user", "content": full_prompt}
            ],
            max_tokens=600,  # Adjust the number of tokens based on your needs
            temperature=0.7  # Adjust temperature for creativity
        )
        
        # Extract the text from the response
        response_text = response['choices'][0]['message']['content'].strip()
        
        return response_text