import os
import re

from flask import (
    Flask,
    request,
    jsonify,
)


app = Flask(__name__)


def update_openai_key_in_env(new_key):
    with open(".env", "r") as file:
        content = file.read()

    new_content = re.sub(
        r'OPENAI_API_KEY=.*',
        f'OPENAI_API_KEY={new_key}',
        content,
    )

    if "OPENAI_API_KEY=" not in content:
        new_content += f"\nOPENAI_API_KEY={new_key}\n"

    with open(".env", "w") as file:
        file.write(new_content)


@app.route('/b/setToken', methods=['POST'])
def set_token():
    data = request.get_json()
    token = data['token']
    os.environ["OPENAI_API_KEY"] = token
    update_openai_key_in_env(token)
    response = {'token': token}
    return jsonify(response)


@app.route('/b/getToken', methods=['GET'])
def get_token():
    api_key = os.environ.get("OPENAI_API_KEY")
    response = {'token': api_key}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
