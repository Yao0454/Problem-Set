def find_min()-> None:
    n = int(input())
    nums = list(map(int, input().split()))
    min = 10000
    for i in nums:
        if i < min: min = i
    print(min)

def sort_three_nums() -> None:
    

if __name__ == "__main__":
    find_min()