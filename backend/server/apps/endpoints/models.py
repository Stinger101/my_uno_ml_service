from django.db import models

# Create your models here.
class Endpoint(models.Model):
	'''
	The Endpoint object represents ML API endpoint
	
	Attributes:
		name: the name of the endpoint, it will be used in API URL
		owner: the string with owner name,
		created_at: the date when the endpoint was created.
	'''
	name = models.CharField(max_length=128)
	owner = models.CharField(max_length=128)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)

class MLAlgorithm(models.Model):
	'''
	The MLAlgorithm model represents the MLAlgorithm object
	
	Attributes:
		name: The name of the algorithm
		description: The short description of how it works
		code: The code of the algorithm
		version: The version of the algorithm similar to the software version
		owner: The name of the owner
		created_at: The date the MLAlgorithm was added
		parent_endpoint: The reference to the Endpoint
	'''

	name = models.CharField(max_length=128)
	description = models.CharField(max_length=1000)
	code = models.CharField(max_length = 50000)
	version = models.CharField(max_length=128)
	owner = models.CharField(max_length=128)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

class MLAlgorithmStatus(models.Model):
	'''
	The MLAlgorithmStatus represent status of the MLAlgorithm which can change during the time.

	Attributes:
		status: The status of the algorithm in the endpoint. Can be: testing, staging, production, ab_testing.
		active: The boolean flag which point to currently active status
		created_by: The name of the creator
		created_at: The date of status creation
		parent_mlalgorithm: The reference corresponding to the MLAlgorithm
	'''

	status = models.CharField(max_length=128)
	active = models.BooleanField()
	created_by = models.CharField(max_length=128)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="status")

class MLRequest(models.Model):
	'''
	The MLRequest model will keep information about all requests to the MLAlgorithms.

	Attributes:
		input_data: The input data to the MLAlgorithm in JSON format.
		full_response: The response of the MLAlgorithm.
		response: The response of the MLAlgorithm in JSON format.
		feedback: The feedback about the response in JSON format.
		created_at: The date when the request was created.
		parent_mlalgorithm: The reference to the MLAlgorithm
	'''

	input_data = models.CharField(max_length=10000)
	full_response = models.CharField(max_length=10000)
	response = models.CharField(max_length=10000)
	feedback = models.CharField(max_length=10000, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)

