import numpy as np

metrics=[10.0,12.0,12.0,13.0,12.0,11.0,14.0,100.0,12.0]

def detect_outliers_zscore(values,threshold=2.0):
    arr=np.array(values)
    mean=np.mean(arr)
    std=np.std(arr)
    z=np.abs((arr-mean)/std)
    return arr[z>threshold].tolist()

outliers=detect_outliers_zscore(metrics,2.0)
print(outliers)