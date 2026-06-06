#!/usr/bin/python3

print("".join("{:c}".format(i) if i % 2 == 0
              else "{:c}".format(i - 32)
              for i in range(122, 96, -1)), end="")
