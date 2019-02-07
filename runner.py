import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.content == 'create-new':
        server = message.id
        await client.create_channel(server, 'test')
        print("create new")
    elif message.author != client.user:
        await client.send_message(message.channel, message.content[::-1])
        print(message.id)
        if message.content == 'test':
            print("works")

        
    
token = 'NTQyNDI5NTQwMDE0ODgyODIy.Dzt4bw.63Eh3M_jyP4Do5DVu3uds6oxapY'

client.run(token)

