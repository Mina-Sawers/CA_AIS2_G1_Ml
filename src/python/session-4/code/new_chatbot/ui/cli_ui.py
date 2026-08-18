from core.model import get_response
def main_bot():
    print("chatbot: Hi How can I help you?")
    while True:
        user_input = input("User: ").lower()
        response = get_response(user_input)
        print("chatbot: ",response)

        if "goodbye" in user_input:
            break