import tensorflow as tf

def main():
    print("1. Carregando o modelo treinado...")
    # Carrega o modelo que foi salvo na etapa anterior
    model = tf.keras.models.load_model('model.h5')

    print("2. Configurando o conversor para TensorFlow Lite...")
    # Inicializa o conversor do TensorFlow Lite usando o modelo Keras
    converter = tf.lite.TFLiteConverter.from_keras_model(model)

    print("3. Aplicando a técnica de otimização (Dynamic Range Quantization)...")
    # Define a otimização padrão, que aplica a quantização de faixa dinâmica
    # Isso reduz o tamanho do modelo sem perder muita precisão
    converter.optimizations = [tf.lite.Optimize.DEFAULT]

    print("4. Convertendo o modelo...")
    # Realiza a conversão de fato
    tflite_quant_model = converter.convert()

    print("5. Salvando o modelo otimizado...")
    # Salva o resultado no arquivo 'model.tflite' no modo de escrita binária ('wb')
    with open('model.tflite', 'wb') as f:
        f.write(tflite_quant_model)
        
    print("Sucesso! Modelo convertido e otimizado salvo como 'model.tflite'.")

if __name__ == "__main__":
    main()