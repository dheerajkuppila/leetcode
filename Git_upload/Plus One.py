class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k = ''
        for i in digits:
            k = k + str(i)
        j = int(k) + 1
        m = list()
        for i in str(j):
            m.append(int(i))
        return m

