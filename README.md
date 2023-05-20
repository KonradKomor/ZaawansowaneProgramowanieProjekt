# ZaawansowaneProgramowanieProjekt

Simple Python project that demonstrates how to use the spaCy library with the spaCy-TextBlob extension to analyze the sentiment of text. The script also includes a FastAPI application that exposes endpoints for testing purposes.


## Usage
### Prerequisites
Before running the script, make sure you have installed all necessary libraries. 

You can install them using pip:
```
pip install -r requirements.txt
```
### Local deployment
To start the server clone the repository, move to the project directory and use a following command:
```
uvicorn main:app --reload
```
Server will listen for incoming requests on http://localhost:8000

### Docker
You can run the project by navigating to the project directory and then building the Docker image by using:
```
sudo docker build -t sentiment .
```
After the build process completes, you can run a container based on the image using the following command
```
sudo docker run -d --name sentiment -p 8000:8000 sentiment
```

### Testing the endpoints

Once the server is running, you can test the endpoints using a tool like cURL or a web browser:

To test the /sentiment endpoint, send a POST request to http://localhost:8000/sentiment with the following JSON payload:
```
{
  "text": "I love this product!"
}
```
API endpoints documentation will be available at http://localhost:8000/docs.
