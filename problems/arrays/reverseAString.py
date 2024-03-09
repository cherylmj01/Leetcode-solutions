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

print(reverseAString(("Cheryl")))

