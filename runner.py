import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    test = message.content
    commandmessage = test.split(':')
    if commandmessage[0] == 'create-new':
        await client.create_channel(message.server, commandmessage[1])


        
    
token = 'NTQyNDI5NTQwMDE0ODgyODIy.Dzt4bw.63Eh3M_jyP4Do5DVu3uds6oxapY'

client.run(token)

