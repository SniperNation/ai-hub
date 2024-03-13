# Import libraries
import tkinter
from tkinter import Tk, Entry, Text, Button, END, PhotoImage, font, Frame, Radiobutton, StringVar

from change_api_key import open_api_key_window, create_change_api_key_button
from get_gemini_pro import get_gemini_pro_response
from get_gpt_3 import get_gpt3_response

background_color = "#212121"
text_color = "white"
primary_color = "#6F42C1"  # Example accent color
# Set the API key and the model ID
# Define the chatbot window
root = Tk()
root.title("AI Hub")
root.geometry("1280x720")
root.configure(bg=background_color)
# Create a frame for the sidebar
sidebar = Frame(root, width=260, height=605, bg="#36373B")  # Adjust width and height as needed
sidebar.grid(row=0,column=2, padx=10, pady=10)

ai_options = ["ChatGPT", "Gemini"]  # List of AI options
ai_models = {"ChatGPT": "gpt","Gemini": "gemini-pro"}  # Model IDs for each option (replace with actual IDs)
current_ai = "gemini-pro"  # Default AI model (should match a key in ai_models)
# Function to change the AI model

# Create a text box to display conversation history
chat_history = Text(root, height=30, width=97, font=font.Font(family="Google Sans"), bg=background_color, fg=text_color, state="disabled")
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
chat_history.config(state="normal")
chat_history.insert(END, "Welcome! How can I help you today?\n")
chat_history.config(state="disabled")


def change_ai(selected_ai):
  global current_ai  # Access global variable for current AI
  current_ai = ai_models[selected_ai]
  chat_history.config(state="normal")
  chat_history.insert(END,f"Switched to AI: {current_ai}\n")  # Update for debugging (replace with your logic to handle AI change)
  chat_history.config(state="disabled")
# Radio button variable to track selection
selected_ai_var = StringVar(value=current_ai)  # Pre-select default AI
row_index = 0  # Track the row index for radio buttons
for option in ai_options:
  radio_button = Radiobutton(sidebar, text=option, variable=selected_ai_var, value=ai_models[option], command=lambda ai=option: change_ai(ai),bg=background_color, fg=text_color, selectcolor=primary_color, activebackground=background_color, activeforeground=text_color, font=font.Font(family="Google Sans"), width=25, anchor="n")
  radio_button.grid(row = row_index, padx=5, pady=5)  # Use pack for radio buttons within the frame
  row_index += 1  # Increment the row index for the next radio button
# ... rest of your code for sidebar content ...


# Create an entry field for user input
user_input = Entry(root, width=93, font=font.Font(family="Google Sans"),bg=background_color, fg="gray", insertbackground=text_color)
user_input.grid(row=1, column=0, padx=10, pady=10)

# Remove the default text when the user clicks on the entry field
def on_entry_click(event):
  if user_input.get() == "Type your message...":
    user_input.delete(0, tkinter.END)
    user_input.configure(foreground=text_color)

# Add the placeholder text
def on_focus_out(event):
  if user_input.get() == "":
    user_input.insert(0, "Type your message...")
    user_input.configure(foreground="gray")

user_input.insert(0, "Type your message...")

user_input.bind("<FocusIn>", on_entry_click)
user_input.bind("<FocusOut>", on_focus_out)



# Function to process user input (replace with your AI logic)
def send_message(current_ai):
  user_message = user_input.get()
  chat_history.config(state="normal")
  chat_history.insert(END, f"You: {user_message}\n")
  chat_history.config(state="disabled")
  user_input.delete(0, 'end')  # Clear user input field

  if current_ai == "gemini-pro":
    gemini_response = get_gemini_pro_response(user_message)  # Call the function to get Gemini response
    chat_history.config(state="normal")
    chat_history.insert(END, f"Bot (Gemini): {gemini_response}\n")
    chat_history.config(state="disabled")
  elif current_ai == "gpt":
    gpt3_response = get_gpt3_response(user_message)  # Call the function to get GPT-3 response
    chat_history.config(state="normal")
    chat_history.insert(END, f"Bot (GPT-3): {gpt3_response}\n")
    chat_history.config(state="disabled")
  else:
    print(f"Error: Unknown AI model: {current_ai}")
    chat_history.config(state="normal")
    chat_history.insert(END, f"Error: AI model not supported.\n")
    chat_history.config(state="disabled")

# Create a button to trigget the command window to change the API key
change_api_key_button = create_change_api_key_button(root, open_api_key_window, font)
change_api_key_button.grid(row=1, column=2, padx=10, pady=10)
# Create a send button to trigger processing
send_icon = PhotoImage(file="send_icon.png")
send_button = Button(root, image=send_icon, command=lambda: send_message(current_ai), borderwidth=0, bg=background_color)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()
