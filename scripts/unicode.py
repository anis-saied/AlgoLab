x="0x2789"
for i in range(10,20):
    x=hex(int(x,16)+1)
    print(chr(int(x,16)), end= " ")
    if i==19: print()
# ➊ ➋ ➌ ➍ ➎ ➏ ➐ ➑ ➒ ➓ 

