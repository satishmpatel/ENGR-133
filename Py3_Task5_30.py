"""
===============================================================================
ENGR 13300 Fall 2023

Program Description
    Replace this line with a description of your program.

Assignment Information
    Assignment:     Team HW7 - PY 5
    Author:         Satish Patel, pate1903@purdue.edu, Luke Schlosser, schlosse@purdue.edu, Elizabeth Kanemitsu Ekanemit@purdue.edu, Darla Knaack dknaack@purdue.edu
    Team ID:        LC2 - 30 (e.g. LC1 - 01; for section LC1, team 01)

Contributor:    Satish Patel, pate1903@purdue [repeat for each]
    My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Contributor:    Luke Schlosser, schlosse@purdue [repeat for each]
    My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Contributor:    Elizabeth Kanemitsu, ekanemit@purdue [repeat for each]
    My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Contributor:    Darla Knaack, dknaack@purdue [repeat for each]
    My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""
import numpy as np
import matplotlib.pyplot as plt

i = np.arange(1000)
start = 0
end = 999
intial = 0

f_i = np.sin(np.pi * i/500) ** 2
g = [0.0625, 0.25, -0.375, 0.25, 0.0625]

h = np.zeros(len(f_i))

for i in range(len(f_i)):
    for j in range(len(g)):
        if i + j < len(f_i):
            h[i] += g[j] * f_i[i + j]

print(h[:10])


