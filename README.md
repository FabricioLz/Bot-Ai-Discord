Brita 

Este é um bot do Discord que utiliza a API da Prodia para gerar imagens baseadas em prompts fornecidos pelos usuários. Ele também usa o Google Translate para traduzir os prompts de português para inglês, garantindo uma integração mais acessível e prática.

🚀 Funcionalidades
  Geração de imagens: Gera imagens com base em descrições de texto fornecidas pelos usuários.
  Tradução automática: Traduz automaticamente os prompts do português para o inglês, facilitando o uso por falantes de português.
  Resposta instantânea: Envia o link da imagem gerada diretamente no canal do Discord.

Tecnologias Utilizadas
  Discord.py: Biblioteca para criar bots no Discord.
  Prodia API: Serviço de geração de imagens baseadas em inteligência artificial.
  Googletrans: Biblioteca para tradução automática.

📋 Pré-requisitos
  Python 3.8 ou superior
  Bibliotecas Python necessárias:
  discord.py
  prodiapy
  googletrans
Para instalar as dependências, execute: pip install discord.py prodiapy googletrans==4.0.0-rc1

Configurações obrigatórias:
  Substitua API-KEY pela sua chave da API Prodia.
  Substitua TOKEN pelo token do seu bot no Discord.
  Substitua ID pelo ID do canal onde o bot será ativo.

📚 Como Usar
  Clone este repositório: git clone https://github.com/seu-usuario/seu-repositorio.git
  cd seu-repositorio

Configure as variáveis obrigatórias no código:

  BOT_TOKEN: Token do bot do Discord.
  API-KEY: Chave da API Prodia.
  CHANNEL_ID: ID do canal no Discord.
  Execute o bot: python bot.py

No Discord, use o comando !imagine seguido de um prompt:!imagine Um pôr do sol em uma praia tropical
O bot traduzirá o prompt, e gerará a imagem e enviará a imagem no canal.
