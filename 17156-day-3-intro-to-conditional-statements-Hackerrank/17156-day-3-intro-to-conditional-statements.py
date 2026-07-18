
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    
    # Your logic must be indented inside here:
    if N % 2 != 0:
        print('Weird')
    elif 2 <= N <= 5:
        print('Not Weird')
    elif 6 <= N <= 20:
        print('Weird')
    else:
        print('Not Weird')


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna