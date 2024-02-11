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
assistand_id = myAssist.id
print(assistand_id)

# Creation of assistant with file retrieval
file = openai.files.create(
  file=open("assets/files/input_gpt.txt", "rb"),
  purpose='assistants'
)

assistant = openai.beta.assistants.create(
  name="Prompt to index finder",
  description="You are going to be given a natural language prompt with a desired initial place and final destination place. Your job is to search in a .txt file this names and provide as a result the corresponding index number of the places in the format (#, #)",
  model="gpt-4-turbo-preview",
  tools=[{"type": "retrieval"}],
  file_ids=[file.id]
)

thread = openai.beta.threads.create()

message = openai.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=prompt
)



messages = openai.beta.threads.messages.list(
  thread_id=thread.id
)

print(messages)


'''# Easy way to test the model
response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are going to be given a natural language prompt with a desired initial place and final destination place. Your job is to search in a .pdf file this names and provide as a result the corresponding index number of the places in the format (#, #)"},
    {"role": "user", "content": prompt}
  ]
)

print(response.choices[0].message.content)'''


