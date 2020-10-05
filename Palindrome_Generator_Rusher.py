
def palindrome_generator():

    dna = input("\nPlease enter a DNA sequence: ")

    dna_list = [] # creating emtpy array/list
    
    for i in dna:
        dna_list.append(i) # converting the dna input string into the array/list dna_list
        
    l = len(dna_list) # determining the length of the sequence and assigning it to a variable

    
    mirror1 = dna_list[::-1] # creating a mirrored array of the input sequence and popping off the last element (which would be a repeat of the 1st element of the original strand)
    mirror1.pop()

    i = 0 # recursive value to be used in the following for loop
    for base in dna_list: # this loop will determine if there are multiple repeats of the first nucleotide directly following the first nucleotide (i.e. AAAAAAT), and then remove those repeats from the mirrored array. The end result will be a mirrored array without the repeats (those would not be necessary for creating the shortest palindrome)
        if dna_list[i] == dna_list[i+1]:
            mirror1.pop()
            i = i + 1
        else:
            break

    mirror_array = mirror1 + dna_list # joining the mirrored array with the original input sequence array
    mirror_string = "" 
    for base in mirror_array: # this loop will create a string from the combined arrays
        mirror_string += base 
    
    if dna_list == dna_list[::-1]: #determines if the input sequence is already a palindrome
        print("\nThe sequence you have entered is already a palindrome!\n")

    ## Both of the following 'elif' statements will start in the middle of the array and work their way out to create a palindrome

    elif l%2 == 1: # if statement determines if the sequence length is an odd number (will have single, centerd nucleotide), the following code will iterate through the sequence, ignoring the center nucleotide, and starting by comparing the values to the left and right of the center.
        
        i = 1 # recursive value used in for loop below

        middle = [dna_list[round(l/2)-1]] # sequence of an odd numbered length will have a center nucleotide, this will be put that value into it's own array - I will use the round(len()) method so I can use this value as an index when iterating through the array
        left_side =[] # creating an empty array for the left side and right side to store values as we iterate through the dna_list
        right_side =[] # see comment above

        try: # try block which will catch any index errors
            for base in range(0,(round(l/2))): #this loop will iterate across the dna_list equal to half of the length of the list
            
                if dna_list[round(l/2)-1-i] == dna_list[round(l/2)-1+i]: # evaluating the elements at the postitions center - 1 and the center + 1 to see if they're the same. If they are then that base is added to the left and right arrays
                    left_side.insert(0,(dna_list[round(l/2)-1-i])) # .insert() will add elements to the beginning of the array, so the last element to be added to the left side will be at index 0 (the '- i' at the end indicates this will elvaluate to the left of the middle value)
                    right_side.append(dna_list[round(l/2)-1+i]) # .append() can be used for the right side [], since the elements will read left to right, they will just need to be added to the end of the array each time (the '+ i' at the end indicates this will elvaluate to the right of the middle value)
                    i = i + 1
                
                elif dna_list[round((l/2))-1-i] != dna_list[round((l/2))-1+i]: # if they are not equal, then the base on the left is added to both arrays AND the base on the right is added to both arrays. So 2 additions to each array
                    left_side.insert(0,(dna_list[round(l/2)-1-i])) # adds the evaluated element (which is at a '-i' position from the middle) to the left side AND the right side
                    right_side.append(dna_list[round(l/2)-1-i]) # see comment above

                    left_side.insert(0,(dna_list[round(l/2)-1+i])) # adds the evaluated element (which is at a '+i' position from the middle) to the left side AND the right side
                    right_side.append(dna_list[round(l/2)-1+i]) # see comment above
                    i = i + 1

        except IndexError:
            print("")

        palindrome_array = left_side+middle+right_side # concatenating the left_side[], middle[], and right_side[] into one array
        palindrome_string = "" # creating an empty string to store the array as a string
        
        for base in palindrome_array: # this for loop turn the palindrome_array above, into a string
            palindrome_string += base

        if len(mirror_string) <= len(palindrome_array) and len(mirror_string) > len(dna): # determines if the length of the palindrome array (that was just created) is longer than the mirror palindrome (generated at the beginning of the program). AND that the mirrored array isn't shorter than the original sequence. Whichever one is the shortest length will be printed below.
            print(f"\nThe palindrome with the fewest inserted bases for the given sequence is:\n\n{mirror_string}\n\nThe length of the original input sequence was: {len(dna)}\nThe length of the new palindrome is: {len(mirror_string)}\n")

        else:
            print(f"\nThe palindrome with the fewest inserted bases for the given sequence is:\n\n{palindrome_string}\n\nThe length of the original input sequence was: {len(dna)}\nThe length of the new palindrome is: {len(palindrome_string)}\n")

    elif l%2 == 0: # if statement determines if the sequence length is an even number (two nucleotides will make up the center)
        
        
        i = 0 # used in for loop
        # no middle array is created this time (no single nucleotide will be at the center)
        left_side =[]
        right_side =[]

        try: # try block which will catch any index errors
            for base in range(0,int(l/2)): # used int() because len()/2 should always be an integer for an even numbered array

                if dna_list[round(l/2)-1-i] == dna_list[round(l/2)+i]: # same process as in the 'elif' statement above, except the right side index position does not contain a '-1'. This because the len()/2 will be the index value of the right center value (assuming that 2 nucleotides now make up the center of an even numbered array)
                    left_side.insert(0,(dna_list[round(l/2)-1-i]))
                    right_side.append(dna_list[round(l/2)+i])
                    i = i + 1
                
                elif dna_list[round(l/2)-1-i] != dna_list[round(l/2)+i]: # same process, with the exception mentioned in the previous comment above
                    left_side.insert(0,(dna_list[round(l/2)-1-i]))
                    right_side.append((dna_list[round(l/2)-1-i]))

                    left_side.insert(0,dna_list[round(l/2)+i])
                    right_side.append(dna_list[round(l/2)+i])
                    i = i + 1

        except IndexError:
            print("")        

        palindrome_array = left_side+right_side # same process as the first 'elif' statement, except there is no middle[] being concatenated
        palindrome_string = "" # same process as the first 'elif' statement

        for base in palindrome_array: # same process as the first 'elif' statement
            palindrome_string += base

        if len(mirror_string) <= len(palindrome_array) and len(mirror_string) > len(dna): # same process as the first 'elif' statement
            print(f"\nThe palindrome with the fewest inserted bases for the given sequence is:\n\n{mirror_string}\n\nThe length of the original input sequence was: {len(dna)}\nThe length of the new palindrome is: {len(mirror_string)}\n")

        else:
            print(f"\nThe palindrome with the fewest inserted bases for the given sequence is:\n\n{palindrome_string}\n\nThe length of the original input sequence was: {len(dna)}\nThe length of the new palindrome is: {len(palindrome_string)}\n")

palindrome_generator()


