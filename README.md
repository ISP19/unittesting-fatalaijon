## Unit Testing a Fraction class and List Utilities.

[![Build Status](https://travis-ci.com/fatalaijon/unittesting-fatalaijon.svg?branch=master)](https://travis-ci.com/fatalaijon/unittesting-fatalaijon)
[![codecov](https://codecov.io/gh/fatalaijon/unittesting-fatalaijon/branch/master/graph/badge.svg)](https://codecov.io/gh/fatalaijon/unittesting-fatalaijon)


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| what other test case?  |  what result?       |


## Test Cases for Fraction

Extended number arithmetic is beyond the requirements of this assignment,
but I test these anyway out of curiosity.  In most cases, operations get
the correct result w/o any special code.

`infinity` means Fraction(1,0), `-infinity` is Fraction(-1,0), and `NaN` is Fraction(0,0).  `f` means any finite, non-zero fraction.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| add typical fractions  |  correct sum        |
| f + zero               |  f                  |
| f + infinity           |  f                  |
| infinity + infinity    |  infinity           |
| zero + infinity        |  infinity           |
| NaN + infinity         |  NaN                |
| infinity + -infinity   |  NaN                |
| NaN + anything         |  NaN                |

