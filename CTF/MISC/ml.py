def main():
    while 1:
        print('-' * 134)
        print('\t1.show source code')
        print('\t2.give me the source pictures')
        print('\t3.upload picture')
        print('\t4.exit')
        choose = input('>')
        if choose == '1':
            w = open('run.py','r')
            print(w.read())
            continue
        elif choose == '2':
            print('this is horse`s picture:')
            h = base64.b64encode(open('horse.png','rb').read())
            print(h.decode())
            print('-'*134)
            print('this is deer`s picture:')
            d = base64.b64encode(open('deer.png', 'rb').read())
            print(d.decode())
            continue
        elif choose == '4':
            break
        elif choose == '3':
            print('Please input your deer picture`s base64(Preferably in png format)')
            pic = input('>')
            try:
                pic = base64.b64decode(pic)
            except:
            	exit()
            if b"<?php" in pic or b'eval' in pic:
                print("Hacker!!This is not WEB,It`s Just a misc!!!")
                exit()
            salt = str(random.getrandbits(15))
            pic_name = 'tmp_'+salt+'.png'
            tmp_pic = open(pic_name,'wb')
            tmp_pic.write(pic)
            tmp_pic.close()
            if check(pic_name)>=100000:
                print('Don`t give me the horse source picture!!!')
                os.remove(pic_name)
                break
            ma = load_horse()
            lu = load_deer()
            k = 1
            trainingSet = np.append(ma, lu).reshape(2, 5185)
            testSet = load_test(pic_name)
            neighbors = getNeighbors(trainingSet, testSet[0], k)
            result = getResponse(neighbors)
            if repr(result) == '0':
                os.system('clear')

#m
iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAAAAABwhuybAAAFeElEQVR4nO2Xy28TVxTGvzN2ZpLYIY5dkgImIU4I2DFqQqiaqGpL2gXqv8AC2lUX/BFl032lSpWqblqpGyQ2LQhERQhUDSqk4ZnEtHnxCATn4TjP8fOeLmZszzPEUpeclefeM7/z3e/OfRh4G/9n+Dtk907v7jnKh42vc6690u5BTe/u1FsFyEPVgGoaqkAbw+pR5+m5689dq+5QxApSWjuO/DhbGoRgU6dcv7E7UH1472EUw2fuFDVS8e+UKblmX3JXoHBfiEKAOJjSClPOOpTOp2k3kCG19aN3IADA08habGyZk7nxRN2bFTWc8AuEWiWADtG8AIAF1ZLNrZ77SwynqIAa19cpHpMZgLddmcsTCpmwBACFZLGcFQ69TKoaivPragVKxl/9Z/YI/WlxRiVtoKC1qyoAtJzyAgAx66+LrWdPNu2KGL2n/el6vaFZntogzUBS8wCALXUPA2CQXl0KBPbdXtFfN5gdPxt68M210lNTNFj6mSxooJdWX5ibB3w20JEv9vLMqyeFUlJDtEX7pb4kSZIInFi3rTZuOWIdWuTLfUJiVNxjpUuZFwA8xwVAUzNYvTvgs03ZoYRqAsW+CgnAh3rDWL3t8tMCULMfAD0H8CxzbH+NQQ4A9jeYQF3fHR1LE/fXdHkMNaWD8kyGwAAKaQBIpkJBWRsf1YeCEgOSvmtqrW3fnxTp+2kiYov21alNAkDL1zLWQdW2xQMMcX1eKwoA9edPFjnQG2AWVg+CsSAA8LSNg8w/N1cq7ksA8P7nAuBAT4CJyDwz3HC0BcCLaRsHwModtZztBYC4XwDgpt6RJY/gBo+JVNslL6/N+f12Tl59PRczgXQsN937SRY43StM+d5ION9nx5DILSeWyqvQCwDjmz4GQBt/LQIYOqqYX5FqXTaPgz3p5flSEgDcveohgDyXRwFgctK2NbNzCA50HJYNoO2vL2xJ0uYv51UAyA5btyH3YBz4WPtEdXt8J7p5fGxbe1DO9QmXFx0i98NdA8gcvecUp2bnkB59m4XLSTsxUcUpye0H4AbKVeES2Bd2BWGyGklSozuoKknat+hSuSpJtAMod8NdkvPtxq1w4pFbD684XtuMZ78n3Fx+u7hWdKxMuZnNQFuNvcMI6vqk8h1yIzuBqHB58XgKDiTDAChSKyrheMJT4cpvOULqWX4nRZKX4Walzslf/bVAABw0WW9sBX222OFKTdlLV3Sj7SQLSEoOaQtfdMet0yalLo6UzmE7yaZoQ99BVItJxE8uJgCQv0ySjSm7u/kTide3bq0DQEenftmZHTvVZCC5ghjQ55S5sD1//552UwsNKAwAtPBHMnk2UCG5gho8QPbWGoGLanpxKau1Kv26iumRNYzCQLKCvB5NudzvFdL4BctqoN4IA6Dio9EMYCJZpka0HNNaYt0C6rB1VUXeAwBSR25rJ/joz6ul784AKqYBeD/o8QCQB+sgjScsnOCAAkBKDz0snYujQ6U+o6KHrwio6WsuCbppEaQMBBmgV9dmy84o7WScFz3SQwuE4sMlQD5ZB2li0syhnggDmP7d8D8i1i2gzllBSA0tiNGxAhCNOzjU3gOQeHBjzaBxsA7SZAKwzlrqRsu/RUAerBM2QcEBhUkdfVw0tEVjAupw1g7CygrgLEjpDzHSf84Zl4U8WCekSa2g0wfpKKgzwsgMvzC1RbvLghz3bEeH/B5QbtVaECVBTiD507KDO0c0LpC5mXUFxQyCDWG7XmqCJvQnu0dGBw2RXWPaNO1R0bhAplzQDup2FpSYZYhtW8GSIDtIcRaErBUdMwmyexSLOQqyhdkhh//9n/kEOQiyRfwYpKyhoA00PgU8frMg5C8JWp94c97bqMR/qKdMxhtIpukAAAAASUVORK5CYII=
#l
iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAAAAABwhuybAAAEXUlEQVR4nO2XS2xbRRSG/5l7b/xSb2wnDqbBSdU0FcQUmsRZVCAkorZJumkrFWEkWLJgyZINC5bsQQKEVAkhNRKJRKWqjUiFEAgUkYRQtYQ+ZCc4jzbk4dgkaWzfOSwSP+7D9r3Jtmc198ycz/+ZmTMzBp6Zc2N959wAXGdjDEDTxY6DggJfXT8FoOv7L/wArox/xG2FmUcpHsUNwKO4FYB3QNABQaCKyGi39pc9kKzT8p/Yb3pdfkhNSvTtpvu/2eLoQBfPfjkNAGh7+bTqlYIfs8aGha9XHYOkUyd7pgFAes/L8iIHldIzo4/scSpB2mPRpWYAwLtwK1EAINZW8jY5utQmzr8Uv5YB+MKnf9uNtwTdGbt8uWtW8tG4c44OVPiWBqJRiELSOUcHQvbqw4FjDR4qHBbU/mane0MJy+e2Z7VDgFj3W01ZhZFGL4bGx2wvVzG63IzF/TMjZwYYh0Dh1k2HpHKtxeIqJZcfaqRpRPLgkGI3cM9KqcXiKjHCfoWSPIiamviQd3KuspyL4FhcJcALLyuRampiJ4Y+OFMxL0VFvXGVAOpTTkg2NQktcGm5YsNxAGCxd/wAQIH+SElu3XkSgV6jotbXsptySNKfafXnCWGpvN1kANB+JzraLxnH1SVJFZMkA0BWcvlebTAfqSQPSjef1tJkAG0pA17F6mgm+XxoLCUseqxB9AveCO5lxhViABVjifd13vlzYctUepVZASiVCGsMKQAg2j8JCrDtmaelgYzl0umcEcQiR4jf/ax8TuzvI0qn9xrJxCsaoC3Pl9MjOdRiToUI5A8vlL6NJbP73bYQgrfplpCE2Qig1vejVUH46Z4EUIvfzrVIR989WRW0el0AcEdscADRfEmtBsKNJQ6g1WvrphYdxTIxgx7c5gCpYVuSwHtc1UDaaIYBUti4UayNwoFqIExMcQCyTZBbrQrKjhYA8cRWYQCSUhWEHxKySM7ZU1SqDdmiK/XNlfUnebsgVAfRyPNHWJljyJFZ/4IVCKnp/nK0K6iP3NmwDxK3OyNFkgi+rp/H3amUVYz123dlZL3UwbjevLE2+yDcu5ood+lTI48lyTI1ALPLvd3HJQBM7EqGsuOntUVTQI1FDn8YIIAt/2xYNmrpyUvB4pf2+d2aigAUCADY6o/GA7vVxRtEs8Fp74+G3hjn+X/WioDQwUEAWG5+bW9W+IXYYUBguflFAgBqjEftgaosB9u6NskAgPzHgZqTvR9Q5VnKVh4tsT4C9t9m9RSxjV+tSSKhZYcny3LrKGLp4T+sO9YXgcwwSk+kOorYxJTZ6eMAJXcAbN7IFDXVS23H7JLaGNjW3p2+W8r7AMvf/BwBqU2D9wCgdheQSxrvT+cgXwRgj1eMbuegVpUgEqY94RgkHeNg60smv2NQcwuB5syL6RjU7gLbmjP7nYJ8EQCpjLmjVokwTtxY+y80guUTpBtTD7Q95iF23+icBnb+1Y95UEPMM6uw/wEb7IPCRqC/gwAAAABJRU5ErkJggg==

