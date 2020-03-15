# Tools

* ATECC library: https://github.com/MicrochipTech/cryptoauthtools
* Docker image: https://hub.docker.com/r/ccamrobertson/atecc_python_pi

## Contracts:

* KongERC20: https://etherscan.io/address/0x177f2ace25f81fc50f9f6e9193adf5ac758e8098
* LockDrop: https://etherscan.io/address/0x9b9077a9d91941e20c0a5bbee463b9ba7114cadd
* EllipticCurve : https://etherscan.io/address/0xf471789937856d80e589f5996cf8b0511ddd9de4#code

## Sample Note

* Escrow: https://etherscan.io/address/0x6aba49f0ec8826570c28e4e3e9c9355b268605a6 

## Test Commands

```
$ PYTHON="docker run -it --rm --name atecc_test --device /dev/i2c-1 -v "$PWD":/usr/src -w /usr/src ccamrobertson/atecc_python_pi python"
$ $PYTHON info.py --iface i2c --device ecc -p bus=1 slave_address=0xc1
cfgfn cfg_ateccx08a_i2c_default
cfg.iface_type 0
cfg.devtype 2
cfg.wake_delay 1500
cfg.rx_retries 20
cfg.cfg.atcai2c.bus 1
cfg.cfg.atcai2c.slave_address 193
cfg.cfg.atcai2c.baud 400000
atcab_init status 0

Device Part:
    ATECC608A

Serial number: 
    01 23 BB FF 34 47 9C 32 EE

Configuration Zone:
    01 23 BB FF 00 00 60 02 34 47 9C 32 EE 01 21 00
    C0 00 00 68 89 A0 8A A0 89 A0 89 A0 89 A0 89 A0
    89 A0 89 A0 00 00 00 00 00 00 00 00 00 00 00 00
    00 00 00 00 FF FF FF FF 00 00 00 00 FF FF FF FF
    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    00 00 00 00 00 00 00 00 FC D9 00 00 00 00 00 00
    31 00 71 00 31 00 31 00 31 00 31 00 31 00 31 00
    1C 00 70 00 70 00 70 00 70 00 3C 00 3C 00 3C 00

Check Device Locks
    Config Zone is locked
    Data Zone is locked

Loading Public key

atcab_read_pubkey slot 9 bytearray(b'g\xa9n%\x02\xe3+\xf4.\xbc\x19\x94R\x90Z\xe8\xa9\r\xf0\x14\xa3I#\xa1\xdd\xca\x89\xbb\xc4vZ/G\x00)-\x1bj \xcf\x16_#\xefj"\x88O\xea2\xcb\xce#\xef\xfc[d$\xdf\x99\xe1\t\x9e\x0c')
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEZ6luJQLjK/QuvBmUUpBa6KkN8BSj
SSOh3cqJu8R2Wi9HACktG2ogzxZfI+9qIohP6jLLziPv/FtkJN+Z4QmeDA==
-----END PUBLIC KEY-----
atcab_read_pubkey slot 10 bytearray(b'\xab\x93_.W\x81\x80\xf0\xab\xbeA "\xca7\x98\xd6]<\x93g\xc4\x8e\xba\xc1{\xf6\xab4\xb4\xea\x80v\xb9Tfr\xc5\x9b\x9cG\x7f\xab\x07\xf7\x0c\' 9P{n\x9e-5 O\x1f\\\xc2\n\xe3\x01\xc6')
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEq5NfLleBgPCrvkEgIso3mNZdPJNn
xI66wXv2qzS06oB2uVRmcsWbnEd/qwf3DCcgOVB7bp4tNSBPH1zCCuMBxg==
-----END PUBLIC KEY-----
atcab_read_pubkey slot 12 bytearray(b'\xa08\x95\x0b@$V\xa9\xe0c\xe1/\x06\x95^j^\xbf\xcdB\xda\x1cV\xd5.\xa3\x02\xf6\x06\xf1K[S\x81\xef\xbc"\xad\xf2\x05*\xdc\xe1\xb73+\xa6 <m|RikG\xc8\xbd=\x17P\xdbJ\xb3]')
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEoDiVC0AkVqngY+EvBpVeal6/zULa
HFbVLqMC9gbxS1tTge+8Iq3yBSrc4bczK6YgPG18UmlrR8i9PRdQ20qzXQ==
-----END PUBLIC KEY-----
atcab_read_pubkey slot 13 bytearray(b'\xe2^\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE4l6AAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAP///////////////////////////////////////////////w==
-----END PUBLIC KEY-----

Done
```
