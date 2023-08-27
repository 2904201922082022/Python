# Importa as bibliotecas necessárias
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import keras
from keras.models import load_model
from keras.preprocessing import image

# Define a função que recebe uma imagem e retorna o modelo do carro
def classify_car_model(img_path):
    # Carrega o modelo pré-treinado da CNN
    model = load_model('car_model_classifier.h5')
    # Carrega a imagem e redimensiona para 224x224 pixels
    img = image.load_img(img_path, target_size=(224, 224))
    # Converte a imagem em um array numpy
    img = image.img_to_array(img)
    # Expande as dimensões do array para incluir o tamanho do lote
    img = img.reshape(1, 224, 224, 3)
    # Normaliza os valores dos pixels entre 0 e 1
    img = img / 255.0
    # Faz a predição usando o modelo da CNN
    pred = model.predict(img)
    # Obtém o índice da classe com maior probabilidade
    pred_class = pred.argmax(axis=-1)[0]
    # Retorna o nome da classe correspondente ao índice
    return class_names[pred_class]
# Lê os dados dos veículos a partir de um arquivo CSV
df = pd.read_csv('car_data.csv')

# Explora os dados dos veículos
print(df.head()) # Mostra as primeiras cinco linhas dos dados
print(df.info()) # Mostra informações sobre as colunas, tipos e valores nulos dos dados
print(df.describe()) # Mostra estatísticas descritivas dos dados numéricos
print(df['type'].value_counts()) # Mostra a frequência de cada tipo de veículo nos dados
print(df['model'].unique()) # Mostra os modelos únicos de veículos nos dados

# Limpa os dados dos veículos
df = df.dropna() # Remove as linhas com valores nulos
df = df.replace('?', np.nan) # Substitui os valores desconhecidos por nulos
df = df.fillna(df.mean()) # Substitui os valores nulos pela média da coluna

# Codifica os dados dos veículos
le = LabelEncoder() # Cria um objeto para codificar os valores categóricos em numéricos
df['type'] = le.fit_transform(df['type']) # Codifica a coluna type usando o LabelEncoder
df['model'] = le.fit_transform(df['model']) # Codifica a coluna model usando o LabelEncoder
ohe = OneHotEncoder(sparse=False) # Cria um objeto para codificar os valores numéricos em binários
df = pd.get_dummies(df, columns=['type', 'model']) # Codifica as colunas type e model usando o OneHotEncoder

# Divide os dados dos veículos em conjuntos de treinamento e teste
X = df.drop('price', axis=1) # Define as variáveis independentes como todas as colunas exceto a price
y = df['price'] # Define a variável dependente como a coluna price
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Divide os dados em 80% para treinamento e 20% para teste

# Escolhe um algoritmo de aprendizado de máquina para classificar os modelos de veículos
dtc = DecisionTreeClassifier() # Cria um objeto para o algoritmo de árvore de decisão

# Treina o modelo de classificação usando o conjunto de treinamento
dtc.fit(X_train, y_train) # Ajusta o modelo aos dados de treinamento
y_pred = dtc.predict(X_test) # Faz a predição para os dados de teste

# Avalia o modelo de classificação usando o conjunto de teste
acc = accuracy_score(y_test, y_pred) # Calcula a acurácia do modelo
pre = precision_score(y_test, y_pred, average='macro') # Calcula a precisão do modelo
rec = recall_score(y_test, y_pred, average='macro') # Calcula a revocação do modelo
cm = confusion_matrix(y_test, y_pred) # Gera a matriz de confusão do modelo

# Mostra os resultados da avaliação do modelo
print(f'Acurácia: {acc:.2f}')
print(f'Precisão: {pre:.2f}')
print(f'Revocação: {rec:.2f}')
print(f'Matriz de confusão: \n{cm}')
