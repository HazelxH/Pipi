import random
import time


def create_list(num):  # 生成由num个元素组成的1-100之间的随机数
    clist = []
    for i in range(num):
        clist.append(random.randint(0, 99))
    return clist


class Sort():
    def __init__(self, queue):
        self.queue = queue

    def Bubbling(self):
        ''' 冒泡排序 '''
        a = time.time()
        list_len = len(self.queue)
        if list_len == 0 or list_len == 1:
            return self.queue
        for i in range(list_len):
            for n in range(list_len - i-1):
                if self.queue[n] > self.queue[n + 1]:
                    self.queue[n], self.queue[n + 1] = self.queue[n + 1], self.queue[n]
        b = time.time()
        c = b - a
        return c

    def Select(self):
        '''选择排序'''
        a = time.time()
        list_len = len(self.queue)
        if list_len == 0 or list_len == 1:
            return self.queue
        for i in range(list_len - 1, -1, -1):
            max_num = i
            for n in range(i):
                if self.queue[max_num] < self.queue[n]:
                    max_num = n
            self.queue[i], self.queue[max_num] = self.queue[max_num], self.queue[i]
        b = time.time()
        c = b - a
        return c

    def Insert(self):
        '''插入排序'''
        a = time.time()
        list_len = len(self.queue)
        if list_len == 0 or list_len == 1:
            return self.queue
        for i in range(list_len):
            for n in range(i,0,-1):
                if self.queue[n] < self.queue[n - 1]:
                    self.queue[n], self.queue[n - 1] = self.queue[n - 1], self.queue[n]
                else:
                    break
        b = time.time()
        c = b - a
        return c

    def Shell(self):
        '''希尔排序'''
        a = time.time()
        list_len = len(self.queue)
        if list_len == 0 or list_len == 1:
            return self.queue
        gap = list_len >> 1
        while gap > 0:
            for i in range(gap,list_len):
                insertx = self.queue[i]
                j = i - gap
                while j >= 0:
                    if insertx < self.queue[j]:
                        self.queue[j+gap] = self.queue[j]
                    else:
                        break
                    j -= gap
                self.queue[j + gap] = insertx
            gap >>= 1
        b = time.time()
        c = b - a
        return c

    def qcut(self, ldrop, rdrop):
        ''''分治'''
        k = ldrop
        j = ldrop
        while j < rdrop:
            if self.queue[j] < self.queue[rdrop]:
                self.queue[k], self.queue[j] = self.queue[j], self.queue[k]
                k += 1
            j += 1
        self.queue[k], self.queue[rdrop] = self.queue[rdrop], self.queue[k]
        return k

    def Quicksort(self, ldrop, rdrop):
        '''快速排序'''
        a = time.time()
        if ldrop < rdrop:
            drop = self.qcut(ldrop, rdrop)
            self.Quicksort(ldrop, drop - 1)
            self.Quicksort(drop + 1, rdrop)
        b = time.time()
        c = b - a
        return c

    def nod(self, nod,list_len):
        '''节点'''
        dad = nod
        son = 2 * dad + 1
        while son < list_len:
            if son + 1 < list_len and self.queue[son]<self.queue[son+1]:
                son += 1
            if self.queue[son] > self.queue[dad]:
                self.queue[son],self.queue[dad] = self.queue[dad],self.queue[son]
                dad = son
                son = 2*dad + 1
            else:
                break

    def Tree(self):
        '''堆排序'''
        a = time.time()
        list_len = len(self.queue)
        if list_len == 0 or list_len == 1:
            return self.queue
        for i in range(list_len//2-1,-1,-1):
            self.nod(i,list_len)
        self.queue[0],self.queue[list_len-1]=self.queue[list_len-1],self.queue[0]
        for i in range(list_len-1,1,-1):
            self.nod(0,i)
            self.queue[0], self.queue[i-1] = self.queue[i-1], self.queue[0]
        b = time.time()
        c = b - a
        return c

    def Count(self):
        '''计数排序'''
        a = time.time()
        max_num = max(self.queue)
        count = [0] * (max_num+1)
        for i in self.queue:
            count[i] += 1
        self.queue.clear()
        m = 0
        for n in count:
            if n != 0:
                self.queue = self.queue + n*[m]
            m += 1
        b = time.time()
        c = b - a
        return c


if __name__ == '__main__':
    z = 10000
    print('*' * 10)
    a = create_list(z)
    aa = Sort(a)
    print('冒泡排序耗时')
    print(aa.Bubbling())
    print('*' * 10)
    b = create_list(z)
    bb = Sort(b)
    print('选择排序耗时')
    print(bb.Select())
    print('*' * 10)
    c = create_list(z)
    cc = Sort(c)
    print('插入排序耗时')
    print(cc.Insert())
    print('*' * 10)
    d = create_list(z)
    dd = Sort(d)
    print('希尔耗时')
    print(dd.Shell())
    print('*' * 10)
    e = create_list(z)
    ee = Sort(e)
    print('快速耗时')
    print(ee.Quicksort(0,len(e)-1))
    print('*' * 10)
    f = create_list(z)
    ff = Sort(f)
    print('堆排序耗时')
    print(ff.Tree())
    print('*' * 10)
    g = create_list(z)
    gg = Sort(g)
    print('计数排序耗时')
    print(gg.Count())



