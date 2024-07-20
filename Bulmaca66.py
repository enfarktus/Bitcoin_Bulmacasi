from bitcoin import *
import random
a=0

while(True):
    xx = random.randint(0x20000000000000000,0x3FFFFFFFFFFFFFFFF)
    priv = "%064x" % xx
    #print(str(a), priv)
    pub = privtopub(priv)
    pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
    addr = pubtoaddr(pubkey1)
    #print(addr)
    if addr == "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so":
        print("KAZANDIN")
        print(str(priv) + " " + addr)
        dosya=open("KAZANDIN.txt", "a")
        dosya.write(priv + " " + addr)
        dosya.close
    else:
        if addr.startswith("13z"):
            print(str(a), priv+" "+ addr)
    a+=1