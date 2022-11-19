import cv2

def resize(img,scale_percent):
    #calculate the percent of original dimensions
    width = int(img.shape[1] * scale_percent / 100) #img.shape[1] means width
    height = int(img.shape[0] * scale_percent / 100)#img.shape[0] means Height

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(img, dsize)

    return output