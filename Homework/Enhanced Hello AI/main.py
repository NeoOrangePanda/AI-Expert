import random
import re

def name_selection():
    print('Keep a name for your chatbot (cannot contain special characters, numbers and spaces): ')
    chatbot_name = input()

    if re.search(r"[^a-zA-Z ]", chatbot_name):
        print("Sorry cannot take this name")
        name_selection()
    else:
        return chatbot_name

def chat(name):
    print(f"Hello! I'm {name}. What is your name?")
    print("(Cannot contain special characters, numbers and spaces)")
    username = input()

    if re.search(r"[^a-zA-Z ]", username):
        print('Sorry cannot take this name.....')
        print('-------------------------')
        chat(name)

    print(f'Nice to meet you, {username}! How are you feeling now? (good/bad)')
    feeling = input().lower()

    if feeling == 'good':
        print("I'm very glad to hear that you are good.")
    elif feeling == 'bad':
        print("I'm sorry to hear that you are not well. I hope things get better soon.")
    else:
        print("I know, maybe some feelings cannot be explained in words.")

    print(f'Now, what can I explain you about? (What is AI? [1]/What is computer? [2]/Why is AI important for our life? [3])')
    print("Input only the number beside!")
    answer_ques = input()

    if answer_ques == "1":
        print("""
--------------------------------------
What is AI?
      
Artificial Intelligence (AI) is the technology that allows machines and computers to think, learn, and make decisions like humans. It can analyze data, recognize patterns, and solve problems without human help. Examples include virtual assistants, recommendation systems, and self-driving cars. AI is not a real human brain but a way to simulate human intelligence using algorithms and data.
--------------------------------------
        """)
    
    elif answer_ques == "2":
        print("""
--------------------------------------
What is a computer?
              
A computer is an electronic machine that can store, process, and retrieve information. It can perform tasks like calculations, creating documents, running games, or browsing the internet. Computers follow instructions from software to complete tasks quickly and accurately. They are like a smart helper for humans in work, learning, and entertainment.
--------------------------------------
""")
    elif answer_ques == "3":
        print("""
--------------------------------------
Why is AI important for our life?
              
AI is important because it makes life faster, easier, and more efficient. It helps in healthcare by detecting diseases, in daily life through smart assistants, and in education by automating repetitive tasks. AI also helps humans make better decisions by analyzing data quickly. Overall, it improves the quality of life and reduces effort in many areas.
--------------------------------------
""")
    else:
        print("I cannot answer you this but anyways I'm moving on.")

    print(f"My favourite number is {random.randint(10, 100)}. What is yours?")

    while True:
        try:
            fav_num = int(input("Your favourite number: "))
            break
        except ValueError:
            print("Sorry, that's not an integer 😅")
    
    print('I like that also! Btw, my chatting limit is over. See you soon!')

chat(name_selection())