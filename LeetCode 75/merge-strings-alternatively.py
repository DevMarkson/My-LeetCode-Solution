def mergeAlternately(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """

    # initialize the merged words to an epmty string
    merged_words = ""

    # store the minimum length in a container
    length = min(len(word1), len(word2))

    # loop through the range of length and append the words to the merged words
    for i in range(length):
        merged_words += word1[i] + word2[i]

    # Append any remaining characters from the longer word
    if len(word1) > length:
        merged_words += word1[length:]
    elif len(word2) > length:
        merged_words += word2[length:]

    # return merged words
    return merged_words
