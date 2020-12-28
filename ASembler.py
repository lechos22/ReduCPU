#
#           ReduCPU
#
# This proccessor has super llama powers
#

class Instruction:
    content=""
    instruction=""
    parameter=""
    def __init__(self,content):
        self.content=content
        if len(self.content.split())>0:
            self.instruction=content.split()[0]
        else:
            self.instruction="0"
        if len(self.content.split())>1:
            self.parameter=content.split()[1]
        else:
            self.parameter="0"
        if self.parameter in ["RA","IP","PO","MO","CC"]:
            self.parameter={
                "RA":"00",
                "IP":"01",
                "PO":"02",
                "MO":"03",
                "CC":"04"
                }[self.parameter]

program=[]

i=input()
while i != "EOF":
    program+=[Instruction(i)]
    i=input()

def binarize(a):
    s=""
    for i in a:
        s+={
            "0":"0000",
            "1":"0001",
            "2":"0010",
            "3":"0011",
            "4":"0100",
            "5":"0101",
            "6":"0110",
            "7":"0111",
            "8":"1000",
            "9":"1001",
            "A":"1010",
            "B":"1011",
            "C":"1100",
            "D":"1101",
            "E":"1110",
            "F":"1111",
            }[i]
    return s
def hexize(a):
    a=int(a)
    s=""
    while a!=0:
        s=str(hex(a%16))[2:].upper()+s
        a//=16
    while len(s)<2:
        s="0"+s
    return s

output=""

i=0
while i<len(program):
    current=program[i]
    if(current.instruction=="VAL"):
        output+="05"
    if(current.instruction=="ZER"):
        output+="00"
    if(current.instruction=="SET"):
        output+="02"
    if(current.instruction=="GET"):
        output+="01"
    if(current.instruction=="ADD"):
        output+="03"
    if(current.instruction=="SUB"):
        output+="04"
    if(current.instruction=="RGG"):
        output+="06"
    if(current.instruction=="RGS"):
        output+="07"
    if(current.instruction=="RST"):
        output+="08"
    output+=hexize(current.parameter)
    i+=1

print(output)
print(binarize(output))
