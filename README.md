# testes-rabbitmq
 
## Objetivo
Backend responsável por publicar mensagens em massa no RabbitMQ.

## Sobre a Solução 
Atualmente a publicação está somente centralizada via interface na plataforma https://api-marcacao-ponto.herokuapp.com/, visto que não possuímos produtores dessas mensagens. Dessa forma, foi criado esse pacote de testes para atender a necessidade de publicação em massa de mensagens, para testes de carga.

## Testes
O testes de publicação podem ser realizados de forma local.

O limite de mensagens é de 10 mil, a menos que um consumer busque e baixe essas mensagens. Dessa forma, não é possível testar mais que isso. A limitação é do plano gratuito do RabbitMQ.

Para que seja possível, é necessarío:
- Possuir o Python (v3.11) instalado;
- Adicionar o Python ao Path;

Deverá ser aberto o Prompt de Comando (cmd).

Após abrir o Prompt, deverá ser acessado o diretório onde foi baixado o repositório. 

Deverá ser executado o comando "pip install -r requirements.txt".

Alguns caminhos poderão ser tomados agora:

* Testes de importação via arquivo
    - Um dos cenários levantados é que para alguns REP, a importação das marcações se dá via arquivo. Dessa forma, a fim de simular o layout AFD de importação de marcações, foram criados os arquivos "arquivo_marcacoes.txt" e "arquivo_teste.txt".

    - Caso desejar testar a funcionalidade de importação via arquivo, será necessário executar o comando no cmd: "python producer_archive.py"
    - Caso desejar testar a funcionalidade de importação em massa, desconsiderando os arquivos, será necessário executar o comando no cmd: "python producer.py"

Será exibida uma mensagem " [x] Enviado + {conteúdo}". Quando publicadas as mensagens, o consumer (caso esteja ativo, o local e o dedicado irão concorrer) irá automaticamente baixar da fila.

Para gerar uma mensagem, também poderá ser acessada a aplicação web desenvolvida: https://api-marcacao-ponto.herokuapp.com/ e realizado um registro de ponto fictício.
