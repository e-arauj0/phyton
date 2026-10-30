# import time, random, qrcode

# print("Aguarde...")
# time.sleep(4)
# print("pronto")

# while True:
#     numero_aleatorio = random.randint(1, 50)
#     print(numero_aleatorio)
#     time.sleep(1)

#     if numero_aleatorio % 2 == 0:
#         break

#biblioteca externa
#pip install qrcode (no terminal)
#pip install pillow (no termina) para imagens
#cria qr code usando python

import qrcode

img = qrcode.make("https://github.com/e-arauj0/phyton")
img.save("qr_github.png")