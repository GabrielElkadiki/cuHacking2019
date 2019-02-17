
To be able to run this you need the imported packages 
Clone tensorflow/models repository 
Also clone the repository from tensorflow git page and the protoc-3.4.0-osx-x86_64
Build the protoc files in the /Tensorflow/models/research/object_detection/protos

For windows 
“C:\protoc-3.4.0-win32\bin\protoc.exe” object_detection/protos/*.proto --python_out=.

Go to System -> Advanced system settings -> Environment Variables -> System Variables -> New, and add a variable with the name PYTHONPATH and these values:
C:\Program Files\Python36\
C:\TensorFlow\models
C:\TensorFlow\models\research
C:\TensorFlow\models\research\slim
C:\TensorFlow\models\research\object_detection

Use frozen weights to run the graph in the code 
Label and graph files on GitHub 

Don’t forget to change the paths in tf.py
