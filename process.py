#The function open let us read througth the file and convert all to string file object
# then assign the string into the variable log_file
log_file = open("um-server-01.txt")

#The sales_reports function is defined in line 6 and it going to take parameter
def sales_reports(log_file):
# The loop will iterate on each line in the file
    for line in log_file:
#Assign the value to the variable line after the rstrip function remove any white at end of the line 
        line = line.rstrip()
        #slice from the line list the elements from index zero til index two
        day = line[0:3]
        # if the condition met print the whole line
        if day == "Tue":
            print(line)

#invoke the function sales reports argument log_file
sales_reports(log_file)
