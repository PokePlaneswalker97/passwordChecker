# passwordChecker
author: PokePlaneswalker97@gmail.com

Checks the strength of a password using techniques similar to other password strength checkers, but with possibly funnier messages.

This program runs a password strength checker on a String inputted by a user. This input is not checked properly for inject attacks (as I understand them). Once a String is input by the user (via enter/return), the String is then checked for length and use of various regEx characters to see if the password is more or less secure. 

As far as I'm aware, the only dependency to run this code is the ability to run python code. One method to run it is to open up a terminal, go to the directory where the file itself is stored, and use the command 'python3 passwordChecker.py'. python3 could be switched out for whatever command the user needs to run python code.

This program is for educational purposes only. It does check the user's input against modern password strength checking techniques, but I would recommend using some other strength checker. As previously stated, I have not vetted my code against inject attacks and similar hacking methods.

Responsible use of this program would be personal use to see if your password would be strong enough to use on certain websites that don't have proper password strength checker. I would recommend against using this as a substitute for actual security as it would give users a false sense of security. Others may copy this code and find ways to log the user's input to save to their malicious input tables. Or someone could modify this and sneak in something that would cause the code to lie (i.e., causing the variables to always show secure outcome) or add lines that would have the user type in the password again so it would save to a malicious actor's computer. Please be cautious.
