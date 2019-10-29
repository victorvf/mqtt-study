'''Este módulo fornece algumas funções auxiliares para permitir a assinatura
direta(simple()) e o processamento de mensagens(callback())'''

port = 1883
hostname = "canion.labs"
topic = "my/example/test"

import paho.mqtt.subscribe as subscribe
mensagem = subscribe.simple(topic, hostname=hostname, port=port, qos=0)
print ('%s %s'%(mensagem.topic, mensagem.payload))

#a callback funciona da mesma forma, porém com uma função de retorno
def on_message_print(client, userdata, message):
    print("%s %s"%(message.topic, message.payload))

subscribe.callback(on_message_print, topic, hostname=hostname, port=port, qos=2)
