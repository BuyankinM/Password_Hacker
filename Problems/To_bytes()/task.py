val = int(input())
val_b = (val).to_bytes(length=2, byteorder="little")
print(sum(val_b))