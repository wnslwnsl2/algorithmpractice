"""
캐리어 용량은 w로 정해져 있다.
이때 절박도를 최대화 할 수 있는 물건들의 목록을 계산하는 프로그램을 작성하시오

절박도와 w
캐리어 용량을 캐시로 사용하는 것
"""

class item:
    def __init__(self,name,volume,value):
        self.name= name
        self.volume = volume
        self.value = value

class packingSolver:
    def __init__(self,items,max_volume):
        self.items = items
        self.max_volume = max_volume

class Solver:
    def __init__(self,problem):
        self.case = 0
        packingSolvers = self.understand_problem(problem)

    # 문제를 분석해서 해당 문제에 대한 클래스들을 return 한다.
    def understand_problem(self,problem):
        lines = problem.split('\n')
        self.case = int(lines[0])

        start = 1
        packingSolvers=[]
        while(start<len(lines)):
            items = []
            len_items,max_volume = tuple(lines[start].split())
            for i in range(len_items):
                item_index = start+i+1
                name,volume_str,value_str = lines[item_index].split()
                items.append(item(name,int(volume_str),int(value_str)))
            packingSolvers.append(packingSolver(items,max_volume))
        return packingSolvers



problem = """2
6 10
laptop 4 7
camera 2 10
xbox 6 6
grinder 4 7
dumbell 2 5
encyclopedia 10 4
6 17
laptop 4 7
camera 2 10
xbox 6 6
grinder 4 7
dumbell 2 5
encyclopedia 10 4
"""