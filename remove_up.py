import cv2
import numpy as np
import os

def remove_background(input_folder, output_folder):
    # Garantir que a pasta de saída existe
    os.makedirs(output_folder, exist_ok=True)
    
    # Listar todas as imagens na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)
            if image is None:
                continue
            
            # Converter para escala de cinza e aplicar desfoque
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)
            
            # Aplicar limiar adaptativo para destacar o corpo de prova
            _, binary = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)
            
            # Encontrar contornos
            contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Criar uma máscara vazia
            mask = np.zeros_like(image_gray)
            
            # Selecionar o maior contorno (provavelmente o corpo de prova)
            if contours:
                largest_contour = max(contours, key=cv2.contourArea)
                cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)
                
            # Aplicar a máscara à imagem original
            result = cv2.bitwise_and(image, image, mask=mask)
            
            # Salvar a imagem processada
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, result)
            print(f"Imagem processada: {output_path}")

# Exemplo de uso
input_folder = r'D:\Downloads\provete_ver'  # Substituir pelo caminho real da pasta de entrada
output_folder = r'D:\Downloads\provete_ver\remove_up'  # Substituir pelo caminho real da pasta de saída
remove_background(input_folder, output_folder)
