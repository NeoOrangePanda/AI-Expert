print("Hello I'm an AI bot! What is your name?")

name = input()

print(f"Nice to meet you, {name}!")
print("How are you feeling today? (good/bad)")

feeling = input().lower()

if feeling == 'good':
    print("I'm very glad to hear that you are good.")
elif feeling == 'bad':
    print("I'm sorry to hear that you are not well. I hope things get better soon.")
else:
    print("I know, maybe some feelings cannot be explained in words.")

print("Okay, see you soon, bye!")