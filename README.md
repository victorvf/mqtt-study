# MQTT (Message Queue Telemetry Transport)
Conceito:
> Protocolo de mensagem com suporte para a comunicação assíncrona entre as partes, leve e flexível que oferece o equilíbrio ideal para os desenvolvedores de IoT. Baseado no modelo de publish and subscribe

### Modelo Publish and Subscribe
1. O cliente conecta-se ao broker. Ele pode assinar qualquer "tópico" de mensagem do broker. Essa conexão pode ser uma conexão TCP/IP simples ou uma conexão TLS criptografada para mensagens sensíveis.
2. O cliente publica as mensagens em um tópico, enviando a mensagem e o tópico ao broker.
3. Em seguida, o broker encaminha a mensagem a todos os clientes que assinam esse tópico.

### Tipos de Mensagens
1. CONNECT
  - cleanSession
  - username
  - password
  - lastWillTopic
  - lastWillQos
  - lastWillMessage
  - keepAlive

2. CONNACK
  - sessionPresent
  - returnCode

3. SUBSCRIBE
  - qos
  - topico

4. SUBACK
  - returnCode

5. UNSUBSCRIBE
  - topico

6. PUBLISH
  - topicName
  - qos
  - retainFlag
  - carga útil
