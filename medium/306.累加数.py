#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#

# @lc code=start


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        res = []
        track = []
        length = len(num)

        def backtrack(track, num, index, track_index, add1_index, add2_index):

            if index > length + 1:
                return
            if len(''.join(track)) == len(num) and length == add2_index:
                print(track)
                for i in track:
                    # 101->true 1023->false
                    if i.startswith('0') and len(i) > 1:
                        res.append(False)
                        return
                res.append(True)
                return
            if int(num[add2_index:index]) == int(track[track_index]) + int(track[track_index - 1]):
                track.append((num[add2_index:index]))
                add1_index = len(''.join(track))
                add2_index = index
                track_index += 1
                backtrack(track, num, index + 1, track_index,
                          add1_index, add2_index)
                track.pop()
            else:
                backtrack(track, num, index + 1, track_index,
                          add1_index, add2_index)

        for i in range(length):
            for j in range(i + 2, length):
                # 固定track中前两个数，选择满足这两个数相加和相等的数
                track.append(num[0:i + 1])
                track.append(num[i + 1:j])
                backtrack(track, num, i + j + 1, 1, i, j)
                track.pop()
                track.pop()
        if len(res):
            return res[0]
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    res = s.isAdditiveNumber("199100199")
    print(res)
# @lc code=end
