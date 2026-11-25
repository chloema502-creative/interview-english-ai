print("Welcome to Interview English AI!")
Name=input("What is your name?")
Job=input("What job are you applying for?")
print(f"Hello {Name}!")
print(f"Let's prepare for your {Job} interview!")

answer=input("Tell me about yourself:")
length=len(answer)
if length >= 30:
    print("Good start!")
else:
    print("Too short!")
