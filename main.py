import discord
from discord.ext import commands

# getting your token from the token.txt
def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

# logging in your bot
TOKEN = read_token()
bot = commands.Bot(command_prefix='>', intents=discord.Intents.all(), help_command=None)
bot.remove_command('help')
bot.run('TOKEN')


#creating custom help command
@bot.command()
async def help(ctx, args=None):
    embed = discord.Embed(title="I am here to help you.")
    command_names_list = [com.name for com in bot.commands]

    if not args:
        embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+com.name for i, com in enumerate(bot.commands)]),
            inline=False
        )
        embed.add_field(
            name="Details",
            value="Type `>help [command name]` for more details about each command.",
            inline=False
        )
    elif args in command_names_list:
        embed.add_field(
            name=args,
            value=''  #dict with descriptions for your commands
        )
    else:
        embed.add_field(
            name="Uhh....",
            value="There is no command like this."
        )

    await ctx.send(embed=embed)


# Starting a bot
@bot.event
async def on_ready():
    print('Bot started.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Wersario`s development'))
