import os

import requests
import json
import getAPI as api

# TODO: 두번째로 실행

# TODO: puuid json 가져오기
with open("userPUUIDdata.json", "r") as f:
    datas = json.load(f)

userDatas = []

for data in datas:
    userDatas.append(data)

userMatchs = []

# TODO: puuid 로 게임매치id들 가져오기
for userData in userDatas:
    matchs = requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + userData +
                          "/ids?start=0&count=20&api_key=" + api.getAPIKEY())
    if matchs.status_code != 200:
        print(matchs.text)
        break
    for match in matchs.json():
        userMatchs.append(match)

print(userMatchs)

# TODO: 매치id들 저장
if os.path.isfile("matchListData.json"):
    with open("matchListData.json", 'w') as f:
        # 수정된 내용으로 파일을 덮어씁니다.
        f.write("")

with open("matchListData.json", "a+") as f:
    f.write("[\n")
    a = ""
    for match in userMatchs:
        a += '\t { "match" : ' + '"' + match + '"' + '},\n'
    f.write(a[:-2] + "\n]")
