def check_plagiarism(file_1, file_2):
    """
    Detects if `file_1` and `file_2` share five or more consecutive words.
    If there are, returns longest such string of words. If not, return False.

    Files are lower-case text and spaces only.
    """

    # Read in and prepare data
    inputfile_1 = open(file_1, "r")
    output_1 = ""
    for line in inputfile_1:
        output_1 += line
    output_1 = output_1.split()
    inputfile_2 = open(file_2, "r")
    output_2 = ""
    for line in inputfile_2:
        output_2 += line
    output_2 = output_2.split()

    longest_match = False
    for i in range(0, len(output_1) - 5):
        for j in range(0, len(output_2) - 5):
            # if match detected, create new index and go forward
            if output_1[i] == output_2[j]:
                match = []
                m = i
                n = j
                while output_1[m] == output_2[n] and m <= len(output_1) - 1:
                    match.append(output_1[m])
                    m += 1
                    n += 1
                # if plagiariasm, check it against longest previous match
                if len(match) >= 5:
                    if not longest_match:
                        longest_match = match
                    else:
                        if len(match) > len(longest_match):
                            longest_match = match
    if longest_match:
        return " ".join(longest_match)
    else:
        return longest_match
