# 랜덤 워크 시각화

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 재실행 없이 랜덤 워크 생성 반복
while True:
    # 랜덤 워크 생성
    rw = RandomWalk(100_000)
    rw.fill_walk()

    # 랜덤 워크 포인트 그리기
    plt.style.use('classic')

    # figsize 인수를 전달하여 그래프 크기 설정 가능, dpi 인수로 dpi 설정 가능 (기본값 = 100)
    fig, ax = plt.subplots(figsize=(12, 12), dpi=200)

    point_numbers = range(rw.num_points)

    # edgecolors 속성으로 포인트의 윤곽 제거
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolors='none', s=2)
    # ax.scatter(rw.x_values, rw.y_values, s=15)

    # set_aspect() 메서드에 equal 지정으로 x축 y축의 비율 같게 지정
    ax.set_aspect('equal')

    # 시작점과 끝점 강조 - plt.show() 직전에 사용하여 기존 그래프 위에 표시
    ax.scatter(0, 0, c='red', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=50)

    # 축 제거 - 메서드 체인 방식으로 사용
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("다른 랜덤워크를 생성? (y/n): ")
    if keep_running == 'n':
        break