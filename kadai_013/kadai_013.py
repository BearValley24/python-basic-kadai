# -*- coding: utf-8 -*-
"""kadai_013.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RUQzekhEK5qc7wDs6-hgpXYdiHXA2cN7
"""

tax = 0.1
def total(price,tax):
  total = price + price * tax
  return total

# total(6395,tax)
print(f"{total(6395,tax)}円")
