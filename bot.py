# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import responses
# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
  # LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
  load_dotenv()

  # GRAB THE API TOKEN FROM THE .ENV FILE.
  DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

  # GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
  intents = discord.Intents.default()
  intents.message_content = True
  bot = discord.Client(intents=intents)

  # EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
  @bot.event
  async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
      # PRINT THE SERVER'S ID AND NAME.
      print(f"- {guild.id} (name: {guild.name})")

      # INCREMENTS THE GUILD COUNTER.
      guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print(f"{bot.user} is in " + str(guild_count) + " guilds.")

  # EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        username = str(message.author)
        user_message = message.content
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

  # EXECUTES THE BOT WITH THE SPECIFIED TOKEN
  bot.run(DISCORD_TOKEN)