# Experiments file for question 2.
# Fill in the specification for the two RAM programs and use the provided graphing function to graph the running times.
# Run `python experiments.py` to generate the plot.

import simulator

import matplotlib.pyplot as plt
import time


# Problem 2: Writing the RAM programs
# For readibility purposes, we have defined the following Python variables for you to use in your RAM programs. 
# Your RAM program should be a list of length l where the 0th element is an int representing the number of variables 
# used by the program. The subsequent (l-1) elements of the list will be the commands in order. 
# Each command can be represented by a list containing a command (string), followed by any arguments the command takes (ints).
# Please refer to the test file `test.py` to see examples of RAM programs.

# variables
input_len_id = 0
output_ptr_id = 1
output_len_id = 2
zero_id = 3
one_id = 4
counter_id = 5
result_id = 6
temp_id = 7    # Used only in prog2
W_id = 8       # Used only in prog2

# TODO: Fill in prog1 with the first RAM program provided in the homework.
prog1 = []

# TODO: Fill in prog2 with the second RAM program provided in the homework.
prog2 = []


# Helper functions for plotting runtimes

# Time a function call on a given input
def time_fun (fn, input):
    start_time = time.time()
    fn(input)
    end_time = time.time()
    return end_time - start_time

def run_prog1 (n):
    return simulator.executeProgram(prog1, [n])[0]

def run_prog2 (n):
    return simulator.executeProgram(prog2, [n])[0]

# Plot both RAM programs' running times and save as `running_times.png`
def graph ():
    input_range = range(0, 15)
    prog1_time = [time_fun(run_prog1, i) for i in input_range]
    prog2_time = [time_fun(run_prog2, i) for i in input_range]
    plt.plot(input_range, prog1_time, label="Program 1")
    plt.plot(input_range, prog2_time, label="Program 2")
    plt.xlabel('Input')
    plt.ylabel('Running Time (in seconds)')
    plt.legend()
    plt.savefig('running_times.png', bbox_inches = "tight")
    plt.show()

if __name__ == "__main__":
    graph()
