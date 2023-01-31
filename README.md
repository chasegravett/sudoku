Hello There!
Thank you for checking out my command-line sudoku solver!

This little personal project was inspired by LeetCode's "Valid Sudoku" problem:
  https://leetcode.com/problems/valid-sudoku/
  
I was so excited about figuring out how to determine if a board was valid that I wondered what other sudoku-related functionality I could implement.

I brought my solution from that problem into my own project and built up from there.
Now from the commmand line you can start the project via the "main.py" file.

Once started, you will be prompted to enter the numbers that fill your sudoku board one line at a time, using 0 for all blanks.

The program will tell you immediately if the line you just entered is not valid.
Once all 9 rows have been entered, the board is validated as a whole, targeting each row, column, and 3x3 box.

Once it is validated, you will see a copy of your board printed out to the terminal. 
Shortly following, another board will be printed out with the answered spaces :)
