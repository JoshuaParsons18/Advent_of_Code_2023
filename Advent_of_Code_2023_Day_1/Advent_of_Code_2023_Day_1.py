# Pseudo code breakdown

# Load the file
# Read each line storing each line as a set of characters in a dict = {line1: ['a','b','c','1','f',2'], line2: ['g','h','3','i','j',1']}
# Determine the character count 
# Store the position of each integer 
    # if 2 integers use both
    # else if 3 determine first and last integer in set
    # else if only 1 integer repeat the same integer to make a set of 2
# Return a list of the respective integer value for each line
# Sum this value

import os
from sys import call_tracing

class AOC:
    def __init__(self):
        Calibration_Vals = self.loadFile('Calibration_Vals.txt')    # Load File as dict
        numberDict = self.parseDict(Calibration_Vals)               # Parse dict
        codeList = self.getCode(numberDict)                         # Get CodeList
        
        print(codeList)

        code = sum(codeList)
        
        print(code)

    def loadFile(self, path):
        try: 
            lineNum = 0
            dictVals = {}

            with open(path, 'r') as file:
                content = file.readline().strip()
                while content:
                    dictVals[lineNum] = content
                    lineNum+=1

                    content = file.readline().strip()

        except FileNotFoundError: 
            print("File not found")

        return dictVals

    def parseDict(self, sample):
        updatedDict = {}
        i = 0

        # Turn the dict into a list of only value
        valueList = list(sample.values())                            # Returns a list of values from the passed dict

        # Now we need to split each valueSet into a list of characters
        for valueSet in range(0, len(valueList)):
            # Take the valueSet in the range of 0 - 999 (1000) and convert to a list of chars
            charSet = [*sample[valueSet]]

            for index in range(0, len(charSet)):     
                
                if charSet[index].isalpha():
                    pass
                else:
                    updatedDict.setdefault(i, []).append(charSet[index])

            i+=1 # Updates key of dict

        return updatedDict

    def getCode(self, numberDict):
        # Loop through each key in the dictionary
        codeList = []
        valuePos = 0
            
        for key in range(0, len(numberDict)):   # Loop through passed dict
            valueList = numberDict[key]         # convert a given dict key to a list of value
            v0 = str(valueList[0])              # Get first value as string
            v1 = str(valueList[-1])                  # Get last value as string
            v = int(v0 + v1)
            codeList.append(v)

        return codeList

if __name__ == '__main__':
    aoc = AOC()
