first_dict = {}

def main():
    inputfile = open("input2.txt", 'r')
    grammar = []                                    # store the various rules of the grammar
    Non_Terminals = []                              # store the non terminals of the grammar

    for line in inputfile:                          # read the input file containing the grammar
        grammar.append(line.strip().split("\n"))    # store each line of input into grammar

    inputfile.close()

    for rule in grammar:                            # read every line of grammar in rule
        if rule[0][0] not in Non_Terminals:         # Store only unique Non terminals
            Non_Terminals.append(rule[0][0])
            first_dict[rule[0][0]] = []             # initialize dictionary key to corresponding non terminal and
                                                    # set the value of the key to a blank list
        if rule[0][3].islower():                    # check to see if first character after '->' is a terminal if yes
            first_dict[rule[0][0]].append(rule[0][3])   # add it to the first of Non terminal

    for rule in grammar:                            # read every line of grammar in rule
        if rule[0][3].isupper():                    # check to see if first character after '->' is a non-terminal if
            first_dict[rule[0][0]] += first_dict[rule[0][3]]    # yes, add the first of the non terminal to first list

    for each in first_dict:                         # read every non terminal of grammar in rule
        first_dict[each] = set(first_dict[each])    # remove duplicate occurrences of the terminals in the first

    outputfile = open("output.txt", 'w')

    for each in first_dict:                         # write the dictionary
        temp = "first(" + each + ") = {"            # to an output file
                                                    # according to the
        for item in first_dict[each]:               # format
            temp = temp + item + ", "               # first(Non-Terminal) = { Terminals }
        temp = temp.rstrip(', ')                    #
        temp += "}\n"                               #
        outputfile.write(temp)                      #

if __name__ == "__main__":
    main()
