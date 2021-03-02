"""
분류: 동적 계획법
문제: 모든 경로 중 포함된 숫자의 최대 합을 찾는 프로그램을 작성하세요

포인트
1) 문제 풀이 클래스 구조
2) 점화식 > 재귀문
3) Cache 사용
"""

"""
문제 인식해서 TriangleSolver로 실제 문제를 푼다.
"""
class Solver:
    def __init__(self,problem):
        self.triangles = self.__understand_problem(problem)

    def solve(self):
        ret = []
        for triangle in self.triangles:
            ts = TriangleSolver(triangle)
            ret.append(ts.get_max_line_sum())
        return ret

    def __understand_problem(self,problem):
        lines = problem.split('\n')
        triangles = []

        start = 1

        while(start<len(lines)):
            triangle, start = self.__make_triangle(lines,start)
            triangles.append(triangle)
        return triangles

    def __make_triangle(self,lines,start):
        n = int(lines[start])
        triangle_in_str = lines[start+1:start+n+1]
        triangle = [list(map(int,line.split())) for line in triangle_in_str]
        return triangle, start+n+1

"""
실제 문제를 푼다.
"""
class TriangleSolver:
    def __init__(self,triangle):
        self.triangle = triangle
        self.n = len(triangle)
        self.cache = []
        print(triangle)

    def get_max_line_sum(self):
        self.cache = [[-1 for col in range(self.n)] for row in range(self.n)]
        return self.__get_max_line_sum(0,0)

    def __get_max_line_sum(self,row,col):
        if self.cache[row][col] != -1:
            return self.cache[row][col]

        ret = self.triangle[row][col]

        if row != self.n-1:
            ret = ret + max(self.__get_max_line_sum(row+1,col),self.__get_max_line_sum(row+1,col+1))

        self.cache[row][col] = ret

        return ret


# 예제
problem="""2
5
6
1  2
3  7  4
9  4  1  7
2  7  5  9  4
5
1 
2 4
8 16 8
32 64 32 64
128 256 128 256 128"""

solver = Solver(problem)
print(solver.solve())