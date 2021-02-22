#!/usr/bin/env python3

#https://bitcoin.stackexchange.com/questions/35848/recovering-private-key-when-someone-uses-the-same-k-twice-in-ecdsa-signatures
#https://crypto.stackexchange.com/questions/71764/is-it-safe-to-reuse-a-ecdsa-nonce-for-two-signatures-if-the-public-keys-are-diff

from ecdsa.numbertheory import inverse_mod
from Crypto.Util.number import long_to_bytes as lb
from Crypto.Cipher import AES

def attack(publicKeyOrderInteger, signaturePair1, signaturePair2, messageHash1, messageHash2):
    r1 = signaturePair1[0]
    s1 = signaturePair1[1]
    r2 = signaturePair2[0]
    s2 = signaturePair2[1]


    if (r1 != r2):
        print("ERROR: The signature pairs given are not susceptible to this attack")
        return None

    #A bit of Math
    #L1 = Hash(message_1)
    #L2 = Hash(message_2)
    #pk = Private Key (unknown to attacker)
    #R  = r1 == r2
    #K  = K value that was used (unknown to attacker)
    #N  = integer order of G (part of public key)

    #         From Signing Defintion
    #s1 = (L1 + pk * R) / K Mod N    and     s2 = (L2 + pk * R) / K Mod N

    #         Rearrange
    #K = (L1 + pk * R) / s1 Mod N    and     K = (L2 + pk * R) / s2 Mod N

    #         Set Equal
    #(L1 + pk * R) / s1 = (L2 + pk * R) / s2     Mod N

    #         Solve for pk (private key)
    #pk Mod N = (s2 * L1 - s1 * L2) / R * (s1 - s2)
    #pk Mod N = (s2 * L1 - s1 * L2) * (R * (s1 - s2)) ** -1

    numerator = (((s2 * messageHash1) % publicKeyOrderInteger) - ((s1 * messageHash2) % publicKeyOrderInteger))
    denominator = inverse_mod(r1 * ((s1 - s2) % publicKeyOrderInteger), publicKeyOrderInteger)

    privateKey = numerator * denominator % publicKeyOrderInteger

    return privateKey

private_key = attack(115792089210356248762697446949407573529996955224135760342422259061068512044369,
			(50394691958404671760038142322836584427075094292966481588111912351250929073849, 26685296872928422980209331126861228951100823826633336689685109679472227918891),
			(50394691958404671760038142322836584427075094292966481588111912351250929073849, 40762052781056121604891649645502377037837029273276315084687606790921202237960),
			777971358777664237997807487843929900983351335441289679035928005996851307115,
			91840683637030200077344423945857298017410109326488651848157059631440788354195)

print(private_key)

encrypted_flag = 'f3ccfd5877ec7eb886d5f9372e97224c43f4412ca8eaeb567f9b20dd5e0aabd5'
aes_key = int(private_key).to_bytes(64, byteorder='little')[0:16]
IV = b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'

cipher = AES.new(aes_key, AES.MODE_CBC, IV)
print(cipher.decrypt(bytes.fromhex(encrypted_flag)).decode())
#flag{cRypt0_c4r3fully}

