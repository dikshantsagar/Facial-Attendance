import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.svm import LinearSVC as svm
import pickle

li=[]
for infile in glob.glob('*/*'):
    a=cv2.imread(infile)
    gray=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
    li.append(cv2.resize(gray,(350,350)).flatten())
li=np.asarray(li)

x=li[0]
plt.imshow(x.reshape(350,350))

y=[]
for infile in glob.glob('*/*'):
    path=infile.split('/')
    y.append(path[0])
y=np.asarray(y)


clf=knn()
clf2=svm()
clf2.fit(li,y)

pickle.dump(clf2,open("model",'wb'))

