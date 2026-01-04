import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_dict(
    eval(os.environ["GOOGLE_CREDENTIALS"]), scope)

client = gspread.authorize(creds)
sheet = client.open("FBFV - Banco de Dados")
jogadores = sheet.worksheet("JOGADORES")

@bot.event
async def on_ready():
    print("Bot online")

@bot.command()
async def jogador(ctx, *, dados):
    partes = dados.split("|")
    jogadores.append_row([p.strip() for p in partes])
    await ctx.send("Jogador cadastrado com sucesso!")

bot.run(os.environ["9d411a09e956fd4252a32ae69cc23dced9fad32cc540ebe772c9b6973099ae4c"])
