from openai import OpenAI
import re

def interact_once(user_input, messages, save_user = True, number_only = False):
    client = OpenAI()

    if not messages:
        # 打开日志文件并逐行读取
        with open('log.txt', 'r') as file:
            for line in file:
                # 根据日志格式分割角色和内容
                parts = line.split(": ", 1)  # 最多分割成两部分
                if len(parts) == 2:
                    # 构造字典并添加到列表
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
    # 假设 'stream' 是一个从GPT模型获得的流式响应对象
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            # 去除内容中的换行符
            content_without_newlines += chunk.choices[0].delta.content.replace('\n', '')



    if not number_only:
        messages.append({"role": "assistant", "content": content_without_newlines})

    match = re.search(r'\d+', content_without_newlines)
    if(number_only):
        if match:
            first_number = match.group(0)
            return first_number  # 输出: 12345
        else:
            return 85

    return content_without_newlines
