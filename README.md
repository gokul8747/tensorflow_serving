# Tensorflow Serving

TF Serving allows you to easily expose a trained model via a model server. It provides a flexible API that can be easily integrated with an existing system.   
Model serving is simply the exposure of a trained model so that it can be accessed by an endpoint. Endpoint here can be a direct user or other software.

Steps for Serving a Docker TensorFlow Model   
1. Export the TensorFlow Model
   * refer sign_language_train.ipynb
  
2. Download the TensorFlow Serving Image
   * docker pull tensorflow/serving

3. Run the TensforFlow Serving Container
   * docker run -p 8501:8501 --name <YOUR_MODEL_NAME>_serving \

--mount type=bind,source=/{path to your directory with saved file}/TF-Docker-Serving/<YOUR_MODEL_NAME>/,

target=/models/<YOUR_MODEL> \

-e MODEL_NAME=<YOUR_MODEL_NAME> -t tensorflow/serving         
4. Send Prediction Requests 
  * You can send prediction requests to the TensorFlow Serving server using a HTTP REST API or gRPC interface
  * refer prediction.py
