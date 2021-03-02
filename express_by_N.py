def solve(N,number):
    s = Solver(N,number)
    return s.solve()

class Solver:
    def __init__(self,N,number):
        self.N = N
        self.number = number
        self.cache = [-2 for i in range(10**7)]

    def solve(self):
        return self.__get_min_count(0,0)

    # 현재 num일 때 최소의 숫자로 number를 만들 수 있는 연산의 수
    def __get_min_count(self,count,num):
        if count>8:
            return -1

        if num==self.number:
            return count

        if self.cache[num] != -2:
            return self.cache[num]

        ret = 10
        ## operation 구현

        for i in range(5):
            operNumber = int(str(self.N)*(i+1))
            cand = self.__get_min_count(count+1,num + operNumber)
            if cand != -1:
                ret = min(ret, cand)

            cand = self.__get_min_count(count+1,num - operNumber)
            if cand != -1:
                ret = min(ret, cand)

            cand = self.__get_min_count(count+1,num * operNumber)
            if cand != -1:
                ret = min(ret, cand)

            if num!=0:
                cand = self.__get_min_count(count+1,num % operNumber)
                if cand != -1:
                    ret = min(ret, cand)

            if ret>8:
                ret = -1

        self.cache[num] = ret
        return ret

print(solve(5,15))