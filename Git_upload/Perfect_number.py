class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        k=0
        for i in range(1,int(num/2)+1):
            if num%i==0:
                k=k+i
        if k==num:
            return True
        else:
            return False
