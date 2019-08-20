def duplicate_count(text):
    '''
    Returns count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
    >>> duplicate_count('abcde')
    0
    >>> duplicate_count('abcdea')
    1
    >>> duplicate_count('indivisibility')
    1
    >>> duplicate_count('aabBcde')
    2
    >>> duplicate_count('aabbcde')
    2
    >>> duplicate_count('aA11')
    2
    >>> duplicate_count('ABBA')
    2
    '''
    unique_characters = set(text.upper())
    duplicate_characters = []

    for character in unique_characters:
        if text.upper().count(character) > 1:
            duplicate_characters.append(character)
    return len(duplicate_characters)
