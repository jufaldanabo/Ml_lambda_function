from utils import  load_model

def inference(x_test,filename_scaler,filename_model,name_bucket):
    scaler = load_model(filename_model=filename_scaler,name_bucket=name_bucket)
    inference_model = load_model(filename_model= filename_model,name_bucket=name_bucket)

    test_array = scaler.transform(x_test)
    output = inference_model.predict(test_array)
    if output == 1:
        result = "virginica"
    else:
        result = "Not virginica"

    return result



