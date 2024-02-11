from api_keys import OPENAI_API_KEY
from openai import OpenAI
from gsheet_auth import gsheet_auth
import openai
import time

auth = gsheet_auth()
sheet = auth.open('Streamlit SafeNav').worksheet('Hoja 1')
prompt = sheet.acell('A1').value
print(prompt)

client = OpenAI(api_key=OPENAI_API_KEY)
myAssist = client.beta.assistants.retrieve("asst_Mzkk7scg3aRzRVx8EFfzAmnr")
assistant_id = myAssist.id
print(assistant_id)

def ask_gpt(prompt):
    try:

        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input
        )

        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id
        )

        complete = False
        while(not complete):
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
 
            if(run.status == "completed"):
                complete = True
            else:
                time.sleep(5)
 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        return messages.data[0].content[0].text.value
 
    except Exception as e:
        return f"An error occurred: {str(e)}"
 

thread = client.beta.threads.create() 

print("Welcome! You can start chatting with the GPT Assistant. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting the conversation.")
        break
    else:
        response = ask_gpt(user_input)
        print(f"GPT Assistant: {response}")




