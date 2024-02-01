import cv2
import os
import re

sceneName='dragon_nero_normal'

img_folder_path = f"/Users/menglidaren/iclr2024/assets/{sceneName}"

img_names = sorted([f for f in os.listdir(img_folder_path) if not f.startswith('.')],key= lambda x: int(re.findall(r'\d+',x)[-1]))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

img = cv2.imread(os.path.join(img_folder_path, img_names[0]), -1)
height, width, channels = img.shape

video = cv2.VideoWriter(f'{sceneName}.mp4', fourcc, 25.0, (width, height))


for img_name in img_names:
    img_path = os.path.join(img_folder_path, img_name)
    img = cv2.imread(img_path,-1)
    img[img[:, :, 3] == 0] = [255, 255, 255, 0]
    video.write(img[:, :, :3])


video.release()