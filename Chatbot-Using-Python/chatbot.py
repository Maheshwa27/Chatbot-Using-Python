import datetime
import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return random.choice([
            "Hello! 😊",
            "Hi there! 👋",
            "Hey! How can I help you?"
        ])

    # Name
    elif "your name" in user_input:
        return "I am a Smart Python Chatbot 🤖 (Mini ChatGPT)"

    # Creator
    elif "who created you" in user_input or "who made you" in user_input:
        return "I was created using Python as an internship project 😄"

    # Date
    elif "date" in user_input:
        today = datetime.date.today()
        return f"Today's date is {today}"

    # Time
    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current time is {now}"

    # Help
    elif "help" in user_input:
        return (
            "I can help you with:\n"
            "- Greetings\n"
            "- Date & Time\n"
            "- Simple math\n"
            "- Basic questions\n"
            "- Exit the chat"
        )

    # Simple math (addition)
    elif "+" in user_input:
        try:
            nums = user_input.split("+")
            result = int(nums[0]) + int(nums[1])
            return f"Answer is {result}"
        except:
            return "Please enter like this: 5 + 3"

    # Simple math (subtraction)
    elif "-" in user_input:
        try:
            nums = user_input.split("-")
            result = int(nums[0]) - int(nums[1])
            return f"Answer is {result}"
        except:
            return "Please enter like this: 10 - 3"

    # Internship related
    elif "internship" in user_input:
        return "Internships help you gain real-world experience and skills "

    # Python related
    elif "python" in user_input:
        return "Python is a powerful and beginner-friendly programming language "

    # Exit
    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        return "Bye 👋 Have a great day!"

    # Default fallback
    else:
        return random.choice([
            "Hmm 🤔 I am still learning.",
            "Can you rephrase that?",
            "Sorry, I didn't understand that."
        ])


print("🤖 Smart Chatbot Started")
print("Type 'help' to see what I can do")
print("Type 'bye' to exit\n")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)

    if any(word in user_input.lower() for word in ["bye", "exit", "quit"]):
        break
