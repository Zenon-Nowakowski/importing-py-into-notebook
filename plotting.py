import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from random import choice
import time
from string import ascii_lowercase

def create_random_dataframe(num_el, id_len):
    magnitude = list(np.random.randint(1,101,num_el))
    ids = lst = [''.join(choice(ascii_lowercase) for _ in range(id_len)) for _ in range(num_el)]

    data = {'magnitude':magnitude, 'id':ids}

    return pd.DataFrame(data, columns=['magnitude','id'])
def meaningless_math(mag):
    return np.log(mag) ** np.sqrt(mag)

def main():
        
    MAX_LEN = 1000  # Maximum number of rows in the DataFrame
    ID_LEN = 25 # length of the ID

    # Initialise results containers
    l_v = []
    t_v = []
    l_a = []
    t_a = []

    for length in range(10, MAX_LEN, 10):
        # Generate the random DataFrame
        df = create_random_dataframe(length, ID_LEN)
        
        start = time.perf_counter()
        meaningless_math(df['magnitude'].values)
        end = time.perf_counter()

        # Store results
        l_v.append(length)
        t_v.append(end - start)

        start = time.perf_counter()
        df.apply(lambda row: meaningless_math(row['magnitude']), axis=1)
        end = time.perf_counter()

        # Store results
        l_a.append(length)
        t_a.append(end - start)

    # Plot results
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Pandas Query - Time Complexity")
    plt.xlabel("Number of rows")
    plt.ylabel("Execution Time (s)")
    plt.plot(l_v, t_v, label="vectorization")
    plt.plot(l_a, t_a, label="apply()")
    plt.legend()
    plt.tight_layout()
    plt.show()