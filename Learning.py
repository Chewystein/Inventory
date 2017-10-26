import os


class Node():
    def __init__(self):
        self.tag = ""
        self.location = ""

    def __init__(self, tag, location):
        self.tag = tag
        self.location = location


def main():
    # Initialize the two arrays
    badTagList = []
    missingTagList = []
    # Check through all of the log files for the day
    # Wherever the audits go change this variable to that
    path = "/root/new/Audits/"
    for temp in os.listdir(path):
        file = open(path + temp, "r")
        if temp.endswith(".txt"):
            # Read through the files to find the correct lines
            lines = file.readlines()
            for line in lines:
                # Get the locations and values of stuff using substrings
                if "location" in line:
                    line = str(line[line.find(":"):])
                    location = line[line.find('"') + 1:line.rfind('"')]
                # Tags looked like they were seperated by a comma
                elif "bad" in line:
                    if '""' in line:
                        continue
                    line = str(line[line.find(":") + 1:])
                    badTags = str(line[line.find('"') + 1:line.rfind('"')])
                    while badTags.find(",") is not -1:
                        badTag = badTags[0:badTags.find(",")]
                        myNode = Node(badTag, location)
                        badTags = badTags[badTags.find(",") + 1:]
                        badTagList.append(myNode)

                elif "missing" in line:
                    if '""' in line:
                        continue
                    line = str(line[line.find(':') + 1:])
                    missingTags = str(line[line.find('"') + 1:line.rfind('"')])
                    while missingTags.find(",") is not -1:
                        missingTag = missingTags[0:missingTags.find(",")]
                        myNode = Node(missingTag, location)
                        missingTags = missingTags[missingTags.find(",") + 1:]
                        missingTagList.append(myNode)

    # Go through the lists and see if any tags match up
    for i in range(len(badTagList) - 1):
        badTag = badTagList[i]
        for j in range(len(missingTagList) - 1):
            missingTag = missingTagList[j]
            if missingTag.tag == badTag.tag:
                print("Tag {0} can be found at location {1}".format(missingTag.tag, missingTag.location))


main()
