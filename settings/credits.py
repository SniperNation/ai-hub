from tkinter import Toplevel, Label, Button, font

# define theme colors
background_color = "#212121"
text_color = "white"
primary_color = "#6F42C1"  # Example accent color


def show_credits_window():
    credits_window = Toplevel()
    credits_window.title("Credits")
    credits_window.geometry("1000x200")
    credits_window.configure(bg=background_color)
    credits_label = Label(
        credits_window,
        text="This app was created by Aashay Ghodgaonkar, (C) 2024. AI Hub is FOSS and is not affiliated with OpenAI or Gemini.\n Icons from Google Fonts Material Icons."
        "\n ChatGPT is a registered trademark of OpenAI, and Gemini is a registered trademark of Google.\n All code is available on GitHub at https://github.com/snipernation/ai-hub.",
        bg=background_color,
        fg=text_color,
        font=font.Font(family="Google Sans"),
    )
    credits_label.pack(side="top", padx=10, pady=10)
    close_button = Button(
        credits_window,
        text="Exit",
        command=credits_window.destroy,
        bg=background_color,
        fg=text_color,
        font=font.Font(family="Google Sans", size=10),
    )
    close_button.pack(padx=10, pady=10, side="bottom")
