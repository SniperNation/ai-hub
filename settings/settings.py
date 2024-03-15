# This file contains the code for the settings window, which is opened when the user clicks the "Settings" button in the main window.
from .change_api_key import open_api_key_window
from tkinter import Button, Toplevel, font
from .credits import show_credits_window

background_color = "#212121"
text_color = "white"
primary_color = "#6F42C1"  # Example accent color


def open_settings_window():
    settings_window = Toplevel()
    settings_window.title("Settings")
    settings_window.geometry("300x200")
    settings_window.configure(bg=background_color)

    change_api_key_button = Button(
        settings_window,
        text="Change API Key",
        command=open_api_key_window,
        bg=background_color,
        fg=text_color,
        font=font.Font(family="Google Sans"),
        activebackground=background_color,
    )
    change_api_key_button.pack(pady=10)

    credits_button = Button(
        settings_window,
        text="Credits",
        command=show_credits_window,
        bg=background_color,
        fg=text_color,
        font=font.Font(family="Google Sans"),
        activebackground=background_color,
    )
    credits_button.pack(pady=10)
