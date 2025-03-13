import cv2
import numpy as np
import os

def remove_background(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)
            if image is None:
                continue
            
            # Converter para escala de cinza e aplicar desfoque
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            
            # Aplicar detecção de bordas para segmentação melhorada
            edges = cv2.Canny(blurred, 50, 150)
            
            # Expandir bordas para melhor contorno
            kernel = np.ones((3,3), np.uint8)
            edges = cv2.dilate(edges, kernel, iterations=2)
            
            # Encontrar contornos
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            mask = np.zeros_like(gray)
            
            if contours:
                largest_contour = max(contours, key=cv2.contourArea)
                cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)
                
                # Refinar máscara para eliminar buracos e ruídos
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=3)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
                
                # Aplicar suavização na máscara para melhor transição
                mask = cv2.GaussianBlur(mask, (5,5), 0)
                
            # Aplicar a máscara à imagem original
            result = cv2.bitwise_and(image, image, mask=mask)
            
            # Salvar a imagem processada
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, result)
            print(f"Imagem processada: {output_path}")

# Exemplo de uso
input_folder = r'D:\Downloads\provete_ver'  # Substituir pelo caminho real da pasta de entrada
output_folder = r'D:\Downloads\provete_ver\remove_up2'  # Substituir pelo caminho real da pasta de saída
remove_background(input_folder, output_folder)
