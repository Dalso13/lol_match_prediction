import os
import requests

# TODO:가장 먼저 실행
def get_puuid_data(api_key):
    userDatas = requests.get(f"https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/MASTER/I?page=1&api_key={api_key}")

    # TODO:천상계 Summonerid들 가져오기
    if userDatas.status_code != 200:
        print("api error(Summonerid)", userDatas.status_code)
        exit()

    userSummonerDatas = []
    for data in userDatas.json()[:50]:
        userSummonerDatas.append(data["summonerId"])

    userPUUIDs = []

    # TODO:Summonerid로 puuid들 가져오기

    for userData in userSummonerDatas:
        puuids = requests.get("https://kr.api.riotgames.com/tft/summoner/v1/summoners/" + userData +
                              "?api_key=" + api_key)
        if puuids.status_code != 200:
            print("api error(puuid)", puuids.status_code)
            break
        userPUUIDs.append(puuids.json()["puuid"])

    if os.path.isfile("API/user_puuid_data.json"):
        with open("API/user_puuid_data.json", 'w') as f:
            # 수정된 내용으로 파일을 덮어씁니다.
            f.write("")

    # TODO: JSON 파일로 저장
    with open("API/user_puuid_data.json", "a+") as f:
        f.write("[\n")
        a = ""
        for ppid in userPUUIDs:
            a += '\t"' + ppid + '",\n'
        f.write(a[:-2] + "\n]")
