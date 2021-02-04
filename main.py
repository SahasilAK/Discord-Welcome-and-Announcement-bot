import discord
from discord.ext import commands
from discord import utils
import os
from keep_alive import keep_alive
import time
import random
from custom_msg import hi_lists, colors_list, bot_commands, hidden_commands
import json



# ___________________________Constants for the discord bot________________________

SERVER_ID = os.getenv('SERVER_ID')
CHANNEL_ID = os.getenv('CHANNEL_ID')
ADMIN_ROLE_ID = os.getenv('ADMIN_ROLE_ID')
GAMING_TEXT_ID = os.getenv('GAMING_TEXT_ID')
RULE_TEXT_ID = os.getenv('RULE_TEXT_ID')
ROLE_TEXT_ID = os.getenv('ROLE_TEXT_ID')
MODERATOR_ROLE_ID = os.getenv('MODERATOR_ROLE_ID')
TEST_CHANNEL_ID = os.getenv('TEST_CHANNEL_ID')
EVERYONE_ROLE_ID = os.getenv('EVERYONE_ROLE_ID')
ANNOUNCEMENT_CHANNEL_ID = os.getenv('ANNOUNCEMENT_CHANNEL_ID')
# _______________________________________________________________________________________

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)



# ___________________Bot rich presence__________________________
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=".help"))
    print(f'We have logged in as {client.user}')


# ___________________________Members When Join_______________________________
@client.event
async def on_member_join(member):

    # ______________Defining roles and channels to mention________________

    guild = client.get_guild(SERVER_ID)
    welcome_channel = guild.get_channel(CHANNEL_ID)

    gaming_text = client.get_channel(GAMING_TEXT_ID)
    rule_text = client.get_channel(RULE_TEXT_ID)
    role_text = client.get_channel(ROLE_TEXT_ID)

    if not member.bot:
        #message in welcome channel
        await welcome_channel.send(f'Hey {member.mention}, welcome to **MALMER** Discord server, <:welcome:793253408814399520>\n'\
                                 '\n'\
                                 ':partying_face:  Please tell us your NAME ( IGN will do),\n'\
                                 ':partying_face: Your gaming platform (PC, Mobile, Console)\n'\
                                 ':partying_face: Games you mostly play in a daily basis.\n'\
                                 f'tag <@&{ADMIN_ROLE_ID}> in {gaming_text.mention}\n'\
                                 ' \n'\
                                 'Enjoy your stay.\n'\
                                 f'read {rule_text.mention} \n'\
                                 f'choose your gaming roles {role_text.mention}\n'\
                                 '\n'\
                                 'Be a Good Gamer :dancer:\n')

#___________________WEHEN BOT JOINS______________________
# else:

#   await welcome_channel.send(f'ഇത് {member.mention}, പുതിയ പണിക്കാരൻ ആണ്')

#message on pm
# await member.send(f'welcome to the server')


@client.event
async def on_message(message):
    gaming_text = client.get_channel(GAMING_TEXT_ID)
    rule_text = client.get_channel(RULE_TEXT_ID)
    role_text = client.get_channel(ROLE_TEXT_ID)

   

    
   

    #  _______________________Announcement__________________________
    if message.content == '.malan':
      await message.delete()
       # ___________________________Announce data________________________________________
      with open('data.json', 'r') as an_data:
          data = json.load(an_data)

      a_title = data['title']
      a_desc = data['description']
      a_url = data['url']
      a_img_url = data['img_url']
      color_list = random.choice(colors_list)
      # announcement_channel = guild.get_channel(ANNOUNCEMENT_CHANNEL_ID)
      announcement_channel = client.get_channel(ANNOUNCEMENT_CHANNEL_ID)


      announce = discord.Embed(title=a_title,description=a_desc,url=a_url,color=color_list)
      # await message.channel.send(f'@everyone ')
      # await message.channel.send(embed=announce)
      # await message.channel.send(a_img_url)
      await announcement_channel.send(f'@everyone ')
      await announcement_channel.send(embed=announce)
      await announcement_channel.send(a_img_url)
    # _________________________________________________________________

    if message.content == '.hi':
        hi_list = random.choice(hi_lists)
        await message.channel.send(hi_list)
        # await message.channel.send(f' :AmongUs::mellohi::banned::sans::nou:')
    if message.content == '.sendlink' or message.content == '.discord':
        await message.channel.send('https://discord.gg/qWsyByC')
    if message.content == '.bestgame':
        await message.channel.send('osu! Best')
    if message.content == '.a10':
        await message.delete()
        await message.channel.send(
            'hmmmmm. check this https://stylesatlife.com/wp-content/uploads/2016/06/mohanlal-without-makeup6.jpg'
        )
    if message.content == '.hentai':
        await message.delete()
        await message.channel.send(
            'better to watch this. " https://www.youtube.com/channel/UCImMNR03gzOizyYFE-DFifQ ""'
        )
    if message.content == '.yt' or message.content == '.youtube':
        await message.channel.send('https://www.youtube.com/malmerdotin')

    if message.content == '.roles':
        await message.channel.send(f'>>> {role_text.mention}')

    if message.content == '.support':
        await message.channel.send(f'<@&{MODERATOR_ROLE_ID}>')

    if message.content == '.admin':
        await message.channel.send(f'<@&{ADMIN_ROLE_ID}>')

    if message.content == f'.del':
        await message.channel.purge(limit=2)
# _____________________Printing bot commands________________
    if message.content == '.help':
        cmd_str = ''
        color_list = random.choice(colors_list)
        for cmds in bot_commands:

            cmd_str += f'{cmds}\n\n'

        embed = discord.Embed(title='Bot Commands',
                              description=f'{cmd_str}',
                              color=color_list)

        await message.channel.send(embed=embed)
# _____________________Hidden commands list auto deletes after 15sec____________
    if message.content == '.onion':
        cmd_strs = ''

        await message.delete()
        color_list = random.choice(colors_list)
        for cmds in hidden_commands:

            cmd_strs += f'{cmds}\n\n'

        embed = discord.Embed(title='Bot Commands',
                              description=f'{cmd_strs}',
                              color=color_list)

        await message.channel.send(embed=embed)
        time.sleep(10)
        await message.channel.purge(limit=1)


# _____________________GAMES__________________________________

# @client.event
# async def sent_anouncement(input_message):
#   test_channel = guild.get_channel(TEST_CHANNEL_ID)
#   await test_channel.send(input_message)

keep_alive()
client.run(os.getenv('TOKEN'))

# for checking channel and mesaage extras
# if message.channel == general and message.content !='':
