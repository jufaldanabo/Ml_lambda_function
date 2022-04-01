import tempfile
import joblib
import boto3

client_s3 = boto3.resource('s3')


def save_model(model: object, filename_model: str, name_bucket: str) -> str:
    """

    :param model:
    :param filename_model:
    :param name_bucket:
    :return:
    """
    with tempfile.TemporaryFile() as fp:
        joblib.dump(model, fp)
        fp.seek(0)
        client_s3.Bucket(name_bucket).put_object(Key=filename_model, Body=fp.read())

    return "save model successfully"
