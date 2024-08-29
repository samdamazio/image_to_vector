import os
import cv2
import numpy as np
import svgwrite

def image_to_vector(image_path, output_svg_path):
    # Carregar a imagem
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return

    # Detecção de bordas usando Canny
    edges = cv2.Canny(image, threshold1=50, threshold2=150)

    # Encontrar contornos na imagem
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Criar um arquivo SVG para desenhar os contornos
    height, width = edges.shape
    dwg = svgwrite.Drawing(output_svg_path, size=(width, height))
    
    # Adicionar cada contorno ao SVG
    for contour in contours:
        points = [(float(point[0][0]), float(point[0][1])) for point in contour]  # Converte os pontos para float
        dwg.add(dwg.polygon(points, fill='none', stroke='black', stroke_width=1))

    # Salvar o arquivo SVG
    dwg.save()
    print(f"Imagem vetorizada salva como {output_svg_path}")

def process_images(input_dir, output_dir):
    # Certificar-se de que o diretório de saída existe
    os.makedirs(output_dir, exist_ok=True)

    # Iterar sobre todos os arquivos no diretório de entrada
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.svg")
            image_to_vector(input_path, output_path)

# Especificar os diretórios de entrada e saída
input_directory = 'data'
output_directory = 'vetorizadas'

# Processar todas as imagens do diretório de entrada
process_images(input_directory, output_directory)