import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 1. 데이터 불러오기 및 전처리
def load_and_prepare_data(file_path):
    # 데이터 불러오기
    match_data = pd.read_csv(file_path)

    return match_data

# 2. 데이터 준비 및 학습 후 저장
def train_model(data):
    # 특성과 레이블 분리
    X = data[['total_gold', 'dragons', 'kills', 'towers_destroyed']]
    y = data['win']
    
    # 데이터를 학습 및 테스트 세트로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 로지스틱 회귀 모델 학습
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # 테스트 세트로 정확도 평가
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"모델 정확도: {accuracy * 100:.2f}%")

    with open('LOL_pred_model', 'wb') as f:
        pickle.dump(model, f)

# 학습된 모델 가져오기
def get_train_model(path):
    with open(f"{path}", 'rb') as f:
        model = pickle.load(f)

    return model;

# 3. 예측 함수
def predict_win_rate(model, blue_team_stats, purple_team_stats):
    # 입력: 블루팀과 퍼플팀의 통계 (골드, 드래곤, 킬, 타워 파괴 수)
    blue_stats = pd.DataFrame([blue_team_stats], columns=['total_gold', 'dragons', 'kills', 'towers_destroyed'])
    purple_stats = pd.DataFrame([purple_team_stats], columns=['total_gold', 'dragons', 'kills', 'towers_destroyed'])
    
    # 블루팀과 퍼플팀의 승리 확률 예측
    blue_win_prob = model.predict_proba(blue_stats)[0][1]
    purple_win_prob = model.predict_proba(purple_stats)[0][1]
    
    # 결과 출력
    print(f"블루팀 승리 확률: {blue_win_prob * 100:.2f}%")
    print(f"퍼플팀 승리 확률: {purple_win_prob * 100:.2f}%")

# 4. 사용자 입력 받기
def get_team_stats(team_name):
    print(f"{team_name}의 정보를 입력하세요:")
    total_gold = int(input(f"{team_name}의 총 골드량을 입력하세요: "))
    dragons = int(input(f"{team_name}의 드래곤 처치 수를 입력하세요: "))
    kills = int(input(f"{team_name}의 킬 수를 입력하세요: "))
    towers_destroyed = int(input(f"{team_name}의 타워 파괴 수를 입력하세요: "))
    return [total_gold, dragons, kills, towers_destroyed]
