from collections import OrderedDict

first_dict = OrderedDict()
follow_dict = OrderedDict()
grammar = []                                                # store the various rules of the grammar
Non_Terminals = []                                          # store the non terminals of the grammar


def remove_duplicates(passed_dictionary):
    for each in passed_dictionary:
        passed_dictionary[each] = set(passed_dictionary[each])


def write_dictionary(passed_dictionary, string_to_print, output_file_name):
    with open(output_file_name, "a") as file_ptr:
        file_ptr.write("\n")

        for each in passed_dictionary:                              # write the dictionary
            temp = string_to_print + "(" + each + ") = {"           # to an output file
                                                                    # according to the
            for item in passed_dictionary[each]:                          # format
                temp = temp + item + ", "                           # follow(Non-Terminal) = { Terminals }
            temp = temp.rstrip(', ')                                #
            temp += "}\n"                                           #
            file_ptr.write(temp)                                    #


def get_grammar(input_file_name,output_file_name):
    inputfile = open(input_file_name, 'r')
    outputfile = open(output_file_name, 'w')

    for line in inputfile:                                      # read the input file containing the grammar
        outputfile.write(line)                                  # write the grammer rules to the output file
        grammar.append(line.strip().split("\n"))                # store each line of input into grammar

    inputfile.close()
    outputfile.close()


def main():

    input_file_name = "input2.txt"
    output_file_name = "output.txt"
    get_grammar(input_file_name, output_file_name)

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

    remove_duplicates(first_dict)

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

    remove_duplicates(follow_dict)

    write_dictionary(first_dict, "first", output_file_name)
    write_dictionary(follow_dict, "follow", output_file_name)

    print(first_dict)
    print(follow_dict)

if __name__ == "__main__": main()