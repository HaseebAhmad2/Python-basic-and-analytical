import csv
import sys
from sys import argv


def main():

    # Check for command-line usage
    if (len(argv) != 3):
        print("Usage: python dna.py data.csv sequence.txt")
        return

    Data_file = []
    #  Read database file into a variable
    with open(argv[1], 'r')as file:
        CSV = csv.reader(file)
        for line in CSV:
            Data_file.append(line)

    # TODO: Read DNA sequence file into a variable
    with open(argv[2], 'r')as file:
        TXT = file.read()

    # TODO: Find longest match of each STR in DNA sequence
        # initializing the empty string
    longest_STR = []
    # giving values of list to another list
    STR_count = Data_file[0][1:]
    # loop for printing the elements in STR_count
    for i in STR_count:
        longest_count = longest_match(TXT, i)
        longest_STR.append(str(longest_count))
    # print(longest_STR)
    # print(Data_file)

    # TODO: Check database for matching profiles
    # initalizing the flag as false
    flag = False
    # Comparing the values of one list with another list
    for i in range(len(Data_file)):
        # checking longest STR with Data file .
        if (longest_STR == Data_file[i][1:]):
            # printing the name of person whose STR is matched
            print(Data_file[i][0])
            flag = True
            break
    if flag == False:
        print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
