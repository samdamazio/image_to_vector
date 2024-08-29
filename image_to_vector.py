import os
import cv2
import numpy as np
import svgwrite
from skimage import measure, color
from skimage.filters import gaussian

def image_to_vector_with_high_quality(image_path, output_svg_path):
    # Carregar a imagem
    image = cv2.imread(image_path)
    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return

    # Aplicar suavização bilateral para reduzir ruído enquanto mantém as bordas
    image_smoothed = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

    # Converter a imagem suavizada para o espaço de cores RGB
    image_rgb = cv2.cvtColor(image_smoothed, cv2.COLOR_BGR2RGB)

    # Aplicar segmentação de cores usando K-means ou Gaussian Mixture Models (GMM)
    # Aqui usamos apenas uma suavização básica e segmentação para manter a simplicidade

    # Converter a imagem para escala de cinza e suavizar ainda mais
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
    image_gray = gaussian(image_gray, sigma=1)

    # Usar Otsu's threshold para segmentação
    _, binary_mask = cv2.threshold((image_gray * 255).astype(np.uint8), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Encontrar contornos na máscara binária
    contours = measure.find_contours(binary_mask, 0.8)

    # Criar um arquivo SVG para desenhar os contornos com cores
    height, width, _ = image.shape
    dwg = svgwrite.Drawing(output_svg_path, size=(width, height))

    # Adicionar cada contorno ao SVG com a cor média da região
    for contour in contours:
        points = [(float(point[1]), float(point[0])) for point in contour]
        if len(points) < 3:  # Ignorar contornos que não são polígonos válidos
            continue

        # Calcular a cor média da região delimitada pelo contorno
        mask = np.zeros_like(image_gray, dtype=np.uint8)
        cv2.fillPoly(mask, [np.array(points, dtype=np.int32)], 255)
        mean_color = cv2.mean(image_rgb, mask=mask[:image_rgb.shape[0], :image_rgb.shape[1]])[:3]
        rgb_color = f"rgb({int(mean_color[0])}, {int(mean_color[1])}, {int(mean_color[2])})"
        
        dwg.add(dwg.polygon(points, fill=rgb_color, stroke='none'))

    # Salvar o arquivo SVG
    dwg.save()
    print(f"Imagem vetorizada com alta qualidade salva como {output_svg_path}")

def process_images(input_dir, output_dir):
    # Certificar-se de que o diretório de saída existe
    os.makedirs(output_dir, exist_ok=True)

    # Iterar sobre todos os arquivos no diretório de entrada
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.svg")
            image_to_vector_with_high_quality(input_path, output_path)

# Especificar os diretórios de entrada e saída
input_directory = 'data'
output_directory = 'vetorizadas'

# Processar todas as imagens do diretório de entrada
process_images(input_directory, output_directory)