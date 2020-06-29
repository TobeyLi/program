class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        因为是需要划分为两颗非空的树，所以这种直接判断的方式并不相同
        :param s1:
        :param s2:
        :return:
        """
        if len(s1)!=len(s2):
            return False

        N=len(s1)
        if N==0:
            return True
        if N==1:
            return s1==s2
        if sorted(s1)!=sorted(s2):
            return False
        for i in range(1,N):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            elif self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                return True
        return False






if __name__ == '__main__':
    solution=Solution()
    s1="aa"
    s2="ab"
    print(solution.isScramble(s1,s2))