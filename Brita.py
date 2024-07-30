from discord.ext import commands
import discord
from prodiapy import Prodia
from googletrans import Translator

prodia = Prodia(
    api_key="API-KEY"
)
translator = Translator()



BOT_TOKEN = "TOKEN"
CHANNEL_ID = ID

intents = discord.Intents.default()
intents.all()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    pass

@bot.command()
async def imagine(ctx, *, promptText=None):
    if not promptText:
        await ctx.send("Por favor, forneça um prompt para a imagem.")
        return

    inputUser = str(promptText)
    traducao = translator.translate(inputUser, src='pt', dest='en')
    job = prodia.sd.generate(prompt=traducao.text)
    result = prodia.wait(job)
    await ctx.send(result.image_url)

bot.run(BOT_TOKEN)