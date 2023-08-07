# Modelo Detecção de Fraudes Bancárias

Codificação em Python com uso TensorFlow para uma aplicação de Detecção de Fraudes Bancárias que utiliza um modelo de Machine Learning para prever se uma transação é fraudulenta ou não. O modelo é treinado com dados de transações bancárias e, em seguida, é usado para prever a probabilidade de uma nova transação ser fraudulenta. Os resultados são então enviados para um tópico Kafka.

## Requisitos

- Python 3.8+
- Microsoft SQL
- Kafka
- TensorFlow
- Scikit-learn
- Pandas
- Psycopg2
- Python-dotenv
- Kafka-python

## Configuração

1. Clone o repositório
2. Instale as dependências com `pip install -r requirements.txt`
3. Configure as variáveis de ambiente no arquivo `.env`. As variáveis necessárias são:
    - `DB_HOST`: O host do seu banco de dados PostgreSQL
    - `DB_DATABASE`: O nome do seu banco de dados PostgreSQL
    - `DB_USER`: O usuário do seu banco de dados PostgreSQL
    - `DB_PASSWORD`: A senha do seu banco de dados PostgreSQL
    - `KAFKA_SERVERS`: A lista de servidores Kafka para se conectar

## Uso

Para executar o script principal, use o seguinte comando:

python main.py

Este código irá:

1. Conectar-se ao banco de dados Microsoft SQL e buscar os dados de transações
2. Treinar o modelo de detecção de fraudes com os dados
3. Avaliar o desempenho do modelo
4. Enviar as previsões do modelo para um tópico Kafka
5. Estrutura do Projeto
6. projeto contém as seguintes classes:

- FraudDetectionModel: Esta classe define o modelo de aprendizado de máquina para detecção de fraudes. Ele usa uma rede neural densa com duas camadas ocultas.
- DatabaseConnector: Esta classe é responsável por conectar-se ao banco de dados Microsoft SQL e buscar os dados de transações.
- KafkaProducerWrapper: Esta classe é responsável por enviar as previsões do modelo para um tópico Kafka.


## Rodar via Docker

Se você tem o Dockerfile para essa imagem, você pode recriá-la usando o comando docker build. Aqui está um exemplo de como você pode fazer isso:
rode o comando: 
### docker build -t seu_usuario/fraud-detection .

Depois de criar a imagem, você precisa enviá-la para o registro Docker. Aqui está um exemplo de como você pode fazer isso:
### docker push seu_usuario/fraud-detection

Depois rodar o comando:
### docker-compose up

Depois de seguir os passos estará pronto para rodar a aplicação em cointeiner.

## Autor
Emerson Amorim
