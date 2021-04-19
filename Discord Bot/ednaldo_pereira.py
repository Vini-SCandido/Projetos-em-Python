import discord
from discord.ext import commands
from random import choice, randint
from linecache import getline

def ler_txt(txt : str):
    with open(txt, "r", encoding="utf-8") as file:
        lines = 0
        for line in file.readlines():
            lines += 1
        try:
            msg = str(getline(txt, randint(1, lines)))
            return msg.rstrip("\n")
        except Exception:
            return
          
def pokemon():
    try:
        dados = ler_txt("pokemons.txt").split("#")
        embed = discord.Embed(title=dados[0], color=discord.Color.gold())
        embed.set_image(url=dados[1])
        return embed
    except Exception:
        return "Pokedex vazia."
 

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="Ed ", help_command=None, intents=intents)

@bot.event
async def on_ready():
    print("Ednaldo Pereira está On-line")

@bot.event
async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            comp = ['Olá,', 'Eae,', 'Oi,', 'Ora ora,', 'Yare yare daze!', 'Bem-vindo(a),', 'Quanto tempo,']
            to_send = f'{choice(comp)} {member.mention}'
            await guild.system_channel.send(to_send)

@bot.command(name='pokemon')
async def poke(ctx):
    """Ednaldo Pereira te dá uma aula sobre pokemons e seus nomes verdadeiros."""
    if pokemon() != "Pokedex vazia.":
        await ctx.send(embed=pokemon())
    else:
        await ctx.send("Pokedex vazia.")

    
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Comandos do Ednaldo", color=discord.Color.gold())
    embed.add_field(name="Ed pokemon", value="Nintendo não sabe criar nome de pokemon.", inline=False)
    await ctx.send(embed=embed)

bot.run("O TOKEN DO SEU BOT VAI AQUI!")
