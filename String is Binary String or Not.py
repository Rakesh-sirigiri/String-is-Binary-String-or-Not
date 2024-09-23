import re
sampleInput = "1001010"
c = re.compile('[^01]')
if(len(c.findall(sampleInput))):
    print("No")
else:
    print("Yes")
