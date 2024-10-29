import os

import requests
import json
import get_match_param as gp

# TODO: 세번째로 실행
# TODO: 매치id 데이터를 가져오기
def get_match_csv_data(api_key, api_num=50, sqaure=0):
    with open("API/match_list_data.json", "r") as f:
        datas = json.load(f)

    userDatas = []

    for data in datas[api_num*sqaure:api_num+api_num*sqaure]:
        userDatas.append(data["match"])

    userMatchs = []

    # TODO: 매치id로 게임정보들 가져오기
    # TODO: 너무길어져서 메소드활용
    for userData in userDatas:
        matchData = requests.get(
            "https://asia.api.riotgames.com/lol/match/v5/matches/" + userData + "?api_key=" + api_key)
        if matchData.status_code != 200:
            print("api error", matchData.status_code)
            exit()

        userMatchs.append(gp.getMatchParam(matchData.json()))

    # TODO: 게임데이터 전처리후 csv파일로 저장
    if not os.path.isfile("API/match_data.csv"):
        with open("API/match_data.csv", 'w') as f:
            # 수정된 내용으로 파일을 덮어씁니다.
            f.write("blue_gold,blue_dragons,blue_towers_destroyed,blue_kills,blue_total_level,red_gold,red_dragons,red_towers_destroyed,red_kills,red_total_level,game_duration,win\n")

    with open("API/match_data.csv", "a+") as f:
        text = ""
        for match in userMatchs:
            for data in match:
                text += str(data)+","
            text = text[:-1]+"\n"
        f.write(text)