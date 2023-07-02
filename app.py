import openai
import gradio
from dotenv import load_dotenv
from os import environ

load_dotenv()
environ.get('openai.api_key')

messages = [{"role": "system", "content": "You are a cool sasy travel guide chatbot, which gives information of the user's destination and includes information like popular attractions, historical sites, local culture, transportation options, and more.concise descriptions, interesting facts, and even share images or videos to give users a better understanding of each location. "}]

def travel_guide(enter_your_destination):
    messages.append({"role": "user", "content": f"I wish to travel to {enter_your_destination}, give me information about it."})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    response = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": response})
    return response

demo = gradio.Interface(fn=travel_guide, inputs = "text", outputs = "text", title = "Your cool Travel Guide 😎")

demo.launch(share=True)
