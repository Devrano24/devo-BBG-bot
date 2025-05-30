import discord
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# === HIER DEINE CHANNEL-IDs EINTRAGEN ===
EIN_AUSZAHLUNGEN_CHANNEL_ID = 1208870790934700104
ABGABEN_CHANNEL_ID = 1208869756518535228

def get_kw():
    return datetime.now().isocalendar()[1]

@bot.event
async def on_ready():
    print(f'✅ Bot ist online als {bot.user}')

@bot.command()
async def einzahlen(ctx, person: discord.Member, betrag: int, *, grund: str):
    embed = discord.Embed(
        title="💰 Einzahlungsbeleg",
        color=discord.Color.green(),
        timestamp=datetime.utcnow()
    )
    embed.add_field(name="👤 Person", value=person.mention, inline=False)
    embed.add_field(name="💵 Betrag", value=f"{betrag}€", inline=False)
    embed.add_field(name="📝 Grund", value=grund, inline=False)
    embed.set_footer(text=f"Erstellt von {ctx.author.name} am {datetime.now().strftime('%d.%m.%Y – %H:%M Uhr')}")
    
    channel = bot.get_channel(EIN_AUSZAHLUNGEN_CHANNEL_ID)
    await channel.send(embed=embed)
    await ctx.message.add_reaction("✅")

@bot.command()
async def abheben(ctx, person: discord.Member, betrag: int, *, grund: str):
    embed = discord.Embed(
        title="🏧 Abhebungsbeleg",
        color=discord.Color.red(),
        timestamp=datetime.utcnow()
    )
    embed.add_field(name="👤 Person", value=person.mention, inline=False)
    embed.add_field(name="💵 Betrag", value=f"{betrag}€", inline=False)
    embed.add_field(name="📝 Grund", value=grund, inline=False)
    embed.set_footer(text=f"Erstellt von {ctx.author.name} am {datetime.now().strftime('%d.%m.%Y – %H:%M Uhr')}")

    channel = bot.get_channel(EIN_AUSZAHLUNGEN_CHANNEL_ID)
    await channel.send(embed=embed)
    await ctx.message.add_reaction("✅")

@bot.command()
async def abgabe(ctx, vonwem: str, betrag: int):
    embed = discord.Embed(
        title="📤 Abgabe",
        color=discord.Color.light_grey(),
        timestamp=datetime.utcnow()
    )
    embed.add_field(name="👤 Von", value=vonwem, inline=False)
    embed.add_field(name="📅 Kalenderwoche", value=f"KW {get_kw()}", inline=False)
    embed.add_field(name="💵 Betrag", value=f"{betrag}€", inline=False)
    embed.set_footer(text=f"Erstellt von {ctx.author.name} am {datetime.now().strftime('%d.%m.%Y – %H:%M Uhr')}")

    channel = bot.get_channel(ABGABEN_CHANNEL_ID)
    await channel.send(embed=embed)
    await ctx.message.add_reaction("✅")

# BOT-TOKEN hier eintragen
bot.run('DEIN_BOT_TOKEN')
