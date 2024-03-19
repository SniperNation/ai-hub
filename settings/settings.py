# This file contains the code for the settings window, which is opened when the user clicks the "Settings" button in the main window.
from .change_api_key import open_api_key_window
from tkinter import Button, Toplevel, font, OptionMenu, StringVar
from .credits import show_credits_window
import configparser
from .switch_theme import change_theme

config = configparser.ConfigParser()
config.read("preferences.ini")
theme = config.get("Preferences", "theme").strip('"')
if theme == "dark":
    background_color = config.get("Preferences", "background_color").strip('"')
    text_color = config.get("Preferences", "text_color").strip('"')
    primary_color = config.get("Preferences", "primary_color").strip('"')
elif theme == "light":
    background_color = config.get("Preferences", "light_background_color").strip('"')
    text_color = config.get("Preferences", "light_text_color").strip('"')
    primary_color = config.get("Preferences", "light_primary_color").strip('"')


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

    # Create a StringVar instance for the dropdown menu
    theme_var = StringVar()
    theme_var.set(theme)  # Set the initial value to the current theme

    # Create a list of options for the dropdown menu
    theme_options = ["light", "dark"]

    # Create the dropdown menu
    theme_menu = OptionMenu(
        settings_window,
        theme_var,
        *theme_options,
    )
    theme_menu.config(
        bg=background_color,
        fg=text_color,
        font=font.Font(family="Google Sans"),
        activeforeground=text_color,
        activebackground=background_color,
    )
    theme_menu.pack(pady=10)  # Add the dropdown menu to the settings window

    # Call the change_theme function whenever the selection changes
    def on_theme_change(*args):
        new_theme = theme_var.get()
        change_theme(new_theme)

    theme_var.trace("w", on_theme_change)
