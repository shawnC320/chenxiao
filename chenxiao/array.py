class Stack(object):


    # 构建数组
    def __init__(self):
        self.array = []
        self.array1 = []
        self.array2 = []
        
    # 依据下标奇偶将数组分为两个栈 array1 array2
    def divArray(self):
        for i in range(len(self.array), 2):
            self.array1.append(i)
        for i in range(1, len(self.array), 2):
            self.array2.append(i)
            
    # 左侧删除 弹出
    def l_pop(self):
        # 判断array1是否为空
        if len(self.array1) == 0:
            print('Stack array1 is empty')
        else:
            self.array1.pop(0)

    # 左侧插入 压栈
    def l_push(self, data):
        self.array1.insert(0, data)
 
    # 右侧删除 弹出
    def r_pop(self):
        # 判断array2是否为空
        if len(self.array2) == 0:
            print('Stack array2 is empty')
        else:
            self.array2.pop()

    # 右侧插入 压栈
    def r_push(self, data):
        self.array2.append(data)
