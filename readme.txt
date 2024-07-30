Este é um bot para Discord que gera imagens com base em prompts de texto fornecidos pelos usuários. É integrado com a api "Prodia" para gerar imagens
A mensagem do usuário enviada em Portugues é traduzida para o inglês por meio da biblioteca "googletrans" e é enviada ao bot que gera a imagem e retorna ela em uma mensagem no canal de texto do Discord

Dependências: discord.py
prodiapy
googletrans

Config: Substitua "API-KEY" pela sua chave api disponível em: https://app.prodia.com/api
crie um bot no Discord Developer Portal, adicione-o em um servidor, substitua "TOKEN" pelo token do bot do discord que você criou
Copie o ID do Canal de texto do servidor criado e cole em "CHANNEL_ID"

Uso: O prefixo padrão é "!imagine"
Exemplo: !imagine uma paisagem 

