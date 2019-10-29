import paho.mqtt.client as mqtt

host = "canions.lab"
port = 1883

#chamado quando o broker responde à nossa solicitação de conexão
def on_connect(client, userdata, flags, rc):
    print("Resultado da conexão "+str(rc))

#criei uma instancia do Client
client = mqtt.Client()
#estou falando para a minha instancia que vou usar o on_connect deste arquivo
client.on_connect = on_connect

'''faço a conecção com o broker passando como parametro
(host, port, keepalive, bind_address), quando ele recebe uma respostas CONNACK,
do broker, ele gera como retorno uma chamada on_connect'''
client.connect(host, port, 60)

'''aqui eu faço a publicação de uma mensagem para o topico,
onde todos que forem assinantes desse topico, irão receber,
passando os parametros(topico, mensagem, qos, retain), ele gera um retorno
chamado de on_publish'''
client.publish('my/example','oi, aqui é um exemplo', 1, False)


'''essa é uma forma de bloqueio da rede e não retornará até que o cliente
ligue para desconectar. Ele liga automaticamente com a reconexão'''
client.loop_forever()
