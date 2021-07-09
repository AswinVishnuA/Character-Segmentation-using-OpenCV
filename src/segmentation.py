import cv2 as cv
import numpy as np
import os,shutil


# To delete files when new image is processed
def clearPath(path):
    for files in os.listdir(path):
        filepath = os.path.join(path, files)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)
    return



#Write new image file with given contours and image.new file saved to saveToPath
def segment(result,cntrs,saveToPath,name):
    tempImage=result.copy()  
    for i,c in enumerate(cntrs):
        box = cv.boundingRect(c)
        x,y,w,h = box
        temp=tempImage[y:y+h,x:x+w] 
        cv.imwrite(os.path.join(saveToPath,name+f"{i}.png"),temp)
        cv.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 2)
    return result


# Contours are created for images with given kernal size
def makeContours(temp,kernalSize):
    gray=cv.cvtColor(temp,cv.COLOR_BGR2GRAY)
    thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
    kernel = cv.getStructuringElement(cv.MORPH_RECT, kernalSize)
    morph = cv.morphologyEx(thresh, cv.MORPH_DILATE, kernel)
    cntrs = cv.findContours(morph, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]
    return cntrs



def main(path):
    img=cv.imread(path["images"])
    cropped=img[20:img.shape[0]-20,30:img.shape[1]-20]
    contours=makeContours(cropped,(150,3))
    clearPath(path["lines"])
    result=segment(cropped,contours,path["lines"],"line")
    clearPath(path["words"])
    count=0
    for file in os.listdir(path["lines"]):
        filePath=os.path.join(path["lines"],file)
        line=cv.imread(filePath)
        name=f"line{count}word"
        count+=1
        contours=makeContours(line,(3,150))
        resultLine=segment(line,contours,path["words"],name)
    clearPath(path["letter"])
    for file in os.listdir(path["words"]):
        filePath=os.path.join(path["words"],file)
        word=cv.imread(filePath)
        name=file.split('.')[0]+"letter"
        contours=makeContours(word,(1,2))
        resultWord=segment(word,contours,path["letter"],name)
    cv.imshow("Line segmentation",result)#uncomment this for viewing the line segmentation
    cv.waitKey(0)                        #uncomment this for viewing the line segmentation
    
    pass



if __name__=="__main__":
    paths={
    "images":r"Input/in1.png",
    "lines":r"Output/Lines/",
    "words":r"Output/Words/",
    "letter":r"Output/Letters/"
    }
    filename=input("Please enter name of the image file(png/jpg) which is present in the Input folder:\n")
    paths["images"]=os.path.join("Input",filename.strip())
    if os.path.exists(paths["images"]):
        main(paths)
        print("Process completed without error")
    else:
        print("File name does not exist in Input folder")