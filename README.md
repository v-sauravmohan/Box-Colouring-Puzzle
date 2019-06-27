# Story
Took part in a coding competition and got destroyed by this challenge. Had to solve this in 45 mins and even after kind of solving this here and wrapped my head around the logic I still believe 45 mins is too short for a person new to this question. My solution might be wrong as i still want to do a lot of testing with different samples of test data. <br />Weapon of choice  - **Python**<br />*Ping me if you have a better solution or if my solution is not right in anyway.*<br />[https://www.linkedin.com/in/sauravmohanv/](https://www.linkedin.com/in/sauravmohanv/)<br />**Thanks in advance.**
# Colouring the Blocks Challange

There are n blocks placed in a row. Each block must be covered with one of the three colors available, but no two adjacent blocks can be the same color. The cost of coloring each block varies and is given in an array. Given the cost of using each color on each block, determine the minimum cost to color all the blocks.

## Example
There are three blocks to color and the cost to use each color for each block is given as <br />cost = [[1,2,3],<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1,2,3],<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3,3,1]].<br /> For the first block, the cheapest color is the first color which costs 1. For the second block, colors cost the same but color 1 cannot be used because it matches the first block. instead, choose color 2. for the third block, it can be color 1 or 3. the cheaper is color 3 at 1 unit. The total cost to color the blocks is 1+2+1 = 4.

## Function Description

Complete the function minPrice in the code. the Function must return an integer that denotes the minimum cost to color all the blocks.

**minPrice( ) has the following parameter:**
cost[cost[ 0 ],.....cost[ n-1 ]]: an array of integers where cost[ i ][ j ] denotes the cost of using the j<sup>th</sup> color on the i<sup>th</sup> block.

## Constrains

 - 1 <= n <= 100 
 - 0 <= cost[ i ][ j ] <=100

## Input

 - The number of rows will always be 3. 
 - Input data ie: cost should be hardcoded.

## Prerequisites
Any version of Python.
## Deployment

Execute the following command to run the program in the ***\Box-Colouring-Puzzle*** directory. Input desired data before running the code.

    python Col-Puzzle.py

## Authors

-   **Saurav Mohan V**  - [LinkedIn](https://www.linkedin.com/in/sauravmohanv/)
- **HackerRank** - Question Courtesy - [Sign-Up!! Its Great](https://www.hackerrank.com/)
Not Sponsored by HackerRank!!!

## License

This project is licensed under the MIT License
