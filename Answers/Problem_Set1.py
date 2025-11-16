def find_min() -> None:
    """
    第一题：找最小值
    给定 n 个整数，找出其中的最小值
    
    输入格式:
    - 第一行: 一个正整数 n (1 ≤ n ≤ 100)
    - 第二行: n 个非负整数 (0 ≤ ai ≤ 1000)，以空格分隔
    """
    n = int(input())  # 读取数字个数
    nums = list(map(int, input().split()))  # 读取n个整数并转换为列表
    
    # 方法1：使用内置函数（推荐）
    print(min(nums))
    
    # 方法2：手动遍历（你的实现方式）
    # min_val = nums[0]  # 假设第一个数是最小值
    # for i in nums:
    #     if i < min_val: 
    #         min_val = i
    # print(min_val)


def sort_three_nums() -> None:
    """
    第二题：三位数排序
    给定三个整数，按从小到大顺序输出
    
    输入格式:
    - 一行: 三个整数 a, b, c (0 ≤ a, b, c ≤ 100)，以空格分隔
    """
    a, b, c = map(int, input().split())  # 读取三个整数
    
    # 方法1：使用内置排序（推荐）
    nums = [a, b, c]
    nums.sort()  # 原地排序
    print(nums[0], nums[1], nums[2])
    
    # 方法2：手动比较排序
    # if a > b: a, b = b, a  # 确保a <= b
    # if b > c: b, c = c, b  # 确保b <= c
    # if a > b: a, b = b, a  # 再次确保a <= b
    # print(a, b, c)


def days_in_month() -> None:
    """
    第三题：月份天数
    根据年份和月份计算该月的天数，需要考虑闰年
    
    输入格式:
    - 一行: 两个正整数 y, m，以空格分隔
      - y: 年份 (1583 ≤ y ≤ 2020)
      - m: 月份 (1 ≤ m ≤ 12)
    """
    y, m = map(int, input().split())  # 读取年份和月份
    
    # 每月天数（平年）
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 判断是否为闰年
    is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    
    # 如果是闰年且为2月，天数为29
    if is_leap and m == 2:
        print(29)
    else:
        print(days[m - 1])  # 数组索引从0开始，所以月份要减1


def count_digits() -> None:
    """
    第四题：计数问题
    计算在1到n的所有整数中，数字x出现了多少次
    
    输入格式:
    - 一行: 两个整数 n, x，以空格分隔
      - n: 正整数 (1 ≤ n ≤ 10^6)
      - x: 要统计的数字 (0 ≤ x ≤ 9)
    """
    n, x = map(int, input().split())  # 读取n和要统计的数字x
    
    count = 0
    # 遍历1到n的每个数
    for i in range(1, n + 1):
        # 将数字转换为字符串，统计字符x出现的次数
        count += str(i).count(str(x))
    
    print(count)


def series_sum() -> None:
    """
    第五题：级数求和
    找到最小的n，使得Sn = 1 + 1/2 + 1/3 + ... + 1/n > k
    
    输入格式:
    - 一行: 一个正整数 k (1 ≤ k ≤ 15)
    """
    k = int(input())  # 读取k
    
    n = 1
    s = 0.0  # 当前和
    
    # 逐步计算级数和，直到大于k
    while s <= k:
        s += 1.0 / n  # 加上1/n
        n += 1
    
    print(n - 1)  # 因为循环结束时n多加了1，所以要减1


def isbn_check() -> None:
    """
    第六题：ISBN号码
    检查ISBN号码的识别码是否正确
    
    输入格式:
    - 一行: 一个字符串，表示ISBN号码
      格式: x-xxx-xxxxx-x (如: 0-670-82162-4)
      - x: 首位数字 (0-9)
      - xxx: 三位出版社代码 (000-999)
      - xxxxx: 五位书籍编号 (00000-99999)  
      - x: 识别码 (0-9 或 X)
    """
    isbn = input().strip()  # 读取ISBN号码
    
    # 提取9位数字（去掉分隔符）
    digits = ""
    for char in isbn:
        if char.isdigit():
            digits += char
    
    # 计算校验码
    sum_val = 0
    for i in range(9):
        sum_val += int(digits[i]) * (i + 1)
    
    remainder = sum_val % 11
    
    # 确定正确的识别码
    if remainder == 10:
        correct_check = 'X'
    else:
        correct_check = str(remainder)
    
    # 获取输入的识别码（最后一位）
    input_check = isbn[-1]
    
    # 判断是否正确
    if input_check == correct_check:
        print("Right")
    else:
        # 输出正确的ISBN号码
        correct_isbn = isbn[:-1] + correct_check
        print(correct_isbn)


def is_prime(n) -> bool:
    """
    判断一个数是否为质数的辅助函数
    
    参数:
    - n: 待判断的正整数
    
    返回:
    - bool: 如果n是质数返回True，否则返回False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 只需要检查到sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_palindrome(n) -> bool:
    """
    判断一个数是否为回文数的辅助函数
    
    参数:
    - n: 待判断的正整数
    
    返回:
    - bool: 如果n是回文数返回True，否则返回False
    """
    s = str(n)
    return s == s[::-1]  # 字符串反转后是否相等


def palindrome_primes() -> None:
    """
    第七题：回文质数
    找出范围[a,b]间的所有回文质数
    
    输入格式:
    - 一行: 两个正整数 a, b，以空格分隔
      - a: 范围起始值 (5 ≤ a)
      - b: 范围结束值 (a < b ≤ 100,000,000)
    """
    a, b = map(int, input().split())  # 读取范围
    
    # 遍历范围内的每个数
    for num in range(a, b + 1):
        # 检查是否既是回文数又是质数
        if is_palindrome(num) and is_prime(num):
            print(num)


if __name__ == "__main__":
    # 根据需要调用相应的函数
    # 第一题
    # find_min()
    
    # 第二题
    # sort_three_nums()
    
    # 第三题
    # days_in_month()
    
    # 第四题
    # count_digits()
    
    # 第五题
    # series_sum()
    
    # 第六题
    # isbn_check()
    
    # 第七题
    # palindrome_primes()
    
    # 当前运行第一题
    find_min()