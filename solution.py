"""
Rozwiązania do laboratorium 1 z Obrazowania Biomedycznego.
"""
import numpy as np

"""
3 - Kwadrat
"""
def square(size, side, start): 
    image=np.zeros((size, size)).astype(np.uint8)
    x, y=start
    image[y:(side+y), x:(side+x)]=255
    return image

"""
3 - Koło
"""
def midcircle(size):
    x,y=size
    image=np.zeros((y, x)).astype(np.uint8)
    r=int(min(size)/4)
    ax=int(x/2)
    ay=int(y/2)

    for (iy,ix) in np.ndindex(image.shape):
        if (ix-ax)**2+(iy-ay)**2<=r**2:
            image[iy,ix]=255

    return image


"""
3 - Szachownica.
"""
def checkerboard(size):
    image = np.zeros((size, size)).astype(np.uint8)
    cellsize = size//8

    for ix in range(8):
        for iy in range(8):
            if iy%2!=ix%2: 
                image[ix*cellsize:(ix*cellsize+cellsize), iy*cellsize:(iy*cellsize+cellsize)] = 255
    return image

"""
4 - Interpolacja najbliższych sąsiadów.
"""
def nn_interpolation(source, new_size):
    src=source.shape
    dst=new_size

    a_src, b_src=src
    b_dst, a_dst=dst

    ratio_x=b_src/a_dst
    ratio_y=a_src/b_dst

    image = np.zeros(new_size).astype(np.uint8)

    for (iy,ix) in np.ndindex(image.shape):
        image[iy,ix] = source[int(iy*ratio_y), int(ix*ratio_x)]

    return image

"""
5 - Interpolacja dwuliniowa
"""
def bilinear_interpolation(source, new_size):
    a_src, b_src=source.shape
    b_dst, a_dst=new_size

    ratio_x =b_src/b_dst
    ratio_y =a_src/a_dst

    image = np.zeros(new_size).astype(np.uint8)

    for (iy,ix) in np.ndindex(image.shape):
        y=iy*ratio_y 
        x=ix*ratio_x 

        y_floor=int(np.floor(y))
        y_ceil=int(np.ceil(y))

        x_floor=int(np.floor(x))
        x_ceil=int(np.ceil(x))

        values=[
            source[y_floor, x_floor],
            source[y_ceil, x_floor],
            source[y_floor, x_ceil],
            source[y_ceil, x_ceil],
        ]

        x_fraction=x-np.floor(x)
        y_fraction=y-np.floor(y)

        a=x_fraction
        b=y_fraction

        fa0=(1-a)*values[0]+a*values[2]
        fa1=(1-a)*values[1]+a*values[3]

        fab=(1-b)*fa0+b*fa1
        image[iy, ix]=int(fab)

    return image
