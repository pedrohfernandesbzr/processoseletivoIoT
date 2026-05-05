import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

def main():
    print("1. Carregando e preparando o dataset MNIST...")
    # Carregamento do dataset MNIST utilizando o keras diretamente
    mnist = keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Normalização dos dados (transformando os valores dos pixels de 0-255 para 0.0-1.0)
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Redimensionando para adicionar o canal de cor (necessário para camadas Conv2D)
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)

    print("2. Construindo a Rede Neural Convolucional (CNN)...")
    # Construção de um modelo CNN simples usando keras.Sequential
    model = keras.Sequential([
        # Primeira camada convolucional e de pooling
        layers.Conv2D(16, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        
        # Segunda camada convolucional e de pooling
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Achatamento (Flatten) para conectar com as camadas densas finais
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        
        # Camada de saída com 10 neurônios (um para cada dígito de 0 a 9)
        layers.Dense(10, activation='softmax')
    ])

    # Compilação do modelo
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    print("3. Iniciando o treinamento do modelo...")
    # Treinamento limitado a 5 épocas para execução rápida em CPU
    model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

    print("\n4. Avaliando o modelo...")
    # Exibição da acurácia final no terminal
    test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)
    print(f"\n---> ACURÁCIA FINAL NO TESTE: {test_acc:.4f} <---")

    print("\n5. Salvando o modelo...")
    # Salvamento do modelo treinado no formato Keras (.h5)
    model.save('model.h5')
    print("Modelo salvo com sucesso como 'model.h5'!")

if __name__ == "__main__":
    main()