# Identifica erros

import logging

#INFO, DEBUG, WARNING, ERROR, CRITICAL - Niveis de mensagens
'''
logging.basicConfig(level=logging.INFO)
print("INFO")
logging.info("Mensagem informativa")
logging.debug("Mensagem de debug")
logging.error("Um erro aconteceu")
'''
# Debug só funciona quando no level é DEBUG

print(f'-'*30)
print("DEBUG")
#logging.basicConfig(level=logging.DEBUG)
# caso eu queira gravar a mensagem em um arquivo
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename="hello.log", level=logging.DEBUG, filemode="w", format=format)
#file mode é para subescrever 
logger = logging.getLogger(__name__)
logger = logging.getLogger(__file__) #Mostra o caminho do erro

logging.info("Mensagem informativa")
logging.debug("Mensagem de debug")
logging.error("Um erro aconteceu")

