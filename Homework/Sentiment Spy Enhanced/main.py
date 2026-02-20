import itertools
import time
import sys
import re
import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

conversation_history = []
report = {
    "positive": 0,
    "negative": 0,
    "neutral": 0
}

def show_loading_animation(loading: bool):
    spinner = itertools.cycle(["🕛", "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚"])
    while loading:
        sys.stdout.write("\rLoading.... " + next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)

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
    username = input(f"{Fore.CYAN}Enter your name: {Fore.YELLOW}{Style.RESET_ALL}")

    if re.search(r"[^a-zA-Z ]", username):
        print(f"{Fore.RED} Sorry! The username cannot contain special characters and numbers")
        get_valid_username()
    else:
        print(f"{Fore.CYAN}Name verified!")
    
    return username

def execute_command(command: str):
    if command.lower() == "help":
        print(f"{Fore.CYAN}All available commands{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}help -{Fore.YELLOW}lists all available commands{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}summary -{Fore.YELLOW}creates a file of summary of positive, negative and neutral sentiment{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}history -{Fore.YELLOW}lists all previous messages and their sentinels{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}reset -{Fore.YELLOW}clears all previous messages and their sentinels{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}exit -{Fore.YELLOW}exits the terminal{Style.RESET_ALL}")
    elif command.lower() == "history":
        for index, (polarity, type, emoji, color, text) in enumerate(conversation_history, start=1):
            print(f"{index}. {color}Text - {text}, Sentiment Mode - {type}{emoji}, Polarity - {polarity}")
    elif command.lower == "reset":
        conversation_history.clear()
        
        print("")