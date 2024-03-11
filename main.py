# Import libraries
from tkinter import Tk, Entry, Text, Button, END, PhotoImage, font, Frame, Radiobutton, StringVar
import os
import config
from get_gemini_pro import get_gemini_pro_response
from get_gpt_3 import get_gpt3_response

background_color = "#212121"
text_color = "white"
primary_color = "#6F42C1"  # Example accent color

# Set the API key and the model ID
os.environ["GENAI_API_KEY"] = config.GEMINI_API_KEY
# Define the chatbot window
window = Tk()
window.title("AI Hub")
window.geometry("1280x720")
window.configure(bg=background_color)
# Create a frame for the sidebar
sidebar = Frame(window, width=260, height=605, bg="#36373B")  # Adjust width and height as needed
sidebar.grid(row=0,column=2, padx=10, pady=10)

ai_options = ["ChatGPT", "Gemini"]  # List of AI options
ai_models = {"ChatGPT": "gpt","Gemini": "gemini-pro"}  # Model IDs for each option (replace with actual IDs)
current_ai = "gemini-pro"  # Default AI model (should match a key in ai_models)
# Function to change the AI model
def change_ai(selected_ai):
  global current_ai  # Access global variable for current AI
  current_ai = ai_models[selected_ai]
  chat_history.insert(END,f"Switched to AI: {current_ai}\n")  # Update for debugging (replace with your logic to handle AI change)
# Radio button variable to track selection
selected_ai_var = StringVar(value=current_ai)  # Pre-select default AI
row_index = 0  # Track the row index for radio buttons
for option in ai_options:
  radio_button = Radiobutton(sidebar, text=option, variable=selected_ai_var, value=ai_models[option], command=lambda ai=option: change_ai(ai),bg=background_color, fg=text_color, selectcolor=primary_color, activebackground=background_color, activeforeground=text_color, font=font.Font(family="Google Sans"), width=25, anchor="n")
  radio_button.grid(row = row_index, padx=5, pady=5)  # Use pack for radio buttons within the frame
  row_index += 1  # Increment the row index for the next radio button
# ... rest of your code for sidebar content ...


# Create an entry field for user input
user_input = Entry(window, width=93, font=font.Font(family="Google Sans"),bg=background_color, fg=text_color, insertbackground=text_color)
user_input.grid(row=1, column=0, padx=10, pady=10)
placeholder_text = "Enter your prompt here"
def clear_placeholder(e):
  if user_input.get() == placeholder_text:
    user_input.delete(0, END)
  else:
    # Re-insert placeholder if empty on focus out
    if not user_input.get() and e.type == "<Leave>":
      user_input.configure(state="normal", foreground="black")  # Set to black on focus out
      user_input.insert(0, placeholder_text)
      user_input.configure(state="disabled", foreground="gray")  # Disable placeholder

  # Always enable input for typing (moved outside the else block)
  user_input.configure(state="normal", foreground=text_color)

user_input.bind("<FocusIn>", clear_placeholder)
user_input.bind("<Key>", clear_placeholder)  # Bind to any key press
user_input.bind("<Leave>", clear_placeholder)  # Add binding for leaving the entry
# Initial configuration for placeholder
if not user_input.get():
  user_input.insert(0, placeholder_text)
  #user_input.configure(state="disabled", foreground="gray")  # Disable placeholder text


# Create a text box to display conversation history
chat_history = Text(window, height=30, width=97, font=font.Font(family="Google Sans"), bg=background_color, fg=text_color)
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
chat_history.insert(END, "Welcome! How can I help you today?\n")

# Function to process user input (replace with your AI logic)
def send_message(current_ai):
  user_message = user_input.get()
  chat_history.insert(END, f"You: {user_message}\n")
  user_input.delete(0, 'end')  # Clear user input field

  # Access the API key from the environment variable
  api_key = os.environ.get('GENAI_API_KEY')

  # Check if API key is set
  if not api_key:
    print("Error: API key not found in environment variable.")
    chat_history.insert(END, "Error: API key not found.\n")
    return  # Exit the function if key is not found
  if current_ai == "gemini-pro":
    gemini_response = get_gemini_pro_response(user_message)  # Call the function to get Gemini response
    chat_history.insert(END, f"Bot (Gemini): {gemini_response}\n")
  elif current_ai == "gpt":
    gpt3_response = get_gpt3_response(user_message)  # Call the function to get GPT-3 response
    chat_history.insert(END, f"Bot (GPT-3): {gpt3_response}\n")
  else:
    print(f"Error: Unknown AI model: {current_ai}")
    chat_history.insert(END, f"Error: AI model not supported.\n")


# Create a send button to trigger processing
send_icon = PhotoImage(file="send_icon.png")
send_button = Button(window, image=send_icon, command=lambda: send_message(current_ai), borderwidth=0, bg=background_color)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the main event loop
window.mainloop()
