"""
Демоны захватили принцессу и заточили её в правом нижнем углу подземелья. Подземелье состоит из m x n комнат, расположенных в виде двумерной сетки. Наш отважный рыцарь изначально находится в левом верхнем углу и должен пробиться через подземелье, чтобы спасти принцессу.
У рыцаря есть начальное количество очков здоровья, представленное положительным целым числом. Если в какой-то момент его очки здоровья упадут до 0 или ниже, он немедленно умрёт.
Некоторые комнаты охраняются демонами (представлены отрицательными числами), поэтому рыцарь теряет здоровье, заходя в эти комнаты; другие комнаты либо пусты (представлены как 0), либо содержат магические шары, увеличивающие здоровье рыцаря (представлены положительными числами).
Чтобы как можно быстрее добраться до принцессы, рыцарь решает двигаться только вправо или вниз на каждом шаге.
Верните минимальное начальное количество здоровья рыцаря, чтобы он мог спасти принцессу.
Учтите, что любая комната может содержать угрозы или усиления, включая первую комнату, в которую входит рыцарь, и последнюю комнату, где заточена принцесса.
"""

"""
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
"""

from typing import List

class Solution(object):
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * cols for _ in range(rows)]

        def get_min_health(currCell: int, nextRow: int, nextCol: int) -> float:
            if nextRow >= rows or nextCol >= cols:
                return float("inf")
            nextCell = dp[nextRow][nextCol]
            return max(1, nextCell - currCell)

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                currCell = dungeon[row][col]

                right_health = get_min_health(currCell, row, col + 1)
                down_health = get_min_health(currCell, row + 1, col)
                next_health = min(right_health, down_health)

                if next_health != float("inf"):
                    min_health = next_health
                else:
                    min_health = 1 if currCell >= 0 else (1 - currCell)

                dp[row][col] = min_health

        return dp[0][0]
    

if __name__ == "__main__":
    instance = Solution()
    print(instance.calculateMinimumHP(dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]))  # Результат будет напечатан в консоль
