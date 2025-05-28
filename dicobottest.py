import discord
from discord.ext import commands

bot = discord.Client(intents=discord.Intents.default())
client = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@client.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event    
async def on_command_error(ctx, error):
    if isinstance(error, discord.app_commands.CommandNotFound):
        await ctx.send("Command not found. Please use a valid command.")
    else:
        await ctx.send(f"An error occurred: {error}")

@bot.event
async def on_message(message):
    print(message)
    print(f'Message from {message.author}: {message.content}')
    if message.author == bot.user:
        return  # Ignore messages from the bot itself

    if message.content.startswith('!hello'):
        await message.channel.send('Hello! I am Dicobot, your friendly bot!')

@discord.app_commands.command(name="dicobot", description="A simple bot to demonstrate Discord.py commands.")
async def dicobot(interaction: discord.Interaction):
    # Create an embed message
    embed = discord.Embed(
        title="Dicobot",
        description="This is a simple bot to demonstrate Discord.py commands.",
        color=discord.Color.blue()
    )
    
    embed.add_field(name="Hello!", value="I am Dicobot, your friendly bot.", inline=False)
    embed.add_field(name="Commands", value="Use `/dicobot` to see this message.", inline=False)
    embed.set_footer(text="Powered by Discord.py")
    await interaction.response.send_message(embed=embed)


bot.run("TOKEN")