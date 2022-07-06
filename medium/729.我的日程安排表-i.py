#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#

# @lc code=start


class MyCalendar:
    def __init__(self):
        self.calendars = []

    def book(self, start: int, end: int) -> bool:
        is_add = all(
            [calendar[1] <= start or calendar[0] >= end for calendar in self.calendars]
        )
        if is_add:
            self.calendars.append([start, end])
        return is_add


# Your MyCalendar object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyCalendar()
    print(obj.book(10, 20))
    print(obj.book(15, 25))
    print(obj.book(20, 30))

# @lc code=end
