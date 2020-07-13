s, num = input(), int(input())
bb = (num).to_bytes(2, byteorder="little")
sum_key = bb[0] + bb[1]
print("".join([chr(r + sum_key) for r in bytes(s, encoding="utf-8")]))