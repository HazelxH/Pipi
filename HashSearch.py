import time
MAXKEY = 10000
count_table = []
class HashNode:
    '''哈希表节点'''
    def __init__(self,word,count):
        self.count = count
        self.word = word
        self.next = None

class HashTable:
    def __init__(self):
        self.table = [None] * MAXKEY
        self.word_indexs = []

    def hash(self,word):
        '''哈希函数'''
        h = 0
        g = 0
        for i in word:
            h = (h << 4) + ord(i)
            g = h & 0xf0000000
            if g:
                h ^= g >> 24
            h &= ~g
        return h % MAXKEY

    def add_word(self,word):
        index = self.hash(word)
        self.word_indexs.append(index)
        if self.table[index] is None:
            self.table[index] = HashNode(word,1)
            return
        node = self.table[index]
        while True:
            if node.word == word:
                node.count += 1
                return
            if node.next is None:
                break
            node = node.next
        new_node = HashNode(word,1)
        node.next = new_node

    def display_count(self):
        count_table = {}
        for index in list(set(self.word_indexs)):
            p = self.table[index]
            while p:
                count_table[p.word] = p.count
                p = p.next
        sorted_table = sorted(count_table.items(),key=lambda x:x[1],reverse=True)
        m = 1
        print('词频最高的前十个单词为')
        for key,value in sorted_table[0:10]:
            print('第%s多的单词为：' % m,end='')
            print(key,': ',value)
            m += 1

if __name__ == '__main__':
    a = time.time()
    file = open('./The_Holy_Bible.txt', mode='r', encoding='utf-8')
    temp = []
    while True:
        text = file.readline().lower()
        a = text.split(' ')
        temp = temp + a
        if not text:
            break
    file.close()
    split_word = ['\n', '"', ',', '.', '?', '"', '(', ')','\r\n']
    word_list = []
    for word in temp:
        for split_word in split_word:
            word = word.strip(split_word)
        word_list.append(word)
    n = 0
    while n < len(word_list):
        if word_list[n] == '':
            word_list.remove(word_list[n])
            n -= 1
        n += 1

    hash_table = HashTable()
    for word in word_list:
        hash_table.add_word(word)
    hash_table.display_count()
    b = time.time()
    c = b - a
    print(c)



