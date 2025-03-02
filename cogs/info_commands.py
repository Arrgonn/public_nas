# Modules
import os
import requests
from discord import app_commands
from discord.ext import commands

# Variables
status_messages = {200:"🟢​",404:"🟡​",500:"🔴​"}
my_server = str(os.getenv('MY_SERVER'))
jellyfin_port = str(os.getenv('PORT_JELLYFIN'))
minecraft_port = str(os.getenv('PORT_MINECRAFT'))

# Classe InfoCommandsCog
class InfoCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Commandes d'informations - IP - Service_status
    @commands.hybrid_command(
            name="ip",
            help="Obtenir l'adresse ip du service demandé"
    ) # Commande permettant d'obtenir l'ip du serveur pour le service spécifié
    @app_commands.describe(
        service_choice = "Minecraft ou Jellyfin"
    )
    async def ip(self, ctx, service_choice: str):
        if service_choice.lower() == 'minecraft':
            ip_port = minecraft_port
        elif service_choice.lower() == 'jellyfin':
            ip_port = jellyfin_port
        await ctx.reply(f"""L'ip du serveur {service_choice.lower()} est {my_server}:{ip_port}""")


    @commands.hybrid_command(
            name="service_status",
            aliases=['ss'],
            help="Obtenir des informations quant au status des serivces JellyFin ou Minecraft"
    ) # Permet d'obtenir l'état du service spécifié
    @app_commands.describe(
        service_choice = "Minecraft ou Jellyfin"
    )
    async def service_status(self, ctx, service_choice: str):
        try:
            if service_choice.lower() == "minecraft":
                response = requests.get(f"http://{my_server}:{minecraft_port}")
            elif service_choice.lower() == "jellyfin":
                response = requests.get(f"http://{my_server}:{jellyfin_port}")
            await ctx.reply(f"L'état du serveur est {status_messages.get(response.status_code, '🔴')}")
        except requests.exceptions.RequestException as e:
                print(f"Erreur de connexion: {e}")  # Affiche l'erreur dans le terminal
                await ctx.reply("L'état du serveur est 🔴 (Erreur de connexion, veuillez lancer le NAS ou le service souhaité)")


async def setup(bot):  
    await bot.add_cog(InfoCommandsCog(bot))