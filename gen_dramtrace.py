for i in range(0, 2048 * 64, 64):
  for j in range(16):
    print("0x{:08x} R".format(j << 28 | i))