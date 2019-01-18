def Sumab(array1,array2):
    len1 = len(array1)
    len2 = len(array2)
    # 两种情况，第一种：数组1的长度小于数组2的长度，第二种情况反过来。
    if len1 <= len2:
        # 较大和较小的数组长度
        minlen = len1
        maxlen = len2
        # 新建立一个与较长数组长度一致的全为0的数组
        ans = [0 for x in range(maxlen)]
        # 数组的后一部分保存较短数组的值
        ans[-minlen:] = array1
        for i in range(1,maxlen+1):
            # 从数组尾部开始算
            i = -i
            temp = ans[i] + array2[i]
            # 如果和大于10，则保留个位数值，并进位
            if temp >= 10:
                temp = temp - 10
                ans[i] = temp
                # 数组的第一位，进位后超出数组范围，用python的insert函数，在数组前插入数值
                if i == -maxlen:                   
                    ans.insert(0,1)
                # 如果没有超出数组范围，则直接在新建的数组的前一位加1
                else:
                    ans[i-1] = ans[i-1] + 1
            else:
                ans[i] = temp
    # 第二种情况
    else:
        minlen = len2
        maxlen = len1
        ans = [0 for x in range(maxlen)]
        ans[-minlen:] = array2
        for i in range(1,maxlen+1):
            i = -i
            temp = ans[i] + array1[i]
            if temp >= 10:
                temp = temp - 10
                ans[i] = temp
                if i == -maxlen:                    
                    ans.insert(0,1)
                else:
                    ans[i-1] = ans[i-1] + 1
            else:
                ans[i] = temp
    return ans
#测试用例
array1 = [2,1,4,8,0,0,0,0,0,0]
array2 = [2,1,4,9,0,0,0,0,0,0]
print(Sumab(array1,array2))