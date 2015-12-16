#coding=utf-8
class Solution:
    # @param A, a list of integer
    # @return an integer

    # http://www.cnblogs.com/daijinqiao/p/3352893.html
    # 用ones记录到当前计算的变量为止，二进制1出现“1次”（mod 3 之后的 1）的数位。
    # 用twos记录到当前计算的变量为止，二进制1出现“2次”（mod 3 之后的 2）的数位。
    # 当ones和twos中的某一位同时为1时表示二进制1出现3次，此时需要清零。即用二进制模拟三进制计算。最终ones记录的是最终结果。
    def singleNumber(self, A):
        one = 0; two = 0; three = 0
        for i in A:
            # 要先计算two，因为它要用到上一个loop的one
            two |= i & one
            # one 就是做抑或运算
            one = i ^ one
            # 如果one和two在某一位都为1的话，那就证明这一位出现了3次，要清零。
            three = ~(one & two)
            # 出现了三次的位进行清零，否则不变 
            one &= three
            # 出现了三次的位进行清零，否则不变
            two &= three
        return one