### pip install memory-profiler
from memory_profiler import profile
import time
import pandas as pd

# Example of checking time conplexity
def test_time(n):
    # Example algorithm to analyze
    sum = 0
    for i in range(n):
        sum += i
    return sum

input_sizes = [10000,100000,1000000]
for size in input_sizes:
    start_time = time.time()
    result = test_time(size)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Input size: {size}, Elapsed time: {elapsed_time} seconds")



# Example of checking space conplexity
@profile
def test_space():
    csv_file_path = "./data.csv"
    df = pd.read_csv(csv_file_path)
    df_I = pd.read_csv(csv_file_path)

    a = df.iloc[1]
    b = df.iloc[2]



test_space()