from flask import Flask, request, render_template, Response
import time
app = Flask(__name__)

def generate_stream_data(user_input):
    # 这里模拟根据用户输入生成回应的过程
    for i in range(3):  # 假设生成3条回应
        yield f"data: Response {i} to {user_input}\n\n"
        time.sleep(1)

@app.route('/')
def index():
    # 渲染带有聊天框的HTML页面
    return render_template('chat.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['message']
    # 返回一个流式响应
    return Response(generate_stream_data(user_input), mimetype='text/event-stream')
