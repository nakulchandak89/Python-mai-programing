import os
import openai

# Get the API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Use the API key in your code
print(f"Using API key: {api_key}")

# Set the API key for the OpenAI library
openai.api_key = api_key

# Function to get GPT response
def get_gpt_response(message, max_tokens=200):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"

# Single prompt for testing
test_prompt = "Hello! What is Python?"
response = get_gpt_response(test_prompt)
print(f"Response: {response}")