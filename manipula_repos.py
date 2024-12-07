import requests
import base64

class ManipulaRepositorios:

    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = 'seu token'
        self.headers = {
            'Authorization': "Bearer " + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        """Adiciona um arquivo ao repositório existente no GitHub."""

        # Codificando o conteúdo do arquivo em Base64
        try:
            with open(caminho_arquivo, "rb") as file:
                file_content = file.read()
            encoded_content = base64.b64encode(file_content)
        except FileNotFoundError:
            print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
            return

        # Montando a URL e os dados para o upload
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            "message": f"Adicionando o arquivo {nome_arquivo}",
            "content": encoded_content.decode("utf-8")
        }

        # Fazendo a requisição PUT para adicionar o arquivo
        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo "{nome_arquivo}": {response.status_code}')

        if response.status_code == 201:
            print(f"Arquivo '{nome_arquivo}' adicionado com sucesso!")
        else:
            print(f"Erro ao adicionar arquivo '{nome_arquivo}':", response.json())


# Instancia o objeto com o nome de usuário do GitHub
username = 'ruansoarespy'
nome_repo = 'linguagens-repositórios-empresas'

novo_repo = ManipulaRepositorios(username)

# Adiciona os arquivos ao repositório existente
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')
