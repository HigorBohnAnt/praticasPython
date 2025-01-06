import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = 'sua-chave-da-api-da-openai'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'Por favor, envie uma mensagem no campo "prompt".'}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=prompt,
            max_tokens=150
        )

        chatgpt_response = response.choices[0].text.strip()

        return jsonify({'response': chatgpt_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
