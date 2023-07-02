{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db57d8f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import openai\n",
    "import gradio\n",
    "from dotenv import load_dotenv\n",
    "from os import environ\n",
    "\n",
    "load_dotenv()\n",
    "environ.get('openai.api_key')\n",
    "\n",
    "messages = [{\"role\": \"system\", \"content\": \"You are a cool sasy travel guide chatbot, which gives information of the user's destination and includes information like popular attractions, historical sites, local culture, transportation options, and more.concise descriptions, interesting facts, and even share images or videos to give users a better understanding of each location. \"}]\n",
    "\n",
    "def travel_guide(enter_your_destination):\n",
    "    messages.append({\"role\": \"user\", \"content\": f\"I wish to travel to {enter_your_destination}, give me information about it.\"})\n",
    "    response = openai.ChatCompletion.create(\n",
    "        model = \"gpt-3.5-turbo\",\n",
    "        messages = messages\n",
    "    )\n",
    "    response = response[\"choices\"][0][\"message\"][\"content\"]\n",
    "    messages.append({\"role\": \"assistant\", \"content\": response})\n",
    "    return response\n",
    "\n",
    "demo = gradio.Interface(fn=travel_guide, inputs = \"text\", outputs = \"text\", title = \"Your cool Travel Guide 😎\")\n",
    "\n",
    "demo.launch(share=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
