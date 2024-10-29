import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score


# 1. 데이터 불러오기 및 전처리
def load_and_prepare_data(file_path):
    # 데이터 불러오기
    match_data = pd.read_csv(file_path, sep=',')
    return match_data


# 2. 데이터 준비 및 학습 후 저장
def train_model(data):
    # 특성과 레이블 분리
    # pandas 안쓰고 그냥 numpy 써도 될거같은데 일단은 놔둠
    X = data[['blue_gold', 'blue_dragons', 'blue_towers_destroyed', 'blue_kills', 'blue_total_level', 'red_gold',
              'red_dragons', 'red_towers_destroyed', 'red_kills', 'red_total_level', 'game_duration']]
    y = data['win']

    # 데이터를 학습 및 테스트 세트로 분리
    # 원래 분리해서 모델 정확도 테스트 하는게 좋은데 데이터 아까워서 그냥 진행
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 로지스틱 회귀 모델 학습
    model = LogisticRegression(max_iter=500)
    model.fit(X, y)

    # 테스트 세트로 정확도 평가
    # y_pred = model.predict(X_test)
    # accuracy = accuracy_score(y_test, y_pred)
    # print(f"모델 정확도: {accuracy * 100:.2f}%")

    with open('LOL_pred_model', 'wb') as f:
        pickle.dump(model, f)


# 학습된 모델 가져오기
def get_train_model(path):
    with open(f"{path}", 'rb') as f:
        model = pickle.load(f)

    return model


# 3. 예측 함수
def predict_win_rate(model, match_datas):
    match_data_pd = pd.DataFrame([match_datas],
                                 columns=['blue_gold', 'blue_dragons', 'blue_towers_destroyed', 'blue_kills',
                                          'blue_total_level', 'red_gold', 'red_dragons', 'red_towers_destroyed',
                                          'red_kills', 'red_total_level', 'game_duration'])

    # 블루팀과 퍼플팀의 승리 확률 예측
    win_prob = model.predict_proba(match_data_pd)[0][1]

    # 결과 출력
    print(f"블루팀 승리 확률: {win_prob * 100:.2f}%")
    print(f"퍼플팀 승리 확률: {100 - win_prob * 100:.2f}%")


# 4. 사용자 입력 받기
def get_team_stats():
    teams = ["블루", "레드"]
    datas = []

    for team in teams:
        datas.append(int(input(f"{team}팀 의 총 골드량을 입력하세요: ")))
        datas.append(int(input(f"{team}팀 의 드래곤 처치 수를 입력하세요: ")))
        datas.append(int(input(f"{team}팀 의 킬 수를 입력하세요: ")))
        datas.append(int(input(f"{team}팀 의 타워 파괴 수를 입력하세요: ")))
        datas.append(int(input(f"{team}팀 의 총 레벨을 입력하세요: ")))
        print()

    minute = int(input("게임 진행 시간을 입력하세요 (분): "))
    second = int(input("(초): "))

    duration = minute * 60 + second
    datas.append(duration)

    return datas
