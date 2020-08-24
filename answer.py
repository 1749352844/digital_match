"""v2性能更优"""


def get_high_score(desk, mine):
    """获取最高分 -- 使用二分查找，需要对数组做排序"""
    # 结果集初始化 & 二分查找前的数组排序
    result, score = [], 0
    mine = quick_sort(arr=mine)
    # 获取编排后的数组 & 最高分
    for i in desk:
        status, index = binary_search(mine, num=i+1)
        if status:
            score += 1
        result.append(mine.pop(index))
    return result, score


def quick_sort(arr):
    """普通的递归版快速排序，O(nlogn)"""
    if len(arr) < 2:
        return arr
    # 选取中位数做基准值
    mid = arr[len(arr) // 2]
    # 定义基准值左右两个数组
    left, right = [], []
    # 从原始数组中移除基准值
    arr.remove(mid)
    for item in arr:
        # 大于基准值放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用迭代进行比较
    return quick_sort(left) + [mid] + quick_sort(right)


def binary_search(arr, num):
    """场景化的二分查找，O(nlogn)"""
    # 偏移量初始化
    first, last = 0, len(arr) - 1
    # 结果集状态和索引
    status, index = False, 0
    # 查找开始..
    while first <= last:
        mid = (last + first) // 2
        if arr[mid] > num:
            last = mid - 1
            status, index = True, mid
        elif arr[mid] < num:
            first = mid + 1
        else:
            return True, mid
    return status, index


def get_high_score_v2(desk, mine):
    """获取最高分2.0 -- 无需对数组做排序，遍历查+1数值"""

    # 结果集初始化
    result, score = [], 0
    # 获取编排后的数组 & 最高分
    for i in desk:
        eq_val, min_val, rel_val = loop_value(mine=mine, num=i+1)
        # 结果值非空则分数+1，否则追加最小值
        if rel_val is not None:
            result.append(rel_val)
            mine.remove(rel_val)
            score += 1
        else:
            result.append(min_val)
            mine.remove(min_val)
    return result, score


def loop_value(mine, num):
    """遍历取值"""
    # 初始化 -- 匹配值 & 最小值 & 结果值
    eq_val, min_val, rel_val = num, mine[0], None
    for item in mine:
        # 遍历到匹配值则中断循环
        if item == eq_val:
            rel_val = item
            break
        # 遍历到大于匹配值的则替换
        elif item > eq_val:
            if rel_val is None:
                rel_val = item
            elif item < rel_val:
                rel_val = item
        # 更新最小值(结果值为空，则使用最小值)
        if item < min_val:
            min_val = item
    return eq_val, min_val, rel_val
