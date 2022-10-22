# Can't rename this file to match project submission guidelines
# of proj5.py without breaking REPL and testing execution to the right

# main.py:
# Academic Integrity Statement: I certify that, while others may have assisted me in brain storming, debugging and validating this program, the program itself is my own work. I understand that submitting code which is the work of other individuals is a violation of the course Academic Integrity Policy and may result in a zero credit for the assignment, or course failure and a report to the Academic Dishonesty Board. I also understand that if I knowingly give my original work to another individual that it could also result in a zero credit for the assignment, or course failure and a report to the Academic Dishonesty Board. See Academic Integrity Procedural GuidelinesLinks to an external site. at:  https://psbehrend.psu.edu/intranet/faculty-resources/academic-integrity/academic-integrity-procedural-guidelinesLinks to an external site.
# Assisted by and Assisted line numbers:
# Your Name: Keian Kaserman
# Your PSU user ID:  knk5281
# Course title CMPSC 465
# Due Time: 11:59, Monday, October 24, 2022
# Time of Last Modification: 7:56, Saturday, October 22, 2022
# Description: Provides functions used in main program logic

from proj5_lib import getTestCases, printOutput

tests = getTestCases('input-1.txt')
inversions = []
# Use divide and conquer with efficiency nlogn
# Use recursion ^
# Inversion == when i < j and test[i] > test[j]

for inv in inversions:
  printOutput(inv)
## Sample Output:
#