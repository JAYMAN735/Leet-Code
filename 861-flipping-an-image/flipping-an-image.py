class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in image:
            left=0
            right=len(row)-1

            while left<=right:
                new_left=1-row[right]
                new_right=1-row[left]

                row[left]=new_left
                row[right]=new_right

                left+=1
                right-=1

        return image