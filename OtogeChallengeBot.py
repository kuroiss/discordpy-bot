import RandomSelect
import discord
from discord import app_commands
import os

UNDEF_DIFF = '1-25'

def GetChallengeString(challenges):
    reply_message = ""
    for challenge in challenges:
        reply_message += challenge + '\n'    
        
    return reply_message

def isint(s):  # 整数値を表しているかどうかを判定
    try:
        int(s, 10)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True
    
def ParseDifficultAndSelectNum(content, mode='insane'):
    message_list = content.split(' ')
    
    # メッセージから難易度指定と選曲回数をパース
    if mode == 'insane' or mode == 'bms':
        difficult = UNDEF_DIFF
        select_num = 1
        
        # とりあえず決め打ち
        if len(message_list) == 3:
            difficult = message_list[2]
        else:
            difficult = message_list[2]
            tmp_num = message_list[3]
            if isint(tmp_num) and (int(tmp_num) >= 1) and (int(tmp_num) <= 25):
                select_num = int(tmp_num)
            else:
                select_num = 1
        # for msg_str in message_list:
        #     if '-' in msg_str:
        #         difficult = msg_str
                
        #     if isint(msg_str) and (int(msg_str) >= 1) and (int(msg_str) <= 25):
        #         select_num = int(msg_str)

    elif mode == 'beat':
        if len(message_list) == 1:
            difficult = 12
            select_num = 1
        elif len(message_list) == 2:
            difficult = 12
            select_num = int(message_list[1])
        else:
            difficult = int(message_list[1])
            select_num = int(message_list[2])

    return difficult, select_num

client_intents = discord.Intents.default()
client = discord.Client(intents=client_intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("on ready")
    await tree.sync()

# TODO : そのうち重複してる処理はまとめたいけど、今はめんどいからコピペでいいや
@tree.command(name="beat12", description="throw a Beatmania Level12 request.")
async def request_command_beat12(interaction: discord.Interaction, select_num:int = 1):
    diff = '12'
    message = GetChallengeString(RandomSelect.GetBeatmaniaChallenge(diff, select_num))
    await interaction.response.send_message(message)

@tree.command(name="beat", description="throw Beatmania requests(Level 11 - 12).")
async def request_command_beatmania(interaction: discord.Interaction, diff:str, select_num:int = 1):
    message = GetChallengeString(RandomSelect.GetBeatmaniaChallenge(diff, select_num))
    await interaction.response.send_message(message)

@tree.command(name="dance", description="throw DDR requests(level 11 - 19).")
async def request_command_dance(interaction: discord.Interaction, diff:str, select_num:int = 1):
    message = GetChallengeString(RandomSelect.GetDanceChallenge(diff, select_num))
    await interaction.response.send_message(message)

@tree.command(name="ddr", description="throw DDR requests(level 11 - 19).")
async def request_command_ddr(interaction: discord.Interaction, diff:str, select_num:int = 1):
    message = GetChallengeString(RandomSelect.GetDanceChallenge(diff, select_num))
    await interaction.response.send_message(message)

@tree.command(name="bms", description="throw BMS Insane requests(★1 - 25).")
async def request_command_bms(interaction: discord.Interaction, diff:str, select_num:int = 1):
    message = GetChallengeString(RandomSelect.GetInsaneChallenge(diff, select_num))
    await interaction.response.send_message(message)

@tree.command(name="insane", description="throw BMS Insane requests(★1 - 25).")
async def request_command_insane(interaction: discord.Interaction, diff:str, select_num:int = 1):
    message = GetChallengeString(RandomSelect.GetInsaneChallenge(diff, select_num))
    await interaction.response.send_message(message)

@tree.command(name="popn", description="throw Popn requests(40 - 50).")
async def request_command_insane(interaction: discord.Interaction, diff:str, select_num:int = 1):
    message = GetChallengeString(RandomSelect.GetPopnChallenge(diff, select_num))
    await interaction.response.send_message(message)

@tree.command(name="p", description="throw Popn requests(40 - 50).")
async def request_command_insane(interaction: discord.Interaction, diff:str, select_num:int = 1):
    message = GetChallengeString(RandomSelect.GetPopnChallenge(diff, select_num))
    await interaction.response.send_message(message)

@client.event
async def on_message(message):
    if message.author.bot:
        pass
    
    bot_mention_str = '<@' + str(client.user.id) + '>'
    
    if bot_mention_str in message.content:
        if 'insane' in message.content or 'bms' in message.content:
            difficult, select_num = ParseDifficultAndSelectNum(message.content)
            
            # 課題一覧を取得する
            challenge_set = RandomSelect.GetInsaneChallenge(difficult, select_num)
            
            # メッセージを作る
            reply_message = '<@'+ str(message.author.id) +'>\n'
            for challenge in challenge_set:
                reply_message += challenge + '\n'
            
            await message.channel.send(reply_message)
            
        elif 'beat' in message.content:
            difficult, select_num = ParseDifficultAndSelectNum(message.content)
            
            challenge_set = RandomSelect.GetBeatmaniaChallenge(difficult, select_num)
            
            reply_message = '<@'+ str(message.author.id) +'>\n'
            for challenge in challenge_set:
                reply_message += challenge + '\n'
            
            await message.channel.send(reply_message)

        elif 'dance' in message.content or 'ddr' in message.content:
            difficult, select_num = ParseDifficultAndSelectNum(message.content)
            
            challenge_set = RandomSelect.GetDanceChallenge(difficult, select_num)
            
            reply_message = '<@'+ str(message.author.id) +'>\n'
            for challenge in challenge_set:
                reply_message += challenge + '\n'
            
            await message.channel.send(reply_message)

        elif 'popn' in message.content or 'p' in message.content:
            difficult, select_num = ParseDifficultAndSelectNum(message.content)
            
            print("difficult", difficult)
            
            challenge_set = RandomSelect.GetPopnChallenge(difficult, select_num)
            
            reply_message = '<@'+ str(message.author.id) +'>\n'
            for challenge in challenge_set:
                reply_message += challenge + '\n'
            
            await message.channel.send(reply_message)

token = os.environ["OTOGE_DISCO_TOKEN"]
client.run(token)
