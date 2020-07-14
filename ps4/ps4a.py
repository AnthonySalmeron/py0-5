# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence, sequence_dict=0, permutations={}, str=""):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if not sequence_dict:
        sequence_dict = {}
        for char in sequence:
            sequence_dict[char] = sequence_dict.get(char,0) + 1
    for letter in sequence_dict:
        copy_str = str
        copy_str += letter
        copy_dict = sequence_dict.copy()
        copy_dict[letter] = copy_dict.get(letter) - 1
        if not copy_dict.get(letter):
            del copy_dict[letter]
        if not copy_dict:
            permutations[copy_str] = 1
            return
        get_permutations(sequence,copy_dict,permutations,copy_str)
    return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

    print(get_permutations(input('Put word here: ')))
