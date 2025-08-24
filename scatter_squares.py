import matplotlib.pyplot as plt

from pathlib import Path

path = Path('square_plot.png')

# 범위 지정 및 루프로 입력 값 설정
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('bmh')
fig, ax = plt.subplots()

# color=(r, g, b) 튜플을 인수로 지정해 색상 설정 가능 - 0.0 to 1.0 범위로 지정
# ax.scatter(x_values, y_values, color=(0.4, 0.8, 0.4), s=10)
# c(컬러맵과 연결할 값), cmap(사용할 컬러맵) 인수를 사용하여 컬러맵(colormap) 세트 사용 가능
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s=10)

# 그래프 타이틀, 이름표 설정
ax.set_title('Square Numbers', fontsize = 20)
ax.set_xlabel('Value', fontsize = 20)
ax.set_ylabel('Square', fontsize = 20)

# 틱 이름표 크기 지정
ax.tick_params(labelsize=16)

# 각 축의 범위 지정 [min_x, max_x, min_y, max_y] 순서로 할당
ax.axis([0, 1100, 0, 1_100_000])

# 1eN의 형태로 출력이 기본값 - ticklabel_format() 메서드를 통해 스타일 지정 가능
ax.ticklabel_format(style='plain')

# plt.show()

# 컴퓨터에 저장하기 - bbox_inchies='tight' (여분의 공백을 제거하는 옵션)
# plt.savefig('squares.png', bbox_inches='tight')

# Path 객체와 같이 사용 가능
plt.savefig(path, bbox_inches='tight')