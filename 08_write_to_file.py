import re
#History data
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
#assumed valid data input for file name
has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter a Filename (leave the extension off):")
    has_error = "no"


    valid = "[A-za-z0-9_]"
    for letter in filename:
        if re.match(valid, letter):
            
            continue
        
        elif letter == " ":
            problem = ("No spaces allowed.")
       
        else:
            problem = ("No {}'s allowed.".format(letter))

            has_error = "yes"

    if filename == "":
        problem= "Please enter a filename."
        has_error = "yes"

    if has_error == "yes":
        print("Invalid filename - {}".format(problem))
    else:
        print("Done.")

#text file
filename = filename + ".txt"
#make the file
f = open(filename, "w+")
#add new line for each item
for item in data:
    f.write(item + "\n")
#close the file
f.close

