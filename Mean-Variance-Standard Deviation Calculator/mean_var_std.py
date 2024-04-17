import numpy as np

def calculate(list):
    calculations = {}  
    if len(list) == 9:
        raw_matrix = [
            list[0:3],
            list[3:6],
            list[6:9]
        ]
        matrix = np.array(raw_matrix, dtype=int)
        mean = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix)]
        calculations["mean"] = mean
        variance = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix)]
        calculations["variance"] = variance
        standard_deviation = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix)]
        calculations["standard deviation"] = standard_deviation
        _max = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix)]
        calculations["max"] = _max
        _min = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix)]
        calculations["min"] = _min
        _sum = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix)]
        calculations["sum"] = _sum
    else:
        raise ValueError("List must contain nine numbers.")
    return calculations
