import os
from glob import glob


# data_dirs = ["Training_Batch_Files","Prediction_Batch_files"]
data_dirs = ['F:\Internship project\Machine Learning\Fraud Detection\Fraud_detection_dvc_mlops\data\raw\creditcard.csv']
for data_dir in data_dirs:
    files = glob(data_dir + r"/*.csv")
    for filePath in files:
        # print(f"dvc add {filePath}")
        os.system(f"dvc add {filePath}")

print("\n #### all files added to dvc ####")