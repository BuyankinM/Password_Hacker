s = input()
print("".join([chr(bb + 1) for bb in s.encode()]))