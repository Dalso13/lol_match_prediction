import os

import requests
import json
import getAPI as api
import get_match_param as gp

# TODO: 세번째로 실행
# TODO: 매치id 데이터를 가져오기
with open("API/match_list_data.json", "r") as f:
    datas = json.load(f)

userDatas = []

for data in datas:
    userDatas.append(data["match"])

userMatchs = []

# TODO: 매치id로 게임정보들 가져오기
# TODO: 너무길어져서 메소드활용
for userData in userDatas:
    matchData = requests.get(
        "https://asia.api.riotgames.com/lol/match/v5/matches/" + userData + "?api_key=" + api.getAPIKEY())
    if matchData.status_code != 200:
        print("api error", matchData.status_code)
        exit()

    userMatchs.append(gp.getMatchParam(matchData.json()))

# TODO: 게임데이터 전처리후 csv파일로 저장
if os.path.isfile("API/match_data.csv"):
    with open("API/match_data.csv", 'w') as f:
        # 수정된 내용으로 파일을 덮어씁니다.
        f.write("")

print(userMatchs)

with open("API/match_data.csv", "a+") as f:
    text = 'total_gold, dragons, towers_destroyed, kills, win \n'
    for match in userMatchs:
        for data in match:
            for d in data:
                text += str(d)+","
            text = text[:-1]+"\n"
    f.write(text)