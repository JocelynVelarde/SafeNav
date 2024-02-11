from api_keys import OPENAI_API_KEY, ASSISTANT_ID
from openai import OpenAI
from gsheet_auth import gsheet_auth
import time

# Data retrieval from Google Sheets
auth = gsheet_auth()
sheet = auth.open('Streamlit SafeNav').worksheet('Hoja 1')
#prompt = sheet.acell('A1').value
#print(prompt)

def set_api_key():
  client = OpenAI(api_key=OPENAI_API_KEY)
  return client

def ask_gpt(prompt):
    try:
        # Assistant initialization
        myAssist = set_api_key().beta.assistants.retrieve(ASSISTANT_ID)
        assistant_id = myAssist.id
        print(assistant_id)

        # Assistant interaction with new message thread
        message = set_api_key().beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=prompt
        )

        run = set_api_key().beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id
        )

        complete = False
        while(not complete):
            run = set_api_key().beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
 
            if(run.status == "completed"):
                complete = True
            else:
                time.sleep(5)
 
        messages = set_api_key().beta.threads.messages.list(
            thread_id=thread.id
        )
        response = messages.data[0].content[0].text.value
        print(response)
        return response
 
    except Exception as e:
        return f"An error occurred: {str(e)}"
 

thread = set_api_key().beta.threads.create() 







