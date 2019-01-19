class Stack(object):

    # 构建数组
    def __init__(self,data):
        self.array = data

    # 依据下标奇偶将数组分为两个栈 array[0] array[1]
    def divArray(self):
        array1 = []
        array2 = []
        for i in range(0,len(self.array), 2):
            array1.append(self.array[i])
        for i in range(1, len(self.array), 2):
            array2.append(self.array[i])
        return array1,array2

    # 左侧删除 弹出
    def l_pop(self):
        array1 = self.divArray()[0]
        print(array1)
        # 判断array[0]是否为空
        if len(array1) == 0:
            print('Stack array1 is empty')
        else:
            array1.pop(0)
            print(array1)

    # 左侧插入 压栈
    def l_push(self, data):
        array1 = self.divArray()[0]
        array1.insert(0, data)
        print(array1)

    # 右侧删除 弹出
    def r_pop(self):
        array2 = self.divArray()[1]
        # 判断array[1]是否为空
        if len(array2) == 0:
            print('Stack array2 is empty')
        else:
            array2.pop()
            print(array2)

    # 右侧插入 压栈
    def r_push(self, data):
        array2 = self.divArray()[1]
        array2.append(data)
        print(array2)


data = [1,2,3,4,5,6,7,8]
s = Stack(data)

s.l_pop()  #[2, 4, 6]

s.l_push('a')  # ['a', 0, 2, 4, 6]

s.r_pop() # [1, 3, 5]

s.r_push('b') #[1, 3, 5, 7, 'b']
