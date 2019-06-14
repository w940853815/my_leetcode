
# 一瓶汽水1块钱，两个瓶子可以换一瓶汽水，4个盖子能换一瓶汽水，问：10块钱一共能买几瓶汽水
# qss换的汽水数
# kps空瓶数
# pgs瓶盖数
# pre_kps 兑换剩余空瓶数
# pre_pgs 兑换剩余瓶盖数
def water_count(qss):
    # import ipdb; ipdb.set_trace()
    kps  = qss
    pgs = qss
    sum =  qss
    while (kps >=2 and pgs >=4):
        # print("当前汽水数",qss,"当前空瓶数",kps,"当前瓶盖数",pgs)
        pre_kps = kps % 2
        pre_pgs = pgs % 4
        qss = kps // 2 + pgs // 4
        sum = sum + qss
        kps = qss + pre_kps
        pgs = qss + pre_pgs
        print('喝的汽水数',sum,"换的汽水数",qss,"空瓶数",kps,"上次兑换剩余空瓶数",pre_kps,"瓶盖数",pgs,"上次兑换剩余瓶盖数",pre_pgs)
    return  sum


if __name__ == "__main__":
    
    a = water_count(20)
    print(a)