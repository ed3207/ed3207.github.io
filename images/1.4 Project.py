import matplotlib.pyplot as plt
import os.path
import numpy as np
import PIL
import PIL.ImageDraw

directory=os.path.dirname(os.path.abspath(__file__))
filepath_spongegar=os.path.join(directory, 'spongegar.jpg')
spongegar_numpy=plt.imread(filepath_spongegar)



directory=os.path.dirname(os.path.abspath(__file__))
filepath_rice=os.path.join(directory, 'rice.jpg')
rice_numpy=plt.imread(filepath_rice)

directory=os.path.dirname(os.path.abspath(__file__))
filepath_snake=os.path.join(directory, 'snake.jpg')
snake_numpy=plt.imread(filepath_snake)

directory=os.path.dirname(os.path.abspath(__file__))
filepath_ricehat=os.path.join(directory, 'ricehat.jpg')
ricehat_numpy=plt.imread(filepath_ricehat)

spongegar_pil = PIL.Image.fromarray(spongegar_numpy)
rice_pil = PIL.Image.fromarray(rice_numpy)
snake_pil= PIL.Image.fromarray(snake_numpy)
ricehat_pil=PIL. Image.fromarray(ricehat_numpy)

ricehat=ricehat_pil.convert("RGBA")
ricehat_n=np.array(ricehat)
height = len(ricehat_n)
width = len(ricehat_n[0])
for r in range(height):
    for c in range(width):
        if sum(ricehat_n[r][c])>764:
            ricehat_n[r][c]=[0,128,0,255]
ricehat_p=PIL.Image.fromarray(ricehat_n)

spongegar_crop=spongegar_pil.crop((27,80,769,524))
spongegar_final=spongegar_crop.resize((284,190))
spongegar_n=np.array(spongegar_final)

for r in range(0,190):
   for c in range(0,284):
        if sum(spongegar_n[r][c])>666:
         spongegar_n[r][c]=[255,0,0,255]
spongegar_p=PIL.Image.fromarray(spongegar_n)

rice_pil.paste(snake_pil,(220,400))
rice_pil.paste(spongegar_p,(515,380))
rice_pil.paste(ricehat_p,(555,320))
rice_final=np.array(rice_pil)

fig, ax=plt.subplots(1,1)
ax.imshow(rice_final, interpolation='none')
fig.show()