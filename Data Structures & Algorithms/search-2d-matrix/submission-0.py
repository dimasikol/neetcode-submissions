class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while r >= l:
            m = l+(r-l)//2
            if self.func(matrix[m],target):
                ll = 0
                rr = len(matrix[m])-1
                while rr >= ll:
                    mm = ll+(rr-ll)//2
                    if matrix[m][mm] == target:
                          return True
                    elif matrix[m][mm] > target:
                        rr = mm - 1
                    else:
                        ll = mm + 1
                return False
            elif matrix[m][-1] > target:
                r = m - 1 
            else:
                l = m + 1
        return False

    def func(self,array,target):
            if array[0]<=target<=array[-1]:
                return True
            return False