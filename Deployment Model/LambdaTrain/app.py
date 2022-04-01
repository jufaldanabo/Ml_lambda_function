
from functions import create_model
from utils import save_model


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    try:
        model = create_model()
        save_model(model=model, filename_model=event['filename_model'], name_bucket=event['name_bucket'])

        return {
            "statusCode": 200,
            "message":"Train successfully"
            }
    except Exception as e:
        print("Error {}".format(e))
        return {"statusCode": 500,"message":"Internal server error"}
