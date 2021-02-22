#!/usr/bin/env python3

import base64
import codecs

cipher = "NzMgNzkgNmUgNzQgN2IgNzAgNjIgNjEgNzQgNjUgNmUgNjcgNjYgNWYgNmMgNjIgNjggNWYgNzQgNjIgNjcgNWYgN2EgNzIgN2Q="

dec1 = bytes.fromhex(base64.b64decode(cipher).decode().replace(' ', '')).decode()
print(codecs.decode(dec1, "rot-13"))