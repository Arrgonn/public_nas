# Modules
import os
import socket
from discord.ext import commands
from fabric import Connection

# Variables
my_server = str(os.getenv('MY_SERVER'))
wake_up_port = int(os.getenv('PORT_WAKE_UP'))
mac_address = str(os.getenv('MAC_ADDRESS'))
control_port = int(os.getenv('PORT_CONTROL'))
username = str(os.getenv('USERNAME'))
password = str(os.getenv('PASSWORD'))

# Classe GesCommandsCog
class GesCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Commandes de gestion du NAS ; wake_up_nas(alias: start) - Stop - killprocess(alias: kill) - start_process (alias: sp) - See_process(alias: see, seep, listprocess, listp)

    @commands.hybrid_command(
        name="wake_up_nas",
        aliases=["start"], 
        help="Permet de démarrer le serveur via WOL (Wake ON LAN)"
    )
    async def wake_up_nas(self, ctx):
        try: # thx to https://www.youtube.com/watch?v=MOYJkq4RfPQ
            mac_clean = mac_address.replace(":", "").replace("-", "")
            mac_byte = bytes.fromhex(mac_clean)
            payload = b"\xFF" * 6 + mac_byte * 16
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                sock.sendto(payload, ("<broadcast>", wake_up_port))
                await ctx.reply("Le serveur s'allume")
        except Exception as e:
            await ctx.reply(f"Erreur : {e}")

    @commands.hybrid_command(
        name="stop_nas",
        aliases=["stop"], 
        help="Permet d'éteindre le serveur"
    )
    async def stop_nas(self, ctx):
        ssh_connection_and_close = Connection(host=f"{my_server}:{control_port}", user=username, connect_kwargs={'password' : password}).run(f'echo "{password}" | sudo -S poweroff', hide=True)
        await ctx.reply("Le serveur va s'arrêter")

    @commands.hybrid_command(
            name="killprocess",
            aliases=["kill","killp","kp"], 
            help="Permet d'arrêter un processus"
    )
    async def killprocess(self, ctx, process: str):
        try:
            Connection(host=f"{my_server}:{control_port}", user=username, connect_kwargs={'password': password}).run(f'echo "{password}" | sudo -S pkill {process}', hide=True)
            await ctx.reply(f"Le processus {process} a été arrêté")
        except Exception as e:
            await ctx.reply(f"Erreur lors de l'arrêt du processus {process}: {e}")

    @commands.hybrid_command(
            name="start_process",
            aliases=["sp"], 
            help="Permet de lancer un processus"
    )
    async def start_process(self, ctx, process : str):
        try:
            Connection(host=f"{my_server}:{control_port}", user=username, connect_kwargs={'password': password}).run(f'echo "{password}" | sudo -S systemctl start {process}', hide=True)
            await ctx.reply(f"Le processus {process} a été lancé")
        except Exception as e:
            await ctx.reply(f"Erreur lors de l'arrêt du processus {process}: {e}")

    @commands.hybrid_command(
            name="see_process",
            aliases=["see", "seep", "listprocess", "listp"], 
            help="Permet de voir les processus en cours"
    )
    async def see_process(self, ctx):
        try:
            process_list =Connection(host=f"{my_server}:{control_port}", user=username, connect_kwargs={'password': password}).run(f'echo "{password}" | sudo -S ps aux | grep ^{username}', hide=True)
            await ctx.reply(f"{process_list}")
        except Exception as e:
            await ctx.reply(f"Erreur lors de la visualisation: {e}")

async def setup(bot):
    await bot.add_cog(GesCommandsCog(bot))
