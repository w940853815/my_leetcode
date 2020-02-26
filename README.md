未独立解决的问题

- [21] 合并两个有序链表

![](https://github.com/w940853815/my_img/blob/master/img/21mergeTwoLists.jpg)

- [26] 删除排序数组中的重复项
一开始自己的思路，但是 function 函数中 for 循环只循环了两次？
```python
def function(nums):
    for n in nums:
        if nums.count(n) != 1:
            nums.remove(n)
    return len(nums)

if __name__ == '__main__':
    nums=[1,1,1,1]
    a=function(nums)
    for i in range(a):
        print(nums[i])
```
向v站提了这个问题https://www.v2ex.com/t/552743#reply7

> 有个解答明白了
> 第一,for 循环可以认为是根据索引的.
> 第二,remove 会移除第一个匹配项
> 当 remove 前两个 1 之后,nums[2]就不存在了,所以 for 循环直接结束.
  
## 回溯算法
```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```