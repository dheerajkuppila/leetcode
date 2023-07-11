class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        num1=''
        for i in num:
            num1=num1+str(i)
        k1=int(num1)+k
        m=list()
        for i in str(k1):
            m.append(int(i))
        return m