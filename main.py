# 5. 전체 실행
import os
from dotenv import load_dotenv

import ML.ml_lol as ml
import app.get_rt_data as get_rt_data

def main():
    load_dotenv()
    api_key = str(os.environ.get("APIKEY"))

    # 모델 학습 or 가져오기
    if os.path.isfile("LOL_pred_model"):
        model = ml.get_train_model("LOL_pred_model")
    else:
        print("학습된 모델이 없기에 학습합니다.")
        # 파일 경로
        file_path = 'API/match_data.csv'

        # 데이터 불러오기 및 준비
        data = ml.load_and_prepare_data(file_path)

        ml.train_model(data)
        model = ml.get_train_model("LOL_pred_model")
    try:
        # 블루팀과 퍼플팀의 통계 입력 (사용자 입력 받기)
        blue_team_stats = ml.get_team_stats("블루팀")
        purple_team_stats = ml.get_team_stats("퍼플팀")
        # blue_team_stats = [33000, 1, 5, 9, 59, 1312]
        # purple_team_stats = [37600, 4, 6, 14, 59, 1312]

        # 승리 확률 예측
        ml.predict_win_rate(model, blue_team_stats, purple_team_stats)

        # realtime_data(api_key)
    except KeyboardInterrupt as e:
        print("강제종료")
   
# 실시간으로 가져올 경우
def realtime_data(api_key):
    name = input("닉네임을 입력하시오 (태그 X) : ")
    tag = input("태그를 입력하시오 (ex: KR1) : ")

    puuid = get_rt_data.get_puuid(name=name,tagline=tag, api_key=api_key)

    return get_rt_data.get_game_data(puuid=puuid, api_key=api_key)



if __name__ == "__main__":
    main()
