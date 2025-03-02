# Commentaires en français, incohérents par rapport aux noms des fichiers(anglais)
# Modules - discord.py - requests - os - dotenv
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive

#Classe ServerBot servant à load les commandes qui sont dans le dossier "cogs"
class ServerBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['info_commands', 'gestion_commands']:
            await self.load_extension(f'cogs.{extension}')

# Variables 
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = ServerBot(command_prefix="^", intents=discord.Intents.all())

@bot.event
async def on_ready():
    sync = await bot.tree.sync()
    print(f"{len(sync)} commande(s) ont été synchronisée(s)")

if __name__ == '__main__':
    keep_alive()
    bot.run(token=token)