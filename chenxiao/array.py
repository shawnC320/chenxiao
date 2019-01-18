class Stack(object):


    # 构建两个空栈 array[0] array[1]
    def __init__(self):
        self.array = [[], []]

    # 左侧删除 弹出
    def l_pop(self):
        # 判断array[0]是否为空
        if len(self.array[0]) == 0:
            print('Stack b is empty')
        else:
            self.array[0].pop(0)

    # 左侧插入 压栈
    def l_push(self, data):
        self.array[0].insert(0, data)
 
    # 右侧删除 弹出
    def r_pop(self):
        # 判断array[1]是否为空
        if len(self.array[1]) == 0:
            print('Stack a is empty')
        else:
            self.array[1].pop()

    # 右侧插入 压栈
    def r_push(self, data):
        self.array[1].append(data)
