import hashlib
import lief

binary = lief.parse("original_binary")
binary.remove_signature()
binary.write("binary.nosigned")


print(hashlib.sha256(open('binary.nosigned','rb').read()).hexdigest())