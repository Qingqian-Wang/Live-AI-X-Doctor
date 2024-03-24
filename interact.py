from openai import OpenAI
import re

def interact_once(user_input, messages, save_user = True, number_only = False):
    client = OpenAI()

    if not messages:
        # read log file
        with open('log.txt', 'r') as file:
            for line in file:
                # separate role and content
                parts = line.split(": ", 1)  #  split at the first colon
                if len(parts) == 2:
                    # add to messages
                    messages.append({"role": parts[0].strip(), "content": parts[1].strip()})

    model = "gpt-3.5-turbo"

    
    messages.append({"role": "user", "content": user_input})

    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    
    if not save_user:
        messages.pop()

    

    content_without_newlines = ""
    # get the content of the last message
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            # remove newlines
            content_without_newlines += chunk.choices[0].delta.content.replace('\n', '')



    if not number_only:
        messages.append({"role": "assistant", "content": content_without_newlines})

    match = re.search(r'\d+', content_without_newlines)
    if(number_only):
        if match:
            first_number = match.group(0)
            return first_number  # return the first number found
        else:
            return 85

    return content_without_newlines
