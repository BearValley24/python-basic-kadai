# -*- coding: utf-8 -*-
"""kadai008.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gLXfVhqb-HtfaRhI03D55xLqKaRMRmyN
"""

var = 15

if var % 15 == 0:
  print('FizzBuzz')
elif var % 3 == 0:
  print('Fizz')
elif var % 5 == 0:
  print('Buzz')
else:
  print(var)