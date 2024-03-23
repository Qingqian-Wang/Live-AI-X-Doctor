from openai import OpenAI


def interact_once(user_input, messages):

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

  model="gpt-3.5-turbo"

  messages.append({"role": "user", "content": user_input})

  stream = client.chat.completions.create(
      model=model,
      messages=messages,
      stream=True,
  )

  content_without_newlines = ""
  # 假设 'stream' 是一个从GPT模型获得的流式响应对象
  for chunk in stream:
      if chunk.choices[0].delta.content is not None:
          # 去除内容中的换行符
          content_without_newlines += chunk.choices[0].delta.content.replace('\n', '')
  
  messages.append({"role":"assistant", "content": content_without_newlines})
  return content_without_newlines

