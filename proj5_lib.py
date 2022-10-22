# proj5_lib.py 
# Academic Integrity Statement: I certify that, while others may have assisted me in brain storming, debugging and validating this program, the program itself is my own work. I understand that submitting code which is the work of other individuals is a violation of the course Academic Integrity Policy and may result in a zero credit for the assignment, or course failure and a report to the Academic Dishonesty Board. I also understand that if I knowingly give my original work to another individual that it could also result in a zero credit for the assignment, or course failure and a report to the Academic Dishonesty Board. See Academic Integrity Procedural GuidelinesLinks to an external site. at:  https://psbehrend.psu.edu/intranet/faculty-resources/academic-integrity/academic-integrity-procedural-guidelinesLinks to an external site.
# Assisted by and Assisted line numbers:
# Your Name: Keian Kaserman
# Your PSU user ID:  knk5281
# Course title CMPSC 465
# Due Time: 11:59, Monday, October 24, 2022
# Time of Last Modification: 7:54, Saturday, October 22, 2022
# Description: Provides functions used in main program logic

## Get input test cases
def getTestCases(filename):
  with open(filename) as f:
    lines = f.readlines()

  lines = [line.rstrip('\n') for line in lines]
  return lines

## print output
def printOutput(inv):
  print(f'The sequence has {inv} inversions.')

## Merge sort
def mergeSort():
  