import os

import requests
import getAPI as api


# TODO:가장 먼저 실행
userDatas = requests.get("https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/MASTER/I?page=1"
                         + "&api_key=" + api.getAPIKEY())

# TODO:천상계 Summonerid들 가져오기
if userDatas.status_code != 200:
    print("api error", userDatas.status_code)
    exit()

userSummonerDatas = []
for data in userDatas.json():
    userSummonerDatas.append(data["summonerId"])

userPUUIDs = []

# TODO:Summonerid로 puuid들 가져오기

for userData in userSummonerDatas:
    puuids = requests.get("https://kr.api.riotgames.com/tft/summoner/v1/summoners/" + userData +
                          "?api_key=" + api.getAPIKEY())
    if puuids.status_code != 200:
        print("api error", puuids.status_code)
        break
    userPUUIDs.append(puuids.json()["puuid"])

if os.path.isfile("userPUUIDdata.json"):
    with open("userPUUIDdata.json", 'w') as f:
        # 수정된 내용으로 파일을 덮어씁니다.
        f.write("")

# TODO: JSON 파일로 저장
with open("userPUUIDdata.json", "a+") as f:
    f.write("[\n")
    a = ""
    for ppid in userPUUIDs:
        a += '\t"' + ppid + '",\n'
    f.write(a[:-2] + "\n]")
