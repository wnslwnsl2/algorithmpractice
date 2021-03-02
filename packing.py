"""
캐리어 용량은 w로 정해져 있다.
이때 절박도를 최대화 할 수 있는 물건들의 목록을 계산하는 프로그램을 작성하시오

절박도와 w
캐리어 용량을 캐시로 사용하는 것
"""

class Item:
    def __init__(self,name,volume,value):
        self.name = name
        self.volume = volume
        self.value = value

    def __str__(self):
        return '{},{},{}'.format(self.name,self.volume,self.value)

    def __repr__(self):
        return '{},{},{}'.format(self.name,self.volume,self.value)


class packingSolver:
    def __init__(self,items,max_volume):
        self.items = items
        self.max_volume = max_volume
        self.n = len(self.items)
        self.max_value = 0
        self.selected_item = []

        self.cache = []

    def solve(self):
        self.cache = [-1 for i in range(2**self.n)]
        self.max_value = self.__get_max_value(0,self.max_volume)
        self.__find_item(0,self.max_value)

    def __get_max_value(self,choiced,cur_max_volume):
        if self.cache[choiced]!=-1:
            return self.cache[choiced]

        ret = 0
        for index,item in enumerate(self.items):
            item_bit = 2**index
            if (choiced&item_bit != item_bit
                    and cur_max_volume >= item.volume):
                ret = max(ret,item.value+self.__get_max_value(choiced+item_bit,cur_max_volume-item.volume))
        self.cache[choiced] = ret
        return ret

    def __find_item(self,choiced,cur_max_value):
        if cur_max_value == 0:
            return

        for index,item in enumerate(self.items):
            item_bit = 2**index
            if choiced&item_bit!=item_bit:
                if self.cache[choiced] == item.value + self.cache[choiced+item_bit]:
                    self.selected_item.append(item)
                    self.__find_item(choiced+item_bit,cur_max_value-item.value)
                    return ##

    def __str__(self):
        return '최고 가치:{}\n선택된 아이템의 수:{}\n선택된 아이템 목록\n{}'.format(self.max_value,len(self.selected_item),'\n'.join(map(str,self.selected_item)))

    def __repr__(self):
        return str(self.items)

class Solver:
    def __init__(self,problem):
        self.case = 0
        packingSolvers = self.understand_problem(problem)

        for packingSolver in packingSolvers:
            packingSolver.solve()
            print(packingSolver)


    # 문제를 분석해서 해당 문제에 대한 클래스들을 return 한다.
    def understand_problem(self,problem):
        lines = problem.split('\n')
        self.case = int(lines[0])

        start = 1
        packingSolvers=[]
        while(start<len(lines)):
            items = []
            len_items,max_volume = tuple(map(int,lines[start].split()))
            for i in range(len_items):
                item_index = start+i+1
                name,volume_str,value_str = lines[item_index].split()
                items.append(Item(name,int(volume_str),int(value_str)))
            packingSolvers.append(packingSolver(items,max_volume))
            start=start+len_items+1
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
encyclopedia 10 4"""

s = Solver(problem)