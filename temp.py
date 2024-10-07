# 5. 전체 실행
import ML.ml_lol as ml

if __name__ == "__main__":
    # 파일 경로
    file_path = 'API/match_data.csv'

    # 데이터 불러오기 및 준비
    data = ml.load_and_prepare_data(file_path)

    # 모델 학습
    model = ml.train_model(data)
    try:
        # 블루팀과 퍼플팀의 통계 입력 (사용자 입력 받기)
        blue_team_stats = ml.get_team_stats("블루팀")
        purple_team_stats = ml.get_team_stats("퍼플팀")

        # 승리 확률 예측
        ml.predict_win_rate(model, blue_team_stats, purple_team_stats)

    except KeyboardInterrupt as e:
        print("강제종료")
