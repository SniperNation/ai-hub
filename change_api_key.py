from tkinter import Toplevel, Label, Entry, Button
from configparser import ConfigParser

background_color = "#212121"
text_color = "white"
primary_color = "#6F42C1"  # Example accent color


def change_api_key(model, entry):
    config = ConfigParser()
    config.read('config.ini')
    new_api_key = entry.get()
    if model == "gpt":
        config.set('gpt', 'GPT_3_API_KEY', new_api_key)
    elif model == "gemini-pro":
        config.set('gemini', 'GEMINI_API_KEY', new_api_key)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def open_api_key_window(font):
    api_key_window = Toplevel(bg=background_color)
    api_key_window.title("Change API Key")
    api_key_window.geometry("300x200")

    gpt_label = Label(api_key_window, text="ChatGPT API Key:", bg=background_color, fg=text_color,
                      font=font.Font(family="Google Sans"))
    gpt_label.pack()
    gpt_entry = Entry(api_key_window, bg=background_color, fg=text_color, insertbackground=text_color,
                      font=font.Font(family="Google Sans"))
    gpt_entry.pack()
    gpt_button = Button(api_key_window, text="Change ChatGPT API Key", command=lambda: change_api_key("gpt", gpt_entry),
                        bg=background_color, fg=text_color, font=font.Font(family="Google Sans", size=10))
    gpt_button.pack(padx=10, pady=10)

    gemini_label = Label(api_key_window, text="Gemini API Key:", bg=background_color, fg=text_color,
                         font=font.Font(family="Google Sans"))
    gemini_label.pack()
    gemini_entry = Entry(api_key_window, bg=background_color, fg=text_color, insertbackground=text_color,
                         font=font.Font(family="Google Sans"))
    gemini_entry.pack()
    gemini_button = Button(api_key_window, text="Change Gemini API Key",
                           command=lambda: change_api_key("gemini-pro", gemini_entry), bg=background_color,
                           fg=text_color, font=font.Font(family="Google Sans", size=10))
    gemini_button.pack(padx=10, pady=10)


def create_change_api_key_button(root, open_api_key_window, font):
    change_api_key_button = Button(root, text="Change API Key", command=lambda: open_api_key_window(font),
                                   bg=background_color, fg=text_color, font=font.Font(family="Google Sans"))
    return change_api_key_button
