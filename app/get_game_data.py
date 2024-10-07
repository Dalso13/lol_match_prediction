import requests
import API.getAPI as API

def get_puuid(name,tagline):
    request = requests.get("https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"+name+"/"+tagline+"?api_key="+API.getAPIKEY())
    if request.status_code != 200:
        raise Exception("이름,태그가 잘못되었습니다.")

    data = request.json()

    return data['puuid']

def get_game_data(puuid):
    request = requests.get("https://kr.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/"+puuid+"?api_key="+API.getAPIKEY())
    if request.status_code != 200:
        raise Exception("현재 게임중이 아니거나, 관전하기 비활성화 상태입니다..")
    
    # 데이터를 확인해봐야하는데 볼수있는 경우가 별로 없음
    data = request.json()

    return []


if __name__ == "__main__":
    pass