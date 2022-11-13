#Responsável por realizar a produção de mensagens para testes do RabbitMQ

#imports
import pika

#responsável por definir a autenticação e servidor do ambiente cloud do RabbitMQ (amqp)
parameters = pika.URLParameters('amqps://qsvvrqtm:XCvydaLcdvhxgwOUKjXAfviC3G30nK8f@woodpecker.rmq.cloudamqp.com/qsvvrqtm')
connection = pika.BlockingConnection(parameters)

#Inicia conexão
channel = connection.channel()

#define queue
channel.queue_declare(queue='marcacao-ponto', durable=True)

i = 1

#percorre lista para publicação de mensagens
for i in range(5000):
    x = "Mensagem número " + str(i)

    #gera mensagens no Rabbit
    channel.basic_publish(exchange='',
                        routing_key='marcacao-ponto',
                        body=x)
    print(" [x] Enviado " + x)

#Fecha conexão
connection.close()