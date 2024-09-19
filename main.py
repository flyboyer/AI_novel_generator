from flask import Flask, render_template, request, Response, stream_with_context, jsonify
import requests
import json
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def get_available_models():
    try:
        response = requests.get('http://localhost:11434/api/tags')
        response.raise_for_status()
        models = response.json()['models']
        return [model['name'] for model in models]
    except Exception as e:
        app.logger.error(f"获取模型列表时发生错误：{str(e)}")
        return []

@app.route('/models')
def models():
    return jsonify(get_available_models())

@app.route('/', methods=['GET', 'POST'])
def generate_novel():
    if request.method == 'POST':
        theme = request.form['theme']
        model = request.form['model']
        app.logger.info(f"收到主题：{theme}，使用模型：{model}")
        
        def generate():
            try:
                response = requests.post('http://localhost:11434/api/generate', 
                    json={
                        "model": model,
                        "prompt": f"根据以下主题写一篇短篇小说：{theme}",
                        "stream": True
                    },
                    stream=True
                )
                response.raise_for_status()
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line)
                        if 'response' in data:
                            yield data['response']
                        if data.get('done', False):
                            break
            except Exception as e:
                app.logger.error(f"生成小说时发生错误：{str(e)}")
                yield f"发生错误：{str(e)}"

        return Response(stream_with_context(generate()), content_type='text/plain')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
