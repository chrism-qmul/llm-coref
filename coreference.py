from openai import OpenAI

    
gpt4 = OpenAI(
    api_key="...",
)

llama2 = OpenAI(
    api_key="not_required",
    base_url="...",
)

client = gpt4

def coreference(sentence):
    messages = [{
       "role": "system",
       "content": "You are a coreference resolution system. Identify the mentions and link them",
    },{   
        "role": "user",
        "content": "A wolf had been gourging on an animal he had killed."
    },{   
        "role": "assistant",
        "content": "[A wolf]#1 had been gourging on [an animal [he]#1 had killed]#2."
    },{   
        "role": "user",
        "content": "Bob was hungry. It was late, but he went to the shops, and brought some bread."
    },{   
        "role": "assistant",
        "content": "[Bob]#1 was hungry. It was late, but [he]#1 went to [the shops]#2, and brought [some bread]#3."
    },{   
        "role": "user",
        "content": sentence},
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4"
    )   
    return chat_completion.choices[0].message.content

print(coreference("The music was so loud, it couldn't be enjoyed."))
print(coreference("There was lots of traffic on the very busy road. It took a long time for Geoff to navigate through it and reach his home."))
