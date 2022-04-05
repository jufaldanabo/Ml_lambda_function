import tempfile
import joblib
import boto3

client_s3 = boto3.client('s3')


def load_model(filename_model: str, name_bucket: str) -> object:
    """

    :param model:
    :param filename_model:
    :param name_bucket:
    :return:
    """
    with tempfile.TemporaryFile() as fp:
        client_s3.download_fileobj(name_bucket, Fileobj=fp, Key=filename_model)
        fp.seek(0)
        model = joblib.load(fp)

    return model
