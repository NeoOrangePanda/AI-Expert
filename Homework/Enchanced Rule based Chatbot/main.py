import re, random
import requests
from colorama import Fore, init

init(autoreset=True)

API_WEATHER = 'c1b22a5179bd6fe28ca3bc6883d4684b'

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket", "Cox's Bazar", "Langkawi", "Copacabana", "Grace Bay"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Matterhorn", "Mount Fuji", "Mount Kilimanjaro"],
    "cities": ["Tokyo", "Paris", "New York", "Bangkok", "London", "Kuala Lumpur", "Hong Kong", "Istanbul", "Dubai"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it has virus!",
    "Why do travellers always feels hot? Because of all their hot spots!",
    "Why did the salamander go to Hollywood? To make newt movies!",
    "What do you do when your puppy isn't feeling well? Go to Dog-tor!",
    "What did 20 do when it was hungry? Twenty-eight.",
    "Why is grass so dangerous? Because it's full of blades!"
    "Why did the crab cross the road? It didn’t—it used the sidewalk",
    "Why can't you make a dinosaur omelet? Because they're egg-stinct!"
]

def normalize_input(text: str):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains or cities?")
    preference = normalize_input(input(Fore.YELLOW + "You: "))

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another!")
            recommend()
        else:
            print(Fore.RED + "I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
        recommend()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes")
    print(Fore.GREEN + "- Don't overpack!")
    print(Fore.GREEN + "- Bring chargers/adapters")
    print(Fore.GREEN + "- Check the weather forecast")
    print(Fore.GREEN + "- Keep copies of important documents")
    print(Fore.GREEN + "- Stay hydrated")
    print(Fore.GREEN + "- Pack souvenirs carefully")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommend')")
    print(Fore.GREEN + "- Offer packing trips (say 'packing')")
    print(Fore.GREEN + "- Weather Forecast info (say 'weather')")
    print(Fore.GREEN + "- Know local time of a location (say 'time')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def weather_forecast():
    days = input(Fore.YELLOW + "You: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}")

    show_help()

    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))

        if "recommend" in user_input or "suggest" in user_input: recommend()
        elif "pack" in user_input or "packing" in user_input: packing_tips()
        elif "joke" in user_input or "funny" in user_input: tell_joke()
        elif "help" in user_input: show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else: print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()