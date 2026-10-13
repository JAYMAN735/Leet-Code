class Solution(object):
    def superpalindromesInRange(self, left, right):
        """
        :type left: str
        :type right: str
        :rtype: int
        """
        left = int(left)
        right = int(right)

        count = 0

        for i in range(1, 100000):
            s = str(i)

            # Generate odd-length palindrome
            odd = int(s + s[-2::-1])

            # Generate even-length palindrome
            even = int(s + s[::-1])

            for root in (odd, even):
                square = root * root

                if square > right:
                    continue

                if square >= left:
                    if str(square) == str(square)[::-1]:
                        count += 1

        return count