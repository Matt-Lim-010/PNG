from PIL import Image
import re

# Open the PNG file
img = Image.open('render3.png')
file = open("result.csv", "w")

array = []
counter = 0
pixelData = img.getdata()

columList = []
lineLimit = 969
lineList = []
linectn = 0
for pixel in pixelData:
    # temp = round(pixel/255)
    temp = pixel
    print(temp)
    rgb = re.findall("[\d]{1,3},\W[\d]{1,3},\W[\d]{1,3},\W",str(temp))
    tempRBG = rgb[0].split(",")
    r = tempRBG[0]
    g = tempRBG[1]
    b = tempRBG[2]
    # print(r)
    # print(g)
    # print(b)
    grayScale = (int(r)+int(g)+int(b))/3
    if linectn < lineLimit:
        lineList.append(grayScale)
        linectn += 1
    else:
        linectn = 0
        columList.append(lineList)
        lineList.clear()
        # lineList.reverse()
    counter += 1
columList.reverse()

for i in columList:
    for x in i:
        file.write(str(x))
        file.write("\n")

    # print(str(grayScale))

    # rgb = str(pixel).split(",")
    # rgb = rgb[0].split("(")
    # print(rgb[0])



# minV = min(array)
# for a in array:
#     tempResult = round((a/minV)*10)
#     file.write(str(tempResult))
#     file.write("\n")
#     print(tempResult)
# Display information about the image
print("Image format:", img.format)
print("Image mode:", img.mode)
print("Image size:", img.size)
# print(counter)
# print(min(array))
# print(max(array))
# print(max(array)/min(array))




file.close()
# # Display the image
# img.show()
#
# # Close the image file
# img.close()
