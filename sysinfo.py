import sys
import struct
import AColdWalk

print("Python " + sys.version)
print(str(8 * struct.calcsize("P")) + "bit")
print("---")
print("Platform: " + sys.platform)
print("---")
print("A Cold Walk Version: " + str(AColdWalk.__ver__))
