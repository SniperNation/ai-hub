import configparser


def change_theme(new_theme):
    # Create a ConfigParser instance
    config = configparser.ConfigParser()

    # Read the preferences.ini file
    config.read("preferences.ini")

    # Update the theme value
    config.set("Preferences", "theme", new_theme)

    # Write the changes back to the preferences.ini file
    with open("preferences.ini", "w") as configfile:
        config.write(configfile)
