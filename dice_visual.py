import plotly.express as px

from dice import Dice

# 6면체 주사위 생성
dice_1 = Dice()

# 2번째 주사위 생성
dice_2 = Dice()

# n 회 굴린 결과를 리스트에 저장
results = []
for roll in range(1024):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# print(results)

# 결과 분석 - frequencies 리스트에 결과 담기
frequencies = []
max_result = dice_1.sides + dice_2.sides

# 1 to N 까지
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 결과를 시각화 - title, labels 변수에 저장 및 출력
title = 'Result of Rolling 2 Dices 1024 times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# 그래프 커스텀 - 막대에 이름표 부여 (xaxis_dtick=1) - x 축의 틱 기준을 1로 설정
fig.update_layout(xaxis_dtick=1)

# html 파일로 변환해서 표시
fig.show()

# print(frequencies)