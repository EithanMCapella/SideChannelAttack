import csv
import sys

#Idea Given a Decimal Number and the delays
#Find the bits that are active for the decimal number: 
#Use a bitshift right operation grab the key and shift it the 6 times to find which bit is active
#Once we find the active bit, add the appropiate delay to its total delay
#This checking is done with a bitwise AND (&) operation with 1, it checks least significant bit of the result of the previous shift

#Example: Decimal 3 Binary is 000011 
#key: 3 i: 0 binary: 1
#key: 3 i: 1 binary: 1
#key: 3 i: 2 binary: 0
#key: 3 i: 3 binary: 0
#key: 3 i: 4 binary: 0
#key: 3 i: 5 binary: 0

#Total delay: 0.30000000000000004 or 0.1 + 0.2
#Why is there a 4 at the end? Probably a Python thing.
#Fix format it in python example:
#number = 0.30000000000000004
#formatNumber = "%.7f" % number 

#class SideChannel:
#def __init__(self, delayFile, targetLatency):

def encryption(bitDelays, key):
    total_delay = 0
    for i in range(6):
        #print("key: " + str(key) + " i: " + str(i) + " binary: " + str((key >> i) & 1))
        if (key >> i) & 1: #bitwise operation to check if a specific bit in the key integer is set
            total_delay += bitDelays[i]
    
    #print("Total delay: " +str(total_delay))
    #print("------New Iteration------")
    #total_delay = float("%.7f" % total_delay)
    return total_delay 

def probePhase(delay_file): 
    bitDelays = []
    with open(delay_file, newline='') as csvfile: #Grab the 6 Encryption bits
        reader = csv.DictReader(csvfile)
        for row in reader:
            bitDelays.append(float(row['Delay'])) #Append all the bits in the following format: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]    
    #print("Encryption Bit Delays: " + str(bitDelays))
    
    keyLatencies = []
    for key in range(64):  #Iterate over the 6 bit keys, 64 entries (0 to 63) 
        cacheLatency = encryption(bitDelays, key) #Pass Known keys to encryption(str, key):  We are passing the 6 bit delays and a decimal number
        keyLatencies.append((key, cacheLatency)) #Store the Key and its delay together
    
    #print("Latency Dictionary" + str(latencies))
    return keyLatencies 

#Take the keyLatencies we found and check which ones are near our target latency
def possibleKeys(latencies, UKLatency):
    validKeys = []
    tolerance = 0.05
    for key, latency in latencies:
        if abs(latency - UKLatency) <= tolerance: #Basically find the difference and see if its near our ballpark, Absolute value ensures the +/- aspect of it.
            validKeys.append(key)
            #print("Latency - UnknownLatency: " + str(abs(latency-UKLatency)))
    return validKeys

    #Had to change format due to moodle errors relating to sys.argv length?

def main(): 
    delay_file = sys.argv[1]
    unknownKeyLatency = float(sys.argv[2])
    
    cacheLatencies = probePhase(delay_file)
    validKeys = possibleKeys(cacheLatencies, unknownKeyLatency)

    print(validKeys)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()