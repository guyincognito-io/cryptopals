import helper

plaintext = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

cipher = helper.encryptRepeatingKey(plaintext, "ICE")
print cipher.encode('hex')
