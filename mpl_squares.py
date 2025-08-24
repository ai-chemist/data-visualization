# 별칭으로 import
import matplotlib.pyplot as plt

# 입력 데이터의 유무에 따라 plot() 메서드의 동작 방식이 바뀜
input_values = [1, 2, 3, 4, 5]

squares = [1, 4, 9, 16, 25]

# print(plt.style.available) - matplotlib 에서 지원하는 내장 스타일 확인용

# 내장 스타일 사용하기
plt.style.use('bmh')
# fig = figure (그래프 컬렉션), ax (그래프 하나를 뜻함)
fig, ax = plt.subplots()

# 하나의 지점 강조 scatter(x, y, s) - x, y 좌표 값 전달, s 점의 크기
# ax.scatter(3, 9, s=200)
# 리스트도 전달 가능
ax.scatter(input_values, squares, s=100)

# linewidth 속성으로 선의 굵기 지정 - input_values 입력 데이터 지정
ax.plot(input_values, squares, linewidth=2)

# 그래프 타이틀을 지정하고 축에 이름 지정
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=16)
ax.set_ylabel("Square of Value", fontsize=16)

# 틱(Tick) - 눈금 이름표 크기 지정
ax.tick_params(labelsize=12)

plt.show()