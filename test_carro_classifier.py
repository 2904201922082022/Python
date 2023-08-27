import pytest
from carro_classifier import classify_car_model

# Define uma lista de imagens de carros e seus modelos esperados
images = [
    ('car1.jpg', 'Audi A5'),
    ('car2.jpg', 'BMW X5'),
    ('car3.jpg', 'Chevrolet Camaro'),
    ('car4.jpg', 'Ford Mustang'),
    ('car5.jpg', 'Honda Civic')
]

# Define um marcador parametrize para executar o teste com cada par de imagem e modelo da lista
@pytest.mark.parametrize('img_path, expected_model', images)
def test_classify_car_model(img_path, expected_model):
    # Chama a função com o caminho da imagem
    actual_model = classify_car_model(img_path)
    # Verifica se o modelo obtido é igual ao esperado
    assert actual_model == expected_model


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
