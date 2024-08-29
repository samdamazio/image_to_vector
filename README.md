# Image Vectorizer

Este projeto é um script Python que converte imagens raster (como JPEG, PNG) em imagens vetorizadas no formato SVG. Utiliza bibliotecas como OpenCV para processamento de imagem e svgwrite para gerar a imagem vetorizada.

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Funcionamento](#funcionamento)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Pré-requisitos

Certifique-se de ter o Python 3.6 ou superior instalado. Além disso, você precisará instalar algumas bibliotecas Python:

- `opencv-python-headless`
- `numpy`
- `svgwrite`
- `scikit-image`

## Instalação

1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/seuusuario/image-vectorizer.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd image_to_vector
    ```

3. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

4. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

1. Coloque a imagem que deseja vetorizar no diretório do projeto.

2. Execute o script Python passando o caminho da imagem de entrada e o nome do arquivo de saída SVG: (obs, ou use o diretorio data na versão v2 para fazer em varias imagens de uma vez)

    ```bash
    python vectorizer.py caminho/para/sua/imagem.jpg imagem_vetorizada.svg
    ```

3. O arquivo SVG gerado será salvo no mesmo diretório especificado dentro da pasta vetorizadas.

## Funcionamento

- O script carrega uma imagem e usa o algoritmo Canny para detectar bordas.
- Em seguida, encontra os contornos na imagem e os desenha em um arquivo SVG.
- O resultado é uma representação vetorial da imagem original.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar pull requests. Se você deseja adicionar novos recursos ou melhorar o desempenho, por favor, faça um fork do repositório e crie uma nova branch para seu trabalho.

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/MinhaFuncionalidade`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça push para a branch (`git push origin feature/MinhaFuncionalidade`)
5. Abra um pull request

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
