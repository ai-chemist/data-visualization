# Random Walk - 일련의 랜덤한 결정에 따른 경로 생성

from random import choice

class RandomWalk:
    """랜덤 워크 클래스"""

    def __init__(self, num_points=5000):
        """초기화"""
        self.num_points = num_points

        # (0, 0)에서 시작
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """랜덤 워크 포인트 결정 메서드"""

        # 설정한 이동 수에 도달 시 까지 반복
        while len(self.x_values) < self.num_points:
            """direction -> 방향, distance -> 거리"""

            # 방향, 거리 설정
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 움직임이 없는 choice 제거
            if x_step == 0 and y_step == 0:
                continue

            # 새 위치 계산 - 다음 위치 계산에 필요
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)