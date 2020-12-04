import os
import regex as re

def rename_FIR(folder_name):
    # rename Logic
    print("Enter Main Title of the Web Series :")
    series_name = input()
    print("Enter Season Number Padding :")
    season_padding = '0{}'.format(input())
    _ = season_padding
    print("Enter Episode Number Padding :")
    episode_padding = '0{}'.format(input())
    pattern_first = re.compile(r'Episode (\d+) (- (.*?)-)') # FIR - Episode 1058 - 26th November 2013-KYv8C68UNHs.mp4
    pattern_second = re.compile(r'Episode (\d+)-((.*?).)') # FIR - Episode 59-S0NTwMpYu0g.srt
    pattern_3rd = re.compile(r'Ep (\d+) (- (.*?)-)') # FIR - . . . - Ep 159 - Full Episode-6phVOR6gC-E.mp4
    pattern_4th = re.compile(r'Episode (\d+)(- (.*?)-)') # FIR -    - Episode 1270- 11th November 2014-6AJ_LExXSUM.mp4
    pattern_5th = re.compile(r'Episode (\d+) (- (.*?) -) (\d+)') # FIR -    - Episode 1257 - 23rd October - 2014-BmsTXmfXdM4.srt
    for file_name in os.listdir(folder_name):
        if re.match(r'^FIR',file_name):
            episode = -1
            episode_name = -1
            if len(re.findall(pattern_first,file_name)) == 1:
                temp = re.findall(pattern_first,file_name)[0]
                episode = temp[0]
                episode_name = temp[-1]
            if len(re.findall(pattern_second,file_name)) == 1:
                temp = re.findall(pattern_second,file_name)[0]
                episode = temp[0]
            if len(re.findall(pattern_3rd,file_name)) == 1:
                temp = re.findall(pattern_3rd,file_name)[0]
                episode = temp[0]
                episode_name = temp[-1]
            if len(re.findall(pattern_4th,file_name)) == 1:
                temp = re.findall(pattern_4th,file_name)[0]
                episode = temp[0]
                episode_name = temp[-1]
            if len(re.findall(pattern_5th,file_name)) == 1:
                temp = re.findall(pattern_5th,file_name)[0]
                episode = temp[0]
                episode_name = '{} {}'.format(temp[-2],temp[-1])
            name = ''
            if episode_name == -1:
                name = '{} {}'.format(series_name,format(int(episode),episode_padding))
            else:
                name = '{} {} {}'.format(series_name,format(int(episode),episode_padding),episode_name)
            
            if re.search(r'mp4$',file_name):
                name = '{}.mp4'.format(name)
            elif re.search(r'srt$',file_name):
                name = '{}.srt'.format(name)
                pass
            else:
                pass
            os.rename('{}/{}'.format(folder_name,file_name),'{}/{}'.format(folder_name,name))
    pass

def rename_Game_of_Thrones(folder_name):
    # rename Logic
    print("Enter Main Title of the Web Series :")
    series_name = input()
    print("Enter Season Number Padding :")
    season_padding = '0{}'.format(input())
    print("Enter Episode Number Padding :")
    episode_padding = '0{}'.format(input())
    for file_name in os.listdir(folder_name):
        if re.search(r'^(Game of Thrones)',file_name):
            season = -1
            episode = -1
            episode_name = -1
            if len(re.findall(r'- (\d+)x(\d+) (- (.*?)\.)',file_name)): # Game of Thrones - 1x62 - The Kingsroad.720p HDTV.CTU.en.mp4
                temp = re.findall(r'- (\d+)x(\d+) (- (.*?)\.)',file_name)[0]
                season=temp[0]
                episode=temp[1]
                episode_name=temp[-1]
            name = '{} {} {} {}'.format(series_name,format(int(season),season_padding),format(int(episode),episode_padding),episode_name)
            if re.search(r'mp4$',file_name):
                name = '{}.mp4'.format(name)
            elif re.search(r'srt$',file_name):
                name = '{}.srt'.format(name)
                pass
            else:
                pass
            os.rename('{}/{}'.format(folder_name,file_name),'{}/{}'.format(folder_name,name))
    pass
    

def rename_Sherlock(folder_name):
    # rename Logic 
    print("Enter Main Title of the Web Series :")
    series_name = input()
    print("Enter Season Number Padding :")
    season_padding = '0{}'.format(input())
    print("Enter Episode Number Padding :")
    episode_padding = '0{}'.format(input())
    for file_name in os.listdir(folder_name):
        season = -1
        episode = -1
        episode_name = -1
        if len(re.findall(r'\.S(\d+)\.E(\d+)',file_name)) == 1: # Sherlock.S01.E01.480p.srt
            temp = re.findall(r'\.S(\d+)\.E(\d+)',file_name)[0]
            season=temp[0]
            episode=temp[1]
        if len(re.findall(r'\.S(\d+)E(\d+)',file_name)) == 1: # Sherlock.S04E03.720p.x265.mp4
            temp = re.findall(r'\.S(\d+)E(\d+)',file_name)[0]
            season=temp[0]
            episode=temp[1]
        name = ''
        if episode_name != -1:
            name = '{} {} {} {}'.format(series_name,format(int(season),season_padding),format(int(episode),episode_padding),episode_name)
        else:
            name = '{} {} {}'.format(series_name,format(int(season),season_padding),format(int(episode),episode_padding))
        if re.search(r'mp4$',file_name):
            name = '{}.mp4'.format(name)
        elif re.search(r'srt$',file_name):
            name = '{}.srt'.format(name)
            pass
        else:
            pass
        os.rename('{}/{}'.format(folder_name,file_name),'{}/{}'.format(folder_name,name))

    pass
    

def rename_Suits(folder_name):
    # rename Logic 
    print("Enter Main Title of the Web Series :")
    series_name = input()
    print("Enter Season Number Padding :")
    season_padding = '0{}'.format(input())
    print("Enter Episode Number Padding :")
    episode_padding = '0{}'.format(input())
    for file_name in os.listdir(folder_name):
        season = -1
        episode = -1
        episode_name = -1
        if len(re.findall(r'- (\d+)x(\d+) -( (.*?)\.)',file_name)): # Suits - 5x04 - No Puedo Hacerlo.HDTV.ASAP.en.mp4
            temp = re.findall(r'- (\d+)x(\d+) -( (.*?)\.)',file_name)[0]
            season = temp[0]
            episode = temp[1]
            episode_name = temp[-1]
        name = '{} {} {} {}'.format(series_name,format(int(season),season_padding),format(int(episode),episode_padding),episode_name)
        if re.search(r'mp4$',file_name):
            name = '{}.mp4'.format(name)
        elif re.search(r'srt$',file_name):
            name = '{}.srt'.format(name)
            pass
        else:
            pass
        os.rename('{}/{}'.format(folder_name,file_name),'{}/{}'.format(folder_name,name))
    pass
    

def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic
    print("Enter Main Title of the Web Series :")
    series_name = input()
    print("Enter Season Number Padding :")
    season_padding = '0{}'.format(input())
    print("Enter Episode Number Padding :")
    episode_padding = '0{}'.format(input())
    for file_name in os.listdir(folder_name):
        if re.search(r'^(How I Met Your Mother)',file_name):
            season = -1
            episode = -1
            episode_name = -1
            if len(re.findall(r'- (\d+)x(\d+) (- (.*?)\.)',file_name)): # How I Met Your Mother - 6x08 - Natural History.1080p.HDTV.1080p x265.en.mp4
                temp = re.findall(r'- (\d+)x(\d+) (- (.*?)\.)',file_name)[0]
                season=temp[0]
                episode=temp[1]
                episode_name=temp[-1]
            if len(re.findall(r'- (\d+)x(\d+)-(\d+) (- (.*?) \(\d+\))',file_name)): # How I Met Your Mother - 7x23-24 - The Magician's Code (1).HDTV.LOL.en.srt
                temp = re.findall(r'- (\d+)x(\d+)-(\d+) (- (.*?) \(\d+\))',file_name)[0]
                season=temp[0]
                episode=temp[1]
                episode_name=temp[-1]
            if len(re.findall(r'- (\d+)x(\d+)-(\d+) (- (.*?)\.)',file_name)): # How I Met Your Mother - 9x01-02 - The Locket.HDTV.en.mp4
                temp = re.findall(r'- (\d+)x(\d+)-(\d+) (- (.*?)\.)',file_name)[0]
                season=temp[0]
                episode=temp[1]
                episode_name=temp[-1]
            name = '{} {} {} {}'.format(series_name,format(int(season),season_padding),format(int(episode),episode_padding),episode_name)
            if re.search(r'mp4$',file_name):
                name = '{}.mp4'.format(name)
            elif re.search(r'srt$',file_name):
                name = '{}.srt'.format(name)
                pass
            else:
                pass
            os.rename('{}/{}'.format(folder_name,file_name),'{}/{}'.format(folder_name,name))
    pass