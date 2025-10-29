# import bisect

class Solution(object):

    def unwind_and_collect(self, stack, unwind_count=3):
        cursor = []
        if len(stack) > 2:
            cursor.append(stack.pop(0))
            cursor.append(stack[0])
            cursor.append(stack[1])
        print(sum(cursor))
        return sum(cursor)

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        T = log(target**3, 10) # modulo operation, O(1)

        print(T)

        closestvalue = -10000000000000000000000000
        
         #min operation, O(n), can be simplified to O(logn), To DO: Modulo 3 for each number

        # nums.sort()
        # sortednums = closest(nums, T/3)

        N=T/3+0.0

        #print(N)

        closest = sorted(nums, key=lambda x: abs(x - N))

        #print(closest)
        stack = closest
        
        result = self.unwind_and_collect(stack)

        # print(result)

        if result - target == 0:
            print("returned target")
            return result
        if abs(result - target) < abs(closestvalue - target):
            print("closest value achieved")
            closestvalue = result

        return closestvalue



"""
    def closest(sorted_nums, target):
        i = bisect.bisect_left(sorted_nums, target)
        if i == 0: 
        return sorted_nums[0]
        if i == len(sorted_nums): 
            return sorted_nums[-1]
        before, after = sorted_nums[i-1], sorted_nums[i]
        return before if abs(before - target) <= abs(after - target) else after

        # put into stack structure to pop first 3 elements

        #worm throwugh to find closest to target
        # *** OPTIMIZATION: zeros in the array are FREE O(n) time OR LESS??

        """
