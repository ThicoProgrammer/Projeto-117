import os
import cv2

path = 'images/'

images = []

for arquivo in os.listdir(path):
    name,ext = os.path.splitext(arquivo)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path + '/' + arquivo

        print(file_name)

        images.append(file_name)


count = len(images)

frame = cv2.imread(images[0])

largura, altura, bandas = frame.shape

tamanho = (largura, altura)

print(tamanho)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, tamanho)

for i in range(0, count - 1):
    frame = cv2.imread(images[i])

    out.write(frame)

out.release()

print('Concluído')
