import google.generativeai as genai
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
GEMINI_API_KEY = config['gemini']['GEMINI_API_KEY']

def get_gemini_pro_response(user_message):
# Configure the API key
  api_key=GEMINI_API_KEY
  genai.configure(api_key=api_key)

  # ... rest of your code to generate response using Gemini ...

  # Define the model (choose 'gemini' or 'gemini-pro' based on your access)
  model = genai.GenerativeModel('gemini-pro')  # Example using free tier 'gemini'

  # Generate response using the model
  response = model.generate_content(user_message)
  bot_response = response.text.strip()  # Extract text from response

  return bot_response