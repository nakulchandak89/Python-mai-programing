#This code is about face detaction and as an ouptput it create the box near faces 
import cv2

img = cv2.imread("project\Resources\ml2.jpg")
cv2.imshow("face", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade = cv2.CascadeClassifier("project\haar_face.xml")

face_react = haar_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=2)

print(f"number of faces found = {len(face_react)}")

for (x, y, w, h) in face_react:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv2.imshow("detacted Face's", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


'''
this is the logic bhind the arguments passed in for loop 
x --> X cordanets 
y --> Y cordenets 
w --> Width
h --> Hight
(x, y) -------------> (x + w, y)
    |                     |
    |                     |
    |                     |
(x, y + h) -------> (x + w, y + h)
'''
