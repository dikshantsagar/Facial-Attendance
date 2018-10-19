<h1>Facial-Attendance</h1>
<h2>An AttendanceSystem using Facial Recognition using OpenCV and Machine Learning.</h2>

<b><u>Flow of Development</u></b> :
* First tried face detection through Haarcascades(face.xml) in standard OpenCV.
* Processed detected face crops[] captured through OpenCV.
* After the Dataset was prepared , tried using KNN(K-nearest neighbours) from sklearn and got nice results, with only 20         picture snaps per subject.
* After a bit of testing the model started failing in some cases, thats when i implimented SVM(Support Vector Machine) from        sklearn for the model and got enhanced results than before.
* Then i broke the whole program into different modules : 
     1. for forming the dataset
     2. for training and saving the model into a file using pickle module.
     3. for reading the trained model using pickle , capturing test image and passing throught the model for predictions and            drew on the OpenCV Image , and made the test programme run in a loop to exhibhit realtime predictions.

<b><u>Current Features</u></b> :
* Takes pictures through the webcam and creates a dataset for users using m images.(m can vary)
* Trains a SVM model using the dataset
* Takes realtime images and provides realtime predictions.
* Train Time(for 4 subjects - 20 images each => ~1min.)
* Testing Time(realtime)


<b><u>How to use</u></b> :
* after cloning the repository , open terminal in the directory and run command : `python3 -B formdataset.py`
the program will prompt you to enter the Subects Name, enter that and the program will start taking m pictures(m can be varied in the code). Try to move the subjects head a bit(slowly) while the program takes pictures to get different angles.
* After the datasets are formed in the same terminal run command : `python3 -B train.py` then wait.....
* Then run : ` pyhthon3 -B test.py` and enjoy.

<b>Features to be added : </b>
* Using the realtime prediction to mark attendance of the subject on a remote server database.
* Adding time Constraints in testing module for strict and unique attendance whilst communicating with the database to maintain attendance for different Courses in a single day.
