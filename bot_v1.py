import discord #import the discord module. discord module utilizes discord library to give
#access to many prebuilt functions and features.
import requests  #import requests for requests.get function.
import json 
import random

intents = discord.Intents.default() #standard intents for discord 
intents.message_content = True

client = discord.Client(intents=intents)

sad_words = ["sad","depressed","unhappy","angry","miserable","depressing" ]

starter_encouragements = [
  "Cheer Up!",
  "Hang in there.",
  "You'll be alright.",
  "You're good.",
]

syed = ["I miss her...", "Tsubi...", "TheVagabond.", "I CAN'T LET PEOPLE IN R/WIZ KNOW I EXIST"]
fidel = ["No more rank... teammates too trash", "You stupid monkey", "I can't do this anymore, 5 exams tomorrow", "Where my PAJG at"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
  
    if msg.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(starter_encouragements))
    
    if msg.startswith("syed" or "Syed"):
       await message.channel.send(random.choice(syed))

    if msg.startswith("fidel" or "Fidel"):
       await message.channel.send(random.choice(fidel))

client.run('your token')