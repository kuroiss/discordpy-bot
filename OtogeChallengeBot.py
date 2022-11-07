import RandomSelect
import discord
import os

UNDEF_DIFF = '1-25'

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
    if mode == 'insane':
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
            
    print(difficult, select_num)
    return difficult, select_num
    

client = discord.Client()

@client.event
async def on_read():
    print("on rady")
    print(discord.__version__)
    
@client.event
async def on_message(message):
    if message.author.bot:
        pass
    
    bot_mention_str = '<@' + str(client.user.id) + '>'
    
    if bot_mention_str in message.content:
        if 'insane' in message.content:
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

        elif 'dance' in message.content:
            difficult, select_num = ParseDifficultAndSelectNum(message.content)
            
            challenge_set = RandomSelect.GetDanceChallenge(difficult, select_num)
            
            reply_message = '<@'+ str(message.author.id) +'>\n'
            for challenge in challenge_set:
                reply_message += challenge + '\n'
            
            await message.channel.send(reply_message)

token = os.environ["OTOGE_DISCO_TOKEN"]
client.run(token)
