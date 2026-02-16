import re;

def checkStrength(password):
    #Criteria we check against: length, upper & lowercase letters, symbols, and numbers.
    lengthOk = len(password) >= 8
    hasUpper = re.search(r"[A-Z]", password) is not None
    hasLower = re.search(r"[a-z]", password) is not None
    hasNum = re.search(r"\d", password) is not None
    hasSymbol = re.search("[ !@#$%^&*()-+=_~`:;,<>.?|]", password) is not None

    #Now we take these booleans and make them flags. If all flags are true, feedback should be succint.
    boolFlags = [lengthOk, hasUpper, hasLower, hasNum, hasSymbol]
    flagCount = 0
    feedback = ""

    for flag in boolFlags:
        if flag == True:
            flagCount += 1

    match flagCount:
        case 0:
            feedback = "Did... did you even enter anything? THAT\'S NOT A PASSWORD!!! INSECURE!!!\n"
        case 1:
            feedback = "This password would be easy to crack. Were you even trying?\n"
        case 2:
            feedback = "Look, even a monkey could do this. You can do better than that.\n"
        case 3:
            feedback = "Okay, now we're getting somewhere. Let's try to incorporate these next bits into your password next time, ya?\n"
        case 4:
            feedback = "This is a pretty solid password, but you can strengthen it with this suggestion:\n"
        case 5:
            feedback = "Huh. That is one secure password. Just don't let anyone else know what it is, and you\'re good!"
        case _:
            feedback = "Uh...I...I think something broke. How did you even get to this part of the code?"
    
    if not lengthOk:
        feedback = feedback + "You should add a few more characters there my guy; at least have 8.\n"
    if not hasUpper: 
        feedback = feedback + "Seems like you could use some capital letters to make it stronger.\n"
    if not hasLower: 
        feedback = feedback + "Whoa dude, no need to shout and swear at me. Get some lowercase letters in there.\n"
    if not hasNum:
        feedback = feedback + "What, you couldn't be bothered to add a single number? Come on, you're better than a kindergartener.\n"
    if not hasSymbol:
        feedback = feedback + "A symbol might be nice; It requires more complicated input and it is not as easy to check for when trying to crack your password.\n"

    return feedback
                
if __name__ == "__main__":
    try:
        import getpass
        password = getpass.getpass("Enter a password to strength check: ")
    except ImportError:
        password = input("Enter a password to strength check: ")

    message = checkStrength(password)
    print(f"\n{message}")
