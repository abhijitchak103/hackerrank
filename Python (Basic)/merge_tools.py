def merge_the_tools(string, k):
    # your code goes here
    n = len(string)+1

    parts = [string[i:i+k] for i in range(0, n-1, k)]
    
    for part in parts:
        s = ""
        for i in range(len(part)):
            if part[i] not in s:
                s += part[i]
        print(s)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)