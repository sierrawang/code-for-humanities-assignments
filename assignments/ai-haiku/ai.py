from openai import OpenAI

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.api_keys import OPENAI_API_KEY

client = OpenAI(api_key = OPENAI_API_KEY)

def call_gpt(prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )
    return response.output_text