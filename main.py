from imageai.Prediction import ImagePrediction
from prediction import Prediction
import os

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsInceptionV3()
prediction.setModelPath(os.path.join(execution_path, "inception_v3_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()


def readImage():
	predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "cat.jpg"), result_count=5 )

	predictionList = []
	for eachPrediction, eachProbability in zip(predictions, probabilities):
		predictionObj = Prediction(eachPrediction, eachProbability)
		predictionObj.info()
		predictionList.append(predictionObj)

	return  predictionList

readImage()
