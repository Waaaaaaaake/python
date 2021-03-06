'''
Create a function where given the number n to count down from, and some words txt,
return a countdown sequence as a string leading up to the words at the end.

Put a full stop after each number and uppercase and add an exclamation mark
to the word. See the examples below for clarification!
'''

def countdown(num, txt):
    return '. '.join([str(i) for i in range(num, 0, -1)]) + '. ' + txt.upper() + '!'

print(countdown(10, "Blast Off"))
  # "10. 9. 8. 7. 6. 5. 4. 3. 2. 1. BLAST OFF!"

# countdown(3, "go")  "3. 2. 1. GO!"

# countdown(5, "FIRE")  "5. 4. 3. 2. 1. FIRE!"
