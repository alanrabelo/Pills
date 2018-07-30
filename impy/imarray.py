from .__imports__ import *

class imarray(object):

    def __init__(self,path=None,mode='L'):
        if path == None:
            return
        try :
            self.image = imread(path, mode=mode)
        except :
            print("Error! Could not read the image from the path specified: %s"%path)
            return
        try :
            self.image = np.asarray(self.image)
            self.dimension = self.image.shape
            self.type = path.split(".")[-1]
        except :
            print("Internal Error! Image file not supported")

    def __repr__(self):
        #Method to return the image value when an object of the class is created
        #	img = imarray(path)
        #	img store the image. Not the
        return repr(self.image)

    def __cmp__(self,img):
        return cmp(self,img)

    def __getitem__(self,coordinates):
        return self.image[coordinates]

    def load(self, image) :
        image = np.asarray(image,dtype=np.uint8)
        if len(image.shape) == 2 :
            self.image = image
            try :
                self.dimension = self.image.shape
            except :
                print("Internal Error! Image file not supported")
        else :
            print("Assignment Error. Given input is not an image")

    def getShape(self):
        return self.dimension
    shape = property(getShape)

    def getExtension(self):
        return self.type
    ext = property(getExtension)

    def displayImage(self,mode='Greys_r'):
        try:
            plt.imshow(self.image,cmap=mode)
        except:
            print("Image could not be displayed")
            return
        plt.show()
    disp = property(displayImage)

    def save(self,name):
        plt.imsave(name,self.image)

    def convolve(self,mask):
        mask = np.asarray(mask,dtype=np.float32)
        if len(mask.shape) != len(self.dimension):
            print("Invalid Mask Dimensions")
        (m,n) = mask.shape
        padY = int(np.floor(m/2))
        padX = int(np.floor(n/2))
        (M,N) = self.dimension
        padImg = np.ones((M+padY*2,N+padX*2))*128
        fImage = np.zeros((M+padY*2,N+padX*2))
        padImg[padY:-padY,padX:-padX] = self.image

        for yInd in range(padY,M+padY):
            for xInd in range(padX,N+padX):
                fImage[yInd,xInd] = sum(sum(padImg[yInd-padY:yInd+m-padY,xInd-padX:xInd+n-padX]*mask))

        return fImage[padY:-padY,padX:-padX]
