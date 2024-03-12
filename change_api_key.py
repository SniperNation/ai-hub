# Change API key in the config file
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
model = input("Enter the model name (gpt or gemini-pro): ")
if model == "gpt":
    print("You have chosen GPT-3.")
    print("Current api key: ", config['gpt']['GPT_3_API_KEY'])
    gpt_api_key = input("Please enter the api key you'd like to set >>> ")
    config.set('gpt', 'GPT_3_API_KEY', gpt_api_key)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
elif model == "gemini-pro":
    print("You have chosen Gemini Pro.")
    print("Current api key: ", config['gemini']['GEMINI_API_KEY'])
    gemini_api_key = input("Please enter the api key you'd like to set >>>")
    config.set('gemini', 'GEMINI_API_KEY', gemini_api_key)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
else:
    print("Invalid model name. Please enter 'gpt' or 'gemini-pro'.")

    pass