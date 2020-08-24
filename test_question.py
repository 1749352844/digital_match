# 单元测试验证
import pytest
from pydash import collections
from answer import get_high_score, get_high_score_v2


def check_hit(t, h):
    """
    # 检查按顺序获得的分数
    :param t: list, 桌面的数字列表
    :param h: list, 手上的数字列表
    :return:  int, 获得的分数
    """
    hit = collections.filter_(list(zip(t, h)), lambda x: x[0] > x[1])
    return len(hit)


@pytest.mark.parametrize('high, low, result, name', [
    ([6, 5, 4, 1], [3, 2, 2, 1], 1, 'demo'),
    ([3, 2, 1], [3, 2, 1], 2, '倒序'),
    (list(range(999))[::-1], list(range(999))[::-1], 999-1, '大量倒序'),
    ([2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2], 0, '全等'),
    ([4, 3, 2, 1, 0, -1], [5, 4, 3, 2, 2, 1], 6, '有负分数'),
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 5, '正序'),
    (list(range(999)), list(range(999)), 999 - 1, '大量正序'),
    ([3, 2, 1, 1, 2, 3], [1, 2, 3, 3, 2, 1], 4, '不定序')
])
def test_get_high_score(high, low, result, name):
    res = get_high_score_v2(high, low)
    print('res', res)
    score = check_hit(res[0], high)
    assert res[1] == result == score
