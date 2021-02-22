#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long
from bs4 import BeautifulSoup
import requests
import base64

url = "http://167.71.246.232:8080/crypto.php"


def oracle(padding):
	myobj = {
		"text_to_encrypt": padding,
		"do_encrypt": "Encrypt"
		}
	r = requests.post(url=url, data = myobj)
	soup = BeautifulSoup(r.text, 'html.parser')
	return base64.b64decode(soup.b.text).hex()


def second_block(blocks):
        return blocks[32:64]


flag = ""
for i in range(32):
        lookup_table = {}
        padding = ("A" * (31-i)) + flag

        for j in range(0x20, 0x7E):
                build_flag = padding + chr(j)
                blocks = oracle(build_flag)
                lookup_table[second_block(blocks)] = chr(j)

        n = oracle("A" * (31-i))
        flag += lookup_table[second_block(n)]
        print (flag)

        #if the flag is fully recoverd and it is actually shorter than full 32 chars
        if "}" in flag:
            break

print (flag)
#flag{b4d_bl0cks_for_g0nks}
