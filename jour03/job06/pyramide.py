ch = "abcdefghijklmnopqrstuvwxyz" * 10

i = 1
while i <= len(ch):
    print(ch[:i])
    ch=ch[i:]
    i += 1