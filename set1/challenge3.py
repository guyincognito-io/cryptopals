import helper

cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

output = helper.findSingleByteXorChar(cipher)
print output
print output[1].decode('hex')


