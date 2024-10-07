# 5. 전체 실행
import ML.ml_lol as ml
import app.get_game_data as get_game_data

def main():
    # 파일 경로
    file_path = 'API/match_data.csv'

    # 데이터 불러오기 및 준비
    data = ml.load_and_prepare_data(file_path)

    # 모델 학습
    model = ml.train_model(data)
    try:

        # 임시로 임의에 데이터 가져오기
        a = [51000,2,11,6]
        b = [41700,1,1,2]

        ml.predict_win_rate(model, a, b)
    except KeyboardInterrupt as e:
        print("강제종료")
   

def realtime_data():
    name = input("닉네임을 입력하시오 (태그 X) : ")
    tag = input("태그를 입력하시오 (ex: KR1) : ")

    puuid = get_game_data.get_puuid(name=name,tagline=tag)

    return get_game_data.get_game_data(puuid=puuid)



if __name__ == "__main__":
    main()
