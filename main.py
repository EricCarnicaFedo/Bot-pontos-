import discord
from discord.ext import commands

# Definindo as intents necessárias
intents = discord.Intents.default()
intents.message_content = True  # Permissão para acessar conteúdo de mensagens

# Criando o bot com as intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento quando o bot estiver pronto
@bot.event
async def on_ready():
    print("Estou pronto!")

# Rodando o bot com o token
bot.run('MTMyMDI1MTAyMjkyNDQ0NzgxNA.Gumifd.0Va9VKTvDeNOJHkEhLCjRy5Z6o8oOi0-D-vLoc')