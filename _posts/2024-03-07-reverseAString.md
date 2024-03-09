---
title: Reverse a string
author: Cheryl Myers
date: 2024-03-07
category: Jekyll
layout: post
---

### Problem Statement

Write a function that reverses a string. The input string is given as an array of characters `s`.

#### Python code with explanation

There are a few ways we can solve this problem :

#### Solution 1 :

```python
def reverseAString(stringLine):

    # check if the string is valid or not
    if not stringLine or len(stringLine) < 2 or not isinstance(stringLine, str):
        # if it is not valid then return "Invalid input"
        return "Invalid input"

    # Create an empty array to contain the new reversed string
    reversedStringLine = []

    #Get the string length
    totalStringLength = len(stringLine) - 1

    # Create a for loop which has the following parameters
    # Start: The first number in the sequence.
    # Stop: The sequence stops at this number without including it.
    # Step: The difference between each number in the sequence.
    for i in range (totalStringLength, -1, -1) :
        # Add the character to the empty array
        reversedStringLine.append(stringLine[i]);

    # join the characters in the array
    reversedString = ''.join(reversedStringLine);
    return (reversedString);
```

#### Solution 2 :

```python
def reverseAString(stringLine):

    # check if the string is valid or not
    if not stringLine or len(stringLine) < 2 or not isinstance(stringLine, str):
        # if it is not valid then return "Invalid input"
        return "Invalid input"

    # The first : is for start location
    # so we are not specifying any start location
    # The second : is for end location
    # so we are not specifying any end location
    # -1 indicates how we should step up or step down
    # - means we should step down and python will know that we have to step down from the end of the string
    return stringLine[::-1]
```

#### Solution 3 :

```python
def reverseAString(stringLine):

    # check if the string is valid or not
    if not stringLine or len(stringLine) < 2 or not isinstance(stringLine, str):
        # if it is not valid then return "Invalid input"
        return "Invalid input"

    # The first : is for start location
    # so we are not specifying any start location
    # The second : is for end location
    # so we are not specifying any end location
    # -1 indicates how we should step up or step down
    # - means we should step down and python will know that we have to step down from the end of the string
    return stringLine.reverse
```

---

### Another Variation

This problem can also be stated as :

_Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array `in-place` with `O(1)` extra memory._

```python
def reverseStringInPlace(s):

        if (not isinstance(s, list)):
            print("Invalid input")
            return None

        totalLength = len(s)-1
        left = 0
        right = totalLength

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return (''.join(s))

print(reverseStringInPlace(list("Hello")))
```
