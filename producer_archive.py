#Responsável por realizar a produção de mensagens para o RabbitMQ através da leitura de um arquivo
#O arquivo de marcações de exemplo foi elaborado apenasr para os testes
#Foram utilizadas apenas 10 mil linhas pois é o limite máximo de mensagens na queue, do plano free do RabbitMQ

import json
import pika

#responsável por definir a autenticação e servidor do ambiente cloud do RabbitMQ (amqp)
parameters = pika.URLParameters('amqps://qsvvrqtm:XCvydaLcdvhxgwOUKjXAfviC3G30nK8f@woodpecker.rmq.cloudamqp.com/qsvvrqtm')
connection = pika.BlockingConnection(parameters)

#Inicia conexão
channel = connection.channel()

#Define queue 
channel.queue_declare(queue='marcacao-ponto', durable=True)

#Arquivo utilizado para os testes
arquivo = open('arquivo_marcacoes.txt')

#Arquivo utilizado para testes menores
#arquivo = open('arquivo_teste.txt')

#Percorre arquivo
for linha in arquivo:
    
    #Obtém informações conforme layout
    data = linha[12:22]
    hora = linha[22:29]
    employeeId = linha[0:6]
    employerId = linha[6:12]

    #Monta mensagem que será enviada
    body = {
        "includedAt": data + " " + hora,
        "employeeId": employeeId, 
        "employerId": employerId
    }

    #Converte mensagem para Json
    bodyJson = json.dumps(body)                   

    #Publica mensagem e retorna resultado
    channel.basic_publish(exchange='',
                        routing_key='marcacao-ponto',
                        body=bodyJson)

    print(" [x] Enviado " + bodyJson)

#Fecha arquivo e conexão com cloud AMQP
arquivo.close()
connection.close()