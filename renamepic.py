import os
def rename(path):

    images = os.listdir(path)
    for i, image in enumerate(images):

        src = os.path.join(os.path.abspath(path), image)
        dst = os.path.join(os.path.abspath(path),f'{i+300}.jpg')
        os.rename(src,dst)
rename(r'D:\picar')