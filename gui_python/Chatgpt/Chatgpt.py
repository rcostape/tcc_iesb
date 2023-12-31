import requests
import json


class Chatgpt(object):
    def __init__(self, textoGPT = ""):
      self.info = {}
      self.textoGPT = textoGPT

    def selectGPT(self, textoGPT):
      try:
        headers = {"Authorization": "Bearer ", "content-type": "Application/json"}

        link = "https://api.openai.com/v1/chat/completions"

        id_modelo = "gpt-3.5-turbo"

        body_mensagem = {
                "model": id_modelo,
                "messages": [{"role": "user", "content": textoGPT}]
        }

        body_mensagem = json.dumps(body_mensagem)
        requisicao = requests.post(link, headers=headers, data=body_mensagem)

        resposta = requisicao.json()

        return resposta ["choices"][0]["message"]["content"]
      except:
        return resposta ["error"]["message"] + textoGPT

















































