# 📝 Relatório do Candidato - Desafio Edge AI

👤 Identificação: **Pedro Henrique Fernandes Bezerra**


### 1. Resumo da Arquitetura do Modelo
A arquitetura implementada no arquivo `train_model.py` é uma Rede Neural Convolucional (CNN) simples e enxuta, projetada especificamente para ser eficiente em dispositivos de Edge AI. O modelo é composto pelas seguintes camadas:
* **Entrada:** Imagens de 28x28 pixels com 1 canal de cor (tons de cinza).
* **Camadas de Extração de Características:** * 1ª Camada Convolucional (`Conv2D`) com 16 filtros, seguida por uma camada de redução de dimensionalidade (`MaxPooling2D`).
  * 2ª Camada Convolucional (`Conv2D`) com 32 filtros, também seguida por um `MaxPooling2D`.
* **Camadas de Classificação:** Uma camada de achatamento (`Flatten`) que transforma os dados em um vetor 1D, conectada a uma camada densa (`Dense`) oculta de 64 neurônios (ativação ReLU) e, por fim, a camada de saída com 10 neurônios (ativação Softmax) para classificar os dígitos de 0 a 9.



## 2️. Bibliotecas Utilizadas

As principais ferramentas utilizadas no desenvolvimento foram:
* **TensorFlow / Keras:** Biblioteca principal utilizada para construir, treinar, avaliar e salvar a rede neural (CNN), além de fornecer o dataset MNIST.
* **NumPy:** Utilizada para a manipulação matemática dos arrays de imagem (especificamente para adicionar o canal de cor necessário para as camadas convolucionais usando `np.expand_dims`).


## 3️. Técnica de Otimização do Modelo

No arquivo `optimize_model.py`, foi utilizada a técnica de **Dynamic Range Quantization** (Quantização de Faixa Dinâmica) através da ferramenta `TFLiteConverter`. 
Essa técnica otimiza o modelo convertendo os "pesos" da rede neural (que originalmente ocupam muito espaço na memória como números de ponto flutuante/float32) para formatos menores, como números inteiros de 8 bits (int8). Isso reduz drasticamente o tamanho do arquivo final (`model.tflite`) e acelera o tempo de processamento (inferência), tornando-o ideal para rodar em sistemas embarcados com poucos recursos, mantendo um nível de precisão muito alto.


## 4️. Resultados Obtidos

O modelo obteve um excelente desempenho mesmo com restrições de processamento. Após um treinamento muito rápido em CPU, limitado a apenas 5 épocas, o modelo alcançou uma **acurácia final no teste de 98,97%** (0.9897) e uma perda (loss) de apenas 0.0321.



## 5️. Comentários Adicionais (Opcional)

* **Decisões Técnicas:** Optei por não utilizar uma arquitetura profunda. Manter apenas 16 e 32 filtros nas camadas convolucionais foi uma decisão consciente para garantir que o treinamento fosse extremamente rápido (compatível com os limites do pipeline de CI do GitHub Actions) e que o modelo final fosse leve.
* **Aprendizados:** O desafio consolidou o entendimento de que, para aplicações de Edge AI, a engenharia de software não deve buscar apenas a precisão máxima ("overkill"), mas sim o equilíbrio perfeito entre o tamanho do modelo, a velocidade de execução e uma acurácia que resolva o problema real.
