Arithmetic Exam Application
=================
1) With the first message, the program should ask for a difficulty level:
* `1 - simple operations with numbers 2-9`
* `2 - integral squares 11-29`
2) Two difficulty levels:
- For the first difficulty level: the task is a simple math operation; the answer is the result of the operation.
- For the second difficulty level: the task is an integer; the answer is the square of this number.
In case of another input: ask to re-enter. Repeat until the format is correct.

3) The application gives 5 tasks to solve.

- If the answer contains a typo, user will get `"Incorrect format."` message and program will ask to re-enter the answer. 
- If the answer is a number, user will see `"Right!"` or `"Wrong!"` Go to the next question.

4) After five answers, user will get `"Your mark is N/5."` where `N` is the number of correct answers.


5) The results would be saved to the file immediately after the user gave the positive answer to the question `"Would you like to save your result to the file?"`
in file `results.txt` 
