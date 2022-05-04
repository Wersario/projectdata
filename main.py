import discord
import requests
import matplotlib.pyplot as plt
import numpy as np
from discord.ext import commands
from descriptions import desc, key_words


# getting your token from the token.txt
def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


# logging in your bot
TOKEN = read_token()
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)
bot.remove_command('help')
bot.run('TOKEN')


# creating custom help command
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
            value=desc[str(args)]
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


@bot.command()
async def make_diagram(ctx, start, end):
    link = 'https://api.hh.ru/vacancies/'
    stats = np.array([0, 0, 0])
    labels = ['Unknown', 'Other Jobs', 'Programmers']
    check = 0
    for num in range(start, end):
        r = requests.get(link + str(num))
        if r.json()['description'] == 'Not Found':
            stats[0] += 1
            continue
        for word in key_words:
            if word in r.json()['name']:
                check = 1
                break
        if check == 1:
            stats[2] += 1
            check = 0
        else:
            stats[1] += 1

    plt.pie(stats, labels=labels)
    embed = discord.Embed(title="Here is your diagram.")
    embed.set_image(plt.show())
    await ctx.channel.send(embed=embed)


@bot.command()
async def get_vacancies(ctx, start, end):
    link = 'https://api.hh.ru/vacancies/'
    template = 'https://hh.ru/vacancy/'
    for num in range(start, end):
        r = requests.get(link + str(num))
        if r.json()['description'] == 'Not Found':
            continue
        for word in key_words:
            if word in r.json()['name']:
                await ctx.channel.send(f'{r.json()["name"]}, опыт работы: {r.json()["experience"]["name"]}. Ссылка: {template+str(num)}')

        await ctx.channel.send('That`s all!')
