import random
import json
import os


with open(r'c:\Users\Clown\Desktop\CA-S2-G1-AI\CA_AIS2_G1_Ml\src\python\session-4\code\new_chatbot\core\data.json', "r") as file:
     responses = json.load(file)
    

def get_response(user_input: str) -> str:
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])