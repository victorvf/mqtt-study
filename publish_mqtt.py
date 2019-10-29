'''Esse modulo prover a publicação de uma(single()) ou varias
mensagens(multiple()) e depois desconecta o cliente sem precisar de nada mais'''

hostname = 'canion.labs'
port = 1883

import paho.mqtt.publish as publish
#feita a publicação de uma única mensagem
publish.single("my/example/topic", "oi, teste", hostname=hostname, port=port)


'''feita a publicação de varias mensagens, dentro da mensagem eu posso passar
como parametro(topic, payload, qos, retain), os demais parametros vão na função multiple'''

mensagens = [{'topic':"my/example/topic1", 'payload':"mensagem de teste1", 'qos':2},
("my/example/topic2", "mensagem de teste2", 1, True)]
publish.multiple(mensagens, hostname=hostname, port=port)
