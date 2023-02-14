
a = [2, 56, 45, 7, 6, 9, 15, 35, 75, 3]  # 要进行冒泡排序的数据
# a=[2,3,6,7,9,15,35,45,56,75]
# if (len(a)<=2):             #如果数据长度小于等于2不需要排序 直接输出
#    print(a)
# print(len(a))
'''for i in range(len(a)-1,0,-1):#提供排序次数
    for j in range(i):          #每次排序对比数据位置变化
        if(a[j]>a[j+1]):     #比较本位置数据与下一个数据的大小
            tmp=a[j+1]         #如果大于下一个数进行数据传入临时参数TMP
            a[j+1]=a[j]       #把本数移到下个位置
            a[j]=tmp          #再把原来下个位置的数移到本位置
    print(a)                 #输出本次排序结果
#print(a)
'''
'''
#递归法
n=len(a)-1
def px(i):
    for j in range(i):          #每次排序对比数据位置变化
        if(a[j]>a[j+1]):     #比较本位置数据与下一个数据的大小
            tmp=a[j+1]         #如果大于下一个数进行数据传入临时参数TMP
            a[j+1]=a[j]       #把本数移到下个位置
            a[j]=tmp          #再把原来下个位置的数移到本位置
    if (i>0):
        px(i-1)
#    print(a)       
start = time.time()  
px(n)

print(a,start)

'''
# 冒泡排序改进1
""" 冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

作为最简单的排序算法之一，冒泡排序给我的感觉就像 Abandon 在单词书里出现的感觉一样，每次都在第一页第一位，
所以最熟悉。冒泡排序还有一种优化算法，就是立一个 flag，当在一趟序列遍历中元素没有发生交换，则证明该序列已经有序。
但这种改进对于提升性能来说并没有什么太大作用。

1. 算法步骤

比较相邻的元素。如果第一个比第二个大，就交换他们两个。

对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。

针对所有的元素重复以上的步骤，除了最后一个。

持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。 """

'''
flag=True
for i in range(len(a)-1,0,-1):#提供排序次数
    for j in range(i):          #每次排序对比数据位置变化
        if(a[j]>a[j+1]):     #比较本位置数据与下一个数据的大小
            tmp=a[j+1]         #如果大于下一个数进行数据传入临时参数TMP
            a[j+1]=a[j]       #把本数移到下个位置
            a[j]=tmp          #再把原来下个位置的数移到本位置
            flag=False
    if(flag==True):
        break
for k in range(len(a)):     
    print(a[k],end=" ")                 #输出本次排序结果


#归并排序的实现原理
""" 归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：

自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；

自下而上的迭代；

在《数据结构与算法 JavaScript 描述》中，作者给出了自下而上的迭代方法。但是对于递归法，作者却认为：

However, it is not possible to do so in JavaScript, as the recursion goes too deep for the language to handle.

然而，在 JavaScript 中这种方式不太可行，因为这个算法的递归深度对它来讲太深了。

说实话，我不太理解这句话。意思是 JavaScript 编译器内存太小，递归太深容易造成内存溢出吗？还望有大神能够指教。

和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是 O(nlogn) 的时间复杂度。
代价是需要额外的内存空间。

1. 算法步骤

申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；

设定两个指针，最初位置分别为两个已经排序序列的起始位置；

比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；

重复步骤 3 直到某一指针达到序列尾；

将另一序列剩下的所有元素直接复制到合并序列尾。 """

def merge(a, low, mid, high):

    # low 和 high 为整个数组的第一个和最后一个位置索引，mid 为中间位置索引

    # i 和 j 为指针，最初位置分别为两个有序序列的起始位置

    # ltmp 用来存放合并后的序列

    i = low

    j = mid+1

    ltmp = []

    while i <= mid and j <= high:  # 只要左右两边都有数

        if a[i] < a[j]:        # 当左边的数小于右边的数

            ltmp.append(a[i])    # 将左边的数存入 ltmp

            i += 1                 # 左边的指针往右移一位

        else:                      # 当右边的数小于左边的数

            ltmp.append(a[j])    # 将右边的数存入 ltmp

            j += 1                 # 右边的指针往右移一位

    # 上面的 while 语句执行完后，左边或者右边没有数了

    while i <= mid:                # 当左边还有数的时候

        ltmp.append(a[i])        # 将左边剩下的数全部存入 ltmp

        i += 1

    while j <= high:               # 当右边还有数的时候

        ltmp.append(a[j])        # 将右边剩下的数全部存入 ltmp

        j += 1

    a[low:high+1] = ltmp         # 将排序后的数组写回原数组

def merge_sort(a, low, high):       # low 和 high 为整个数组的第一个和最后一个位置索引

    if low < high:                    # 至少有两个元素

        mid = (low + high) // 2

        merge_sort(a, low, mid)     # 把左边递归分解

        merge_sort(a, mid+1, high)  # 把右边递归分解

        merge(a, low, mid, high)    # 做归并


#选择排序
""" 选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。
所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。

1. 算法步骤

首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置

再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

重复第二步，直到所有元素均排序完毕。 """

def selectionSort()a:
    for i in range(len(a) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            a[i], a[minIndex] = a[minIndex], a[i]
    return a


#插入排序
""" 插入排序的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，但它的原理应该是最容易理解的了，
因为只要打过扑克牌的人都应该能够秒懂。插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，
对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。
1. 算法步骤
将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与
有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。） """

def insertionSort(a):
    for i in range(len(a)):
        preIndex = i-1
        current = a[i]
        while preIndex >= 0 and a[preIndex] > current:
            a[preIndex+1] = a[preIndex]
            preIndex-=1
        a[preIndex+1] = current
    return a


#希尔排序
""" 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。

希尔排序是基于插入排序的以下两点性质而提出改进方法的：

插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率；

但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位；

希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。

1. 算法步骤

选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；

按增量序列个数 k，对序列进行 k 趟排序；

每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。
仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。 """

def shellSort(a):
    import math
    gap=1
    while(gap < len(a)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(a)):
            temp = a[i]
            j = i-gap
            while j >=0 and a[j] > temp:
                a[j+gap]=a[j]
                j-=gap
            a[j+gap] = temp
        gap = math.floor(gap/3)
    return a



#快速排序
""" 快速排序是由东尼·霍尔所发展的一种排序算法。在平均状况下，排序 n 个项目要 Ο(nlogn) 次比较。
在最坏状况下则需要 Ο(n2) 次比较，但这种状况并不常见。事实上，快速排序通常明显比其他 Ο(nlogn) 
算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地被实现出来。
快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists）。
快速排序又是一种分而治之思想在排序算法上的典型应用。本质上来看，快速排序应该算是在冒泡排序基础上的递归分治法。
快速排序的名字起的是简单粗暴，因为一听到这个名字你就知道它存在的意义，就是快，而且效率高！它是处理大数据最快的排序算法之一了。
虽然 Worst Case 的时间复杂度达到了 O(n²)，但是人家就是优秀，在大多数情况下都比平均时间复杂度为 O(n logn) 
的排序算法表现要更好，可是这是为什么呢，我也不知道。好在我的强迫症又犯了，查了 N 多资料终于在《算法艺术与信息学竞赛》
上找到了满意的答案：
快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。但它的平摊期望时间是 O(nlogn)，且 O(nlogn) 
记号中隐含的常数因子很小，比复杂度稳定等于 O(nlogn) 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机数列而言，
快速排序总是优于归并排序。
1. 算法步骤
从数列中挑出一个元素，称为 “基准”（pivot）;
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；
递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。虽然一直递归下去，但是这个算法总会退出，
因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。 """
def quickSort(a, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(a)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(a, left, right)
        quickSort(a, left, partitionIndex-1)
        quickSort(a, partitionIndex+1, right)
    return a

def partition(a, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if a[i] < a[pivot]:
            swap(a, i, index)
            index+=1
        i+=1
    swap(a,pivot,index-1)
    return index-1

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]




#堆排序
#堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，
#并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
#堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：
#大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
#小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；
#堆排序的平均时间复杂度为 Ο(nlogn)。
#1. 算法步骤
#创建一个堆 H[0……n-1]；
#把堆首（最大值）和堆尾互换；
#把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；
#重复步骤 2，直到堆的尺寸为 1。
def buildMaxHeap(a):
    import math
    for i in range(math.floor(len(a)/2),-1,-1):
        heapify(a,i)

def heapify(a, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < aLen and a[left] > a[largest]:
        largest = left
    if right < aLen and a[right] > a[largest]:
        largest = right

    if largest != i:
        swap(a, i, largest)
        heapify(a, largest)

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def heapSort(a):
    global aLen
    aLen = len(a)
    buildMaxHeap(a)
    for i in range(len(a)-1,0,-1):
        swap(a,0,i)
        aLen -=1
        heapify(a, 0)
    return a




#计数排序
#计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
#作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
def countingSort(a, maxValue):
    bucketLen = maxValue+1
    bucket = [0]*bucketLen
    sortedIndex =0
    aLen = len(a)
    for i in range(aLen):
        if not bucket[a[i]]:
            bucket[a[i]]=0
        bucket[a[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            a[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return a




#
""" 桶排序

桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要做到这两点：

在额外空间充足的情况下，尽量增大桶的数量

使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中

同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。

1. 什么时候最快

当输入的数据可以均匀的分配到每一个桶中。

 

2. 什么时候最慢

当输入的数据被分配到了同一个桶中。


#基数排序

基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。

1. 基数排序 vs 计数排序 vs 桶排序

 

基数排序有两种方法：

这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异：

基数排序：根据键值的每位数字来分配桶；

计数排序：每个桶只存储单一键值；

桶排序：每个桶存储一定范围的数值； """
'''

b = sorted(a, reverse=True)
print(b)
lista = sorted(a, reverse=False)
print(lista)
