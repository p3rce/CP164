"""
------------------------------------------------------------------------
[Assignment 1, Functions File]
------------------------------------------------------------------------
Author: Pierce Goulimis
ID:     210276250
Email: goul6250@mylaurier.ca
__updated__ = "2022-01-12"
------------------------------------------------------------------------
"""



def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    
    cleanlist = []
    
    for i in values:
        if i not in cleanlist:
            cleanlist.append(i)
    
    print("Cleaned: ", cleanlist)
    return



def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    out = ""
    
    for i in range(len(s)):
        if s[i] not in vowels:
            out += s[i]
            
    return out



def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    
    u, l, d, w,r = 0,0,0,0,0
    
    for i in fv.read():
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
        elif i.isdigit():
            d += 1
        elif i == " ":
            w+= 1
        else:
            r += 1
            
    return u,l,d,w,r
    


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    
    leap_year = False
    
    if year % 4 == 0 and year % 100 != 0:
        leap_year = True
    elif year % 400 == 0:
        leap_year = True
    elif year % 1 == 0:
        leap_year = False
    else:
        leap_year = False
        
    return leap_year
    



def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    
    s = s.lower()
    s_rev = reversed(s)
    
    if list(s) == list(s_rev):
        return True
    
    else:
        return False
    
    
    
            



def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    
    l = []
    
    if len(a) == 0:
        md = 0
    else:
        for i in range(len(a)-1):
            diff = abs(a[i+1]-a[i])
            l.append(diff)
    md = max(l)
    return md


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    
    b = []
    
    for i in range(len(a[0])):
        b.append([])
        
    
    for i in range(len(a)):
        for x in range(len(a[0])):
            b[x].append(a[i][x])
            
    return b



def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    
    small = 0.00
    large = a[0]
    total = 0.00
    average = 0.00
    aLen = len(a)
    
    for i in range(aLen):
        if a[i] < small:
            small = a[i]
        elif a[i] > large:
            large = a[i]
        total = total + a[i]
        
    average = total // aLen
    
    return small,large,total,average
    

def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    
    pl = ""
    vowels = "aeiou"
    isCap = False
    
    if not word[0].islower():
        isCap = not isCap
        
    if word[0] in vowels:
        p1 = word + "way"
        
    else:
        consonants = ""
        others = ""
        
        
        for i in word:
            if i in (vowels + "y"):
                others += i
                
            else:
                consonants += i
                
        if isCap:
            pl = others[0].capitalize() + others[1:].lower() + consonants.lower() + "ay"
            
        else:
            pl = others + consonants.lower() + "ay"
            
    
    return pl
    
