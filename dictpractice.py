#Read data from a file. Group flights and droid names
#display the sorted data

flight_log = open("data.txt", 'r')

log={}

#read in each line, separating flight number and droids
for flight in flight_log:
    #read line into the list record
    record = flight.split()
    
    #the 0th element is the flight number
    flight_num = record[0]
    
    #remove 0th element, leaving only droid names on that flight in the list record
    del record[0]
    
    #check if a droid already exists as a key
    #if it does, add the flight to the list of flights associated with the droid
    #if not, assign it to the dictionary
    for droid in record:      
        if droid in log.keys():
            log[droid] = log[droid] + flight_num + " "
            
        else:
            log[droid] = flight_num + " "

#print the droids in alphabetical order
for key in sorted(log):
    print(f"{key}: {log[key]}")
    
#close the data file
flight_log.close()