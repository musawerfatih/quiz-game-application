# True or False Quiz Application
This is a Python program that allows users to take a quiz based on True or False questions. The program fetches 10 questions from the Open Trivia Database API and displays them in a beautiful GUI. Users can select either True or False as their answer, and the program will provide immediate feedback by changing the color of the canvas and displaying a message.


# Features
- Fetches 10 questions from the Open Trivia Database API using API and stores them in JSON format
- Displays the user's score at the top of the window
- Displays each question in a canvas below the score
- Provides two buttons for True and False answers
- Gives immediate feedback by changing the color of the canvas and displaying a "Correct" or "Incorrect" message
- Disables the buttons after 10 questions and shows the user's total score


# Screenshots
![image](https://user-images.githubusercontent.com/63827449/229089934-5122bee1-4a5d-4891-87ab-75ba29120c47.png)
![Screenshot (51)](https://user-images.githubusercontent.com/63827449/229091610-50565443-eca2-401b-8f42-1f9b09b92d0e.png)
![Screenshot (52)](https://user-images.githubusercontent.com/63827449/229091313-02c2c62b-966a-49ac-9832-293b70a153b4.png)
![image](https://user-images.githubusercontent.com/63827449/229092122-dc7e354a-ee43-418b-bfbb-de7e9b393242.png)


# How to Use
1. Clone the repository to your local machine.
2. Open the terminal or command prompt and navigate to the directory containing the cloned repository.
3. Install the required packages using the following command:
```
pip install -r requirements.txt
```
   
4. Run the program by executing the following command:
```
python main.py
```
     
5. The program will display the first question in the GUI.
6. Click on either the True or False button to select your answer.
7. The program will display a message indicating whether your answer was correct or incorrect.
8. The program will then display the next question.
9. Repeat steps 6-8 until you have answered all 10 questions.
10. At the end of the quiz, the program will display your total score and disable the True and False buttons.
