class Cipher(object):
    def __init__(self, d):
        self.encoder = d
        self.decoder = {}

        for key in self.encoder:
            value = self.encoder[key]
            self.decoder[value] = key


    def decode_message(self, message):
        return Cipher.code(message, self.decoder)


    def encode_message(self, message):
        return Cipher.code(message, self.encoder)


    def code(message, d):
        result = ''
        for c in message:
            if c in d:
                result += d[c]
            else:
                result += c
        return result


d = {
    'a': 's',
    's': 'p',
    'p': 'e',
    'e': 'x',
    'x': 'a',
    'm': 'g',
    'g': 't',
    't': 'r',
    'r': 'm',
}

cipher = Cipher(d)
text = 'this is a very good secret message.'
print('Our text is: ')
print(text)
print()
encoded = cipher.encode_message(text)
print('Our encoded text is: ')
print(encoded)
print()
decoded = cipher.decode_message(encoded)
print('After decoding, the message is: ')
print(decoded)
print()

