import random
def find_ithele(l,r,k,array):
    """产生随机ｉｎｄｅｘ"""
    p=random.randint(l,r)
    array[p],array[l]=array[l],array[p]
    i=l
    j=r
    """
    遍历整个数组，寻找寻找第ｐ大的元素，它的左边都比它小，它的右边都比它大
    """
    while j>i:
        while j>i and array[l]<=array[j]:
            j-=1
        while j>i and array[l]>=array[i]:
            i+=1
        if j>i:
            array[i],array[j]=array[j],array[i]
    """交换第一个元素和第ｐ大的元素"""
    array[l],array[i]=array[i],array[l]
    if i==k-1:
        return array[i]
    if i>k-1:
        return find_ithele(l,i-1,k,array)
    if i<k-1:
        return find_ithele(i+1,r,k,array)

def main():
    array=[i for i in range(1000)]

    print(find_ithele(0,999,1000,array))


main()


