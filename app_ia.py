import requests

ia_key = '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'

def perguntar_ia(mensagem):
    url = 'https://openrouter.ai/api/v1/chat/completions'

    headers = {
        "Authorization": f"Bearer {ia_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": mensagem}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    resposta = response.json()
    return resposta['choices'][0]['message']['content']

while True:
    msg = input('Você: ')
    
    if msg == 'sair':
        break

    reposta = perguntar_ia(msg)

    print('JF: ', reposta)

