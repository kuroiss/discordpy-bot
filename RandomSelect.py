import pandas as pd
import random
import time

# constant variable
INSANE_LOWER = 1
INSANE_UPPER = 25


def isint(s):  # 整数値を表しているかどうかを判定
    try:
        int(s, 10)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True

def ParseDifficult(difficult):
    lower = INSANE_LOWER
    upper = INSANE_UPPER
    
    if '-' in difficult:
        split_diff = difficult.split('-')
        if len(split_diff) == 1:
            lower = int(split_diff)
            upper = lower
        
        if len(split_diff) > 1:
            first_num = int(split_diff[0])
            second_num = int(split_diff[1])
            
            lower = first_num if first_num < second_num else second_num
            upper = second_num if second_num >= first_num else first_num
    else:
        if isint(difficult):
            print(difficult)
            lower = int(difficult)
            upper = int(difficult)
        else:
            print(difficult)
            lower = 12
            upper = 12

    return lower, upper
        
    

def CreateInsaneDictionary(lower, upper):
    insane_dict = dict()
    for level  in range(lower, upper + 1):
        csv_path = './InsaneTable/insane_' + str(level) + '.csv'
        music_table = pd.read_csv(csv_path)
        insane_dict.update(zip(music_table['タイトル'], music_table['レベル']))
    return insane_dict
    
def GetInsaneChallenge(difficult, select_num):
    random.seed(time.time())
    
    lower_diff = 1
    upper_diff = 25
    
    lower_diff, upper_diff = ParseDifficult(difficult)
    insane_dict = CreateInsaneDictionary(lower_diff, upper_diff)
    
    challenge_set = set()
    while len(challenge_set) < select_num:
        title, level = random.choice(list(insane_dict.items()))
        challenge_set.add(level + ' ' + title)
    
    return challenge_set
        

def CreateBeatDictionary(lower, upper):
    beat_dict = dict()
    for level  in range(lower, upper + 1):
        csv_path = './BeatTable/beat_' + str(level) + '.csv'
        music_table = pd.read_csv(csv_path)
        for title in music_table['曲名']:
            beat_dict[title] = str(level)
        # beat_dict.update(zip(music_table['曲名'], level))
    return beat_dict

def GetBeatmaniaChallenge(difficult='12', select_num=1):
    random.seed(time.time())
    
    lower_diff = 7
    upper_diff = 12
    
    lower_diff, upper_diff = ParseDifficult(difficult)
    beat_dict = CreateBeatDictionary(lower_diff, upper_diff)
    
    challenge_set = set()
    while len(challenge_set) < select_num:
        title, level = random.choice(list(beat_dict.items()))
        challenge_set.add(level + ' ' + title)
        
    return challenge_set

def CreateDanceDictionary(lower, upper):
    dance_dict = dict()
    for level  in range(lower, upper + 1):
        csv_path = './DanceTable/dance_' + str(level) + '.csv'
        music_table = pd.read_csv(csv_path)
        for title in music_table['曲名']:
            dance_dict[title] = str(level)
    return dance_dict

def GetDanceChallenge(difficult='15', select_num=1):
    random.seed(time.time())
    
    lower_diff = 11
    upper_diff = 19
    
    lower_diff, upper_diff = ParseDifficult(difficult)
    beat_dict = CreateDanceDictionary(lower_diff, upper_diff)
    
    challenge_set = set()
    while len(challenge_set) < select_num:
        title, level = random.choice(list(beat_dict.items()))
        challenge_set.add(level + ' ' + title)
        
    return challenge_set

def CreatePopnDictionary(lower, upper):
    popn_dict = dict()
    for level  in range(lower, upper + 1):
        csv_path = './PopnTable/popn_' + str(level) + '.csv'
        music_table = pd.read_csv(csv_path)
        title_table = music_table['曲名']
        junre_table = music_table['ジャンル名 (タイプ)']
        for index in range(len(title_table)):
            music_title = title_table[index]
            music_junre = junre_table[index]
            dict_index = ""
            if(music_title != music_junre):
                dict_index = music_junre + " (" + music_title + ")"
            else:
                dict_index = music_title
                
            popn_dict[dict_index] = str(level)
    
    return popn_dict

def GetPopnChallenge(difficult='46', select_num=1):
    random.seed(time.time())
    
    lower_diff = 40
    upper_diff = 50
    
    lower_diff, upper_diff = ParseDifficult(difficult)
    popn_dict = CreatePopnDictionary(lower_diff, upper_diff)
    
    challenge_set = set()
    while len(challenge_set) < select_num:
        title, level = random.choice(list(popn_dict.items()))
        challenge_set.add(level + ' ' + title)
        
    return challenge_set

def main():
    print('random select (11 - 12) \n')
    beat_list = GetDanceChallenge(select_num=10)
    for challenge in beat_list:
        print(challenge)

if __name__ == '__main__':
    main()
    


