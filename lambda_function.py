import pickle
import json

# Load the model
filename = "iris_model.sav"
model = pickle.load(open(filename, "rb"))


def predict(features):
    return model.predict(features).tolist()


def lambda_handler(event, context):
    # TODO: Implement your own lambda_handler logic here
    # You will need to extract the 'values' from the event and call the predict function.

    try:
        # Extract the 'values' from the event
        body = json.loads(event.get("body"))
        values = body.get("values")
        print(values)

        # Call the predict function
        predictions = predict(values)

        # Return the predictions as a JSON response
        return {"statusCode": 200, "body": json.dumps(predictions)}
    except (KeyError, json.JSONDecodeError):
        return {"statusCode": 400, "body": json.dumps({"error": "Invalid input"})}
