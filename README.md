# Discord analytics bot

## General description

This bot bot was created to help you monitor and analyze your server's activity.\
If you are a rookie programmer, it will also help you get acquainted with discord.py and pandas.

## Creating a bot

To create a discord bot you should visit a [developer page](https://discord.com/developers/applications/).\
Here you just need to create an application by simply clicking on the button "New application".\
After that is done, you need to go to the bot tab and then click on the button called "Add bot".

After you created you first discord bot, you have to copy its token and save it somewhere, so nobody can see it.

To invite your bot to the server, simply go to the tab called "0Auth2", then go to the "URL Generator" tab, 
click on the square next to the bot, and finally just copy a link. After that, just paste it in your browser and bot will automatically join the server you chose.

## Installation

1. First of all, you have to download all files on your personal computer. The code runs on python 3,
 which you can download on [python.org](https://www.python.org/downloads/).
 
2. After successful installation you will have to download some libraries for your bot. There are two variants:
    - run ``pip install discord`` and ``pip install pandas`` in your console.
    - if your program can install libraries from *requirements.txt*, then just simply click install.
    
3. You are almost done! Now you just need to create a file called *token.txt* and there a token from your bot.
It will use it to login.


## Automation using heroku

There is a lot of ways how to automate your discord bot, but I found the easiest and the most effective variant.

1. The first step is creating an account on the platform called [heroku](https://www.heroku.com/).
2. After you created your account, click on the top right button "New" and then "Create a new app". Here you just need to give your app a unique name.
3. Once you did that, you will have to download [heroku git](https://devcenter.heroku.com/articles/heroku-cli) and then go to the "Deploy" tab.
4. Here you just have to follow the instructions to successfully automate your bot. If you need some additional commands, just scroll down a page where you downloaded heroku git.
