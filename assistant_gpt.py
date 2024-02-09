import openai
api_key = openai.api_key = "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"
 
import time
from openai import OpenAI

client = OpenAI(
    api_key =  api_key
)


# step1: upload file 
file = client.files.create(
    file = open("dataa.txt", "rb"), 
    purpose = 'assistants'
)


file_list = client.files.list()


# step2: create the assistants with the file 
assistant = client.beta.assistants.create( 
    instructions= 'You are going to be given a natural language prompt with a desired initial point and final destination point. Your job is to search in a .txt file this names and provide as a result the corresponding node number as (#, #)', 
    model = 'gpt-4-1106-preview', 
    tools=[{"type":"retrieval"}], 
    file_ids = [file.id]
)

# step3: create a thread 
thread = client.beta.threads.create(
    
)
# step4: add more message to the thread 
message = client.beta.threads.messages.create(
    thread_id = thread.id, 
    role = 'user', 
    content = 'can you tell me how to go from coapa to churubusco?'
) 

# step5: run the assitant to get the response 
run = client.beta.threads.runs.create(
    thread_id = thread.id, 
    assistant_id= assistant.id, 
    instructions = "please give the answer in format (#, #)"

)

# step6: retrieve the run status 
print(run.status)
while run.status not in ["completed", "failed"]:
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id, 
        run_id = run.id
    )
    print(run.status)
    time.sleep(10)
    
    
# step7: 
messages = client.beta.threads.messages.list(
    thread_id=thread.id
) 

for m in messages: 
    print(m.role + ":" + m.content[0].text.value) 
    print("============================")