# ERROS e EXCEÇÕES
"""
NameError
ValueError
ZeroDivisionError
TypeError
IndexError
KeyError
EOFError
KeyboardInterrupt
OSError
MemoryError
ConnectionError
RuntimeError

fonte: \033[0;0m \033[0;0m https://docs.python.org/3/library/exceptions.html

try:
    operacao
except:
    falhou
else:
    deu certo
finally:
    certo/falha

"""

import verificalog

try:
    a = int(input('Numerador: '))
    b = int(input('Multiplicador: '))
    r = a / b
#except Exception as falha:
    #verificalog.detalhado(falha)
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except (ZeroDivisionError):
    print('Não é possível dividir por zero')
except (KeyboardInterrupt):
    print('O usuário preferiu não informar os dados')
except Exception as falha:
    print(f'O erro encontrado foi {falha.__cause__}')
else:
    print(f'{a} / {b} = {r}')
finally:
    print('\nVolte Sempre')