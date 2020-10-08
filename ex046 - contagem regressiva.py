# FOGOS ARTIFICIO
# contagem regressiva de 10 até 0, com uma pausa de 1 segundo

import time

for c in range (10, -1, -1):
    print (c)
    time.sleep(0.5)
print('BOOOM')