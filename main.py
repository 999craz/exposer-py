import discord
from secret import token, ownerID
from pytz import timezone
from firebase import write, fetch

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
prefix = "?"
ownerID = ownerID

def normalize(p:str):
    return p.encode('utf-16','surrogatepass').decode('utf-16')

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await client.change_presence(status=discord.Status.invisible)
    
@client.event
async def on_message(message: discord.message.Message):
    if message.author == client.user : return 
    if not message.content.startswith(prefix) or message.content == prefix : return
    cmd = message.content.replace(prefix, "").split()[0]
    if cmd == "ping":
        await message.channel.send(f"pong!🏓 {message.author.mention}")
    elif cmd == "expose":
        if len(message.mentions) == 0 :
            await message.reply("provide at least one member to be exposed")
            return
        targetUser = message.mentions[0]
        if message.author.id != ownerID and targetUser.id == ownerID:
            await message.channel.send("You can't expose the creator")
            return
        embed = discord.Embed(title=f"What `{targetUser.name}` did not want you to see", color=0xFFFFFF)
        res = fetch(f"{targetUser.name} ({targetUser.discriminator})")
        if res.val() == None:
            await message.channel.send(f"nothing to be exposed ({targetUser.name})")
            return
        for msg in res.each():
            data = msg.val()
            embed.add_field(name=str(data["timestamp"]), value=data["content"], inline=False)
        embed.set_thumbnail(url=targetUser.avatar.url)
        await message.channel.send(embed=embed)
    elif cmd == "help":
        await message.reply(f"{prefix}expose <user mention>")
        return    

@client.event
async def on_message_delete(message: discord.message.Message):
    if message.author.bot or message.content == "": return
    author = normalize(f"{message.author.name.split('#')[0]} ({message.author.discriminator})")
    content = normalize(message.content)
    user = {
        "name": message.author.name.split("#")[0],
        "avatar": message.author.avatar.url ,
        "discriminator": message.author.discriminator,
    }
    deletedMessage = {
        "content": content,
        "timestamp": message.created_at.astimezone(timezone("EET")).ctime()
    }
    
    write(author, user, deletedMessage)

client.run(token)
