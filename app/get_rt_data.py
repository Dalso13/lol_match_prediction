import requests
import app.get_rt_match_param as gp

def get_puuid(name,tagline, api_key):
    request = requests.get("https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"+name+"/"+tagline+"?api_key="+api_key)
    if request.status_code != 200:
        print(request.status_code)
        raise Exception("이름,태그가 잘못되었습니다.")

    data = request.json()
    print(data['puuid'])

    return data['puuid']

def get_game_data(puuid, api_key):
    request = requests.get("https://kr.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/"+puuid+"?api_key="+api_key)
    if request.status_code != 200:
        print(request.status_code)
        raise Exception("현재 게임중이 아니거나, 관전하기 비활성화 상태입니다..")
    
    # 데이터를 확인해봐야하는데 볼수있는 경우가 별로 없음
    # TODO: 아마 디도스 때문에 실시간 관전을 막아둔거 같음 ㅠ
    data = request.json()

    return gp.getMatchParam(json=data)

if __name__ == "__main__":
    pass