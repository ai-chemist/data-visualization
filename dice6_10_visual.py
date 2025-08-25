import plotly.express as px

from dice import Dice
from pathlib import Path

# 6면체 주사위와 10면체 주사위 생성
dice_6 = Dice()
dice_10 = Dice(10)

# N회 굴린 결과 리스트에 저장
results = []

for roll in range(100_000):
    result = dice_6.roll() + dice_10.roll()
    results.append(result)

# 결과 분석
frequencies = []
max_result = dice_6.sides + dice_10.sides

poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 결과 시각화
title = 'Result of Rolling D6 and D10 100,000 Times'
labels = {'x' : 'Result', 'y' : 'Frequency'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)

# fig.show()

# html 파일로 저장 - Path 객체 사용 가능
path = Path('dice_visualize.html')
# fig.write_html('dice_visualize.html')
fig.write_html(path)