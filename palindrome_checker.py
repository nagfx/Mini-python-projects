# Built a palindrome checker as part of course challenge by Naman

# we define a function first


def palindrome_checker(test_string):
    # we are making use of the slice technique to list a string backwards
    if test_string == test_string[::-1]:
        return True
    return False


run = True
while (run):
    test_string = input(
        "Kindly input text to check if palindrome or not, you can type 'exit' to quit ")
    # if the user entered 'exit' then we will close the program
    if test_string.lower() == "exit":
        run = False
        break

    test_string = test_string.lower()

    newstring = ""
    for x in test_string:
        if x.isalnum():
            newstring += x

    print("Palindrome test:", palindrome_checker(newstring))
