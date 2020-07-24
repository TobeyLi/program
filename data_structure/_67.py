
# 给定两个字符串，代表两个二进制数，将这两个二进制的数相加 得到一个新的二进制数

class Solution:
    def addBinary(self, a, b):
        """
        这里逻辑存在问题，不能直接是以>2来判断
        :param a:
        :param b:
        :return:
        """
        s=str(int(a)+int(b))
        new_res=""
        count=0
        for i in range(len(s)-1,-1,-1):
            if count==1:
                s=s.replace(s[i],str(int(s[i])+1))
                count=0
            if s[i] >='2':
                if i==0:
                    new_res += '01'
                    break
                new_res+='0'
                count+=1
            else:
                new_res+=s[i]

        final=""
        new_res=reversed(new_res)
        for i in new_res:
            final+=i
        return final

    def learn1(self,a,b):
        """
        直接通过python的特性来解决这样的问题
        :param a:
        :param b:
        :return:
        """
        x = int(a, 2)  # convert a into binary
        y = int(b, 2)  # convert b into binary
        z = bin(x + y)  # adds both integer converted values  and converts in into binary
        return z[2::]  # python binary prints 100 binary value like 0b100 slicing first 2 values returns the output

    def learn2(self,a,b):
        """
        抛弃语言特性的特征去学习该题，这种和自己的第一种做法比较类似，但是自己做的有问题，需要好好的学习
        :param a:
        :param b:
        :return:
        """
        res = ''

        carry = 0

        # Fix the difference in lengths
        while len(a) > len(b):
            b = '0' + b
        while len(b) > len(a):
            a = '0' + a

        ia = len(a) - 1
        ib = len(b) - 1

        # Do simple binary addition here
        while ia >= 0 and ib >= 0:
            sumi = int(a[ia]) + int(b[ib]) + carry
            if sumi == 1:
                carry = 0
                res += '1'
            elif sumi == 2:
                carry = 1
                res += '0'
            elif sumi == 3:
                carry = 1
                res += '1'
            else:
                carry = 0
                res += '0'

            ia -= 1
            ib -= 1

            # If carry is still one we might need to add 1 at the end
        if carry == 1:
            res += '1'

        # Reverse of the result gives the actual resultant binary string
        return res[::-1]


if __name__ == '__main__':
    s=Solution()
    print(s.addBinary('1111','1111'))
