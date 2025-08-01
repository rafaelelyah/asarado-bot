import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configura os intents necessários
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True

# Cria o bot com prefixo e intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento de inicialização
@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# Importa e ativa o listener (depois de criar o bot!)
from discord_bot.listener import setup_listener
setup_listener(bot)

# Inicia o bot com o token
bot.run(os.getenv("DISCORD_TOKEN"))