# penr-oz-openai
Microservice with Python REST calling OpenAI

This microservice uses the Flask framework to create a web server and define an endpoint 
for handling GET requests to the `/openai-api` route. The prompt parameter is extracted from 
the query string of the request using request.args.get(), and is then passed to the 
openai.Completion.create() method along with other parameters such as the OpenAI engine, 
the maximum number of tokens to generate, and the temperature for controlling the randomness 
of the output.

The API key for accessing the OpenAI API is obtained from an environment variable 
`OPENAI_API_KEY` using os.environ. The response from the OpenAI API is then returned 
as a JSON object using jsonify().

# build
```shell
pip install requirements.txt
```

# run
```shell
./skaffold run
```
 to build and deploy the Helm chart to a local Minikube cluster

# test
access via http://localhost:5000/openai-api

### Reference Documentation
For further reference, please consider the following sections:

* [OpenAI](https://chat.openai.com/)
* [Docker Overview](https://docs.docker.com/get-started/overview/)
* [Minikube](https://minikube.sigs.k8s.io/docs/start/)
* [Skaffold Overview](https://skaffold.dev/)
