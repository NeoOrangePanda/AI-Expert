import sys
import re
import colorama
from colorama import Fore
from textblob import TextBlob

colorama.init(autoreset=True)

conversation_history = []

positive = 0
negative = 0
neutral = 0

def analyze_sentiment(text: str):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        emoji = "😊"
        text_color = Fore.GREEN
    elif polarity < -0.25:
        sentiment_type = "Negative"
        emoji = "😞"
        text_color = Fore.RED
    else:
        sentiment_type = "Neutral"
        emoji = "😐"
        text_color = Fore.YELLOW

    return polarity, sentiment_type, emoji, text_color, text

def get_valid_username():
    username = input(Fore.CYAN + "Enter your name: ")

    if username:
        if re.search(r"[^a-zA-Z ]", username):
            print(Fore.LIGHTRED_EX + "Sorry! The username cannot contain special characters and numbers")
            return get_valid_username()
        else:
            print(Fore.CYAN + "Name verified!")
            return username
    else:
        print(Fore.LIGHTRED_EX + "Sorry, cannot take blank names!")
        return get_valid_username()

def execute_command(command: str):
    global positive, negative, neutral
    if command.lower() == "help":
        print(f"{Fore.CYAN}All available commands")
        print(f"{Fore.MAGENTA}help- {Fore.YELLOW}lists all available commands")
        print(f"{Fore.MAGENTA}summary- {Fore.YELLOW}creates a file of summary of positive, negative and neutral sentiment")
        print(f"{Fore.MAGENTA}history- {Fore.YELLOW}lists all previous messages and their sentinels")
        print(f"{Fore.MAGENTA}reset- {Fore.YELLOW}clears all previous messages and their sentinels")
        print(f"{Fore.MAGENTA}exit- {Fore.YELLOW}exits the terminal")
    elif command.lower() == "history":
        for index, (polarity, type, emoji, color, text) in enumerate(conversation_history, start=1):
            print(f"{index}. {color}Text - {text}, Sentiment Mode - {type}{emoji}, Polarity - {polarity}")
    elif command.lower() == "reset":
        conversation_history.clear()
        positive = 0
        negative = 0
        neutral = 0
        print(f"{Fore.MAGENTA}All conversations cleared!")
    elif command.lower() == "summary":
        file_name = input(f"{Fore.CYAN}Your report file name: ")
        final_report = ['Mission Report:', f'Positive Texts: {positive}', f'Negative Texts: {negative}', f'Neutral Texts: {neutral}']
        with open(f"{file_name}.txt", "w") as f:
            for i in final_report:
                f.write(i + '\n')

    elif command.lower() == "exit":
        print(f"{Fore.LIGHTYELLOW_EX}Bye! Have a great day! 😊")
        sys.exit()
    else:
        s = analyze_sentiment(command)
        print(f"{Fore.CYAN}Sentiment Type - {s[3]}{s[1]} {s[2]}{Fore.CYAN}, Polarity - {s[0]}")
        conversation_history.append((s))
        if s[1] == 'Positive': positive += 1
        elif s[1] == 'Negative': negative += 1
        else: neutral += 1

def chatbot():
    print(f"{Fore.LIGHTYELLOW_EX}🐍 Welcome to Sentiment Spy! What is your name? 🐍")
    name = get_valid_username()

    print(f"{Fore.CYAN}Hello, {name}! Nice to meet you!")
    print(f"{Fore.CYAN}Type your sentence for polarity calculation.")
    print(f"{Fore.CYAN}To execute any command, type {Fore.LIGHTYELLOW_EX}help, reset, summary or history")
    print(f"{Fore.CYAN}Type {Fore.RED}exit{Fore.CYAN} to end the program.")

    while True:
        user_input = input(f"{Fore.LIGHTYELLOW_EX}>>> ").strip()

        if user_input: execute_command(user_input)
        else: continue

if __name__ == "__main__":
    chatbot()