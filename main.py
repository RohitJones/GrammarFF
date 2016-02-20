from collections import OrderedDict

first_dict = OrderedDict()
follow_dict = OrderedDict()

def main():
    inputfile = open("input2.txt", 'r')
    grammar = []                                                # store the various rules of the grammar
    Non_Terminals = []                                          # store the non terminals of the grammar
    outputfile = open("output.txt", 'w')

    for line in inputfile:                                      # read the input file containing the grammar
        outputfile.write(line)                                  # write the grammer rules to the output file
        grammar.append(line.strip().split("\n"))                # store each line of input into grammar

    inputfile.close()

#--------------------------------------------calculation of first-------------------------------------------------------

    flag = 0                                                    # to check if 1st iteration of for or not
    for rule in grammar:                                        # read every line of grammar in rule
        if rule[0][0] not in Non_Terminals:                     # Store only unique Non terminals
            Non_Terminals.append(rule[0][0])
            first_dict[rule[0][0]] = []                         # initialize dictionary key to corresponding non terminal and
                                                                # set the value of the key to a blank list
            if flag == 0:
                follow_dict[rule[0][0]] = "$"                   # the follow of the starting production contains '$'
                flag = 1                                        # indicate that the 1st iteration of loop is done
            else:
                follow_dict[rule[0][0]] = []                    # initialize dictionary key to corresponding non terminal and
                                                                # set the value of the key to a blank list

        if rule[0][3].islower():                                # check to see if first character after '->' is a terminal if yes
            first_dict[rule[0][0]].append(rule[0][3])           # add it to the first of Non terminal

    for rule in grammar:                                        # read every line of grammar in rule
        if rule[0][3].isupper():                                # check to see if first character after '->' is a non-terminal if
            first_dict[rule[0][0]] += first_dict[rule[0][3]]    # yes, add the first of the non terminal to first list

    for each in first_dict:                                     # read every non terminal of grammar in rule
        first_dict[each] = set(first_dict[each])                # remove duplicate occurrences of the terminals in the first

#---------------------------------------------calculation of follow-----------------------------------------------------

    for temp_string in grammar:                                 # traverse through all the grammar rules
        temp = list(temp_string[0])                             # convert each string(grammar rule) into a list
        for i in range(3, len(temp)):                           # traverse character wise through the grammar rule via temp list
            if temp[i] in Non_Terminals:                        # check if character temp[i] is a Non terminal or not
                if (i + 1) >= len(temp):                        # check if the Non terminal is in the last position of temp list
                    follow_dict[temp[i]] += follow_dict[temp[0]]    # add follow of left side non terminal to the follow of temp[i]
                else:
                    if temp[i+1] in Non_Terminals:              # check if the next char after temp[i] is a non terminal
                        follow_dict[temp[i]] += first_dict[temp[i+1]]   # add first of the non termial to the follow of temp[i]
                    else:
                        follow_dict[temp[i]] += temp[i+1]       # the char after temp[i] is a terminal and is added to its follow

    for each in follow_dict:                                    # remove duplicate entries in the first list
        follow_dict[each] = set(follow_dict[each])

    outputfile.write("\n\n")                                    # output formatting

    for each in first_dict:                                     # write the dictionary
        temp = "first(" + each + ") = {"                        # to an output file
                                                                # according to the
        for item in first_dict[each]:                           # format
            temp = temp + item + ", "                           # first(Non-Terminal) = { Terminals }
        temp = temp.rstrip(', ')                                #
        temp += "}\n"                                           #
        outputfile.write(temp)                                  #

    outputfile.write("\n")                                      # output formatting

    for each in follow_dict:                                    # write the dictionary
        temp = "follow(" + each + ") = {"                       # to an output file
                                                                # according to the
        for item in follow_dict[each]:                          # format
            temp = temp + item + ", "                           # follow(Non-Terminal) = { Terminals }
        temp = temp.rstrip(', ')                                #
        temp += "}\n"                                           #
        outputfile.write(temp)                                  #

if __name__ == "__main__":
    main()