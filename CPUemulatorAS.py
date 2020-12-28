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

program=[]
memory=[0]*(2**20)
registers={
    "RA":0, #Accumulator
    "IP":0, #Instruction pointer
    "PO":0, #Program offset
    "MO":0, #Memory offset
    "CC":1  #Condition control
    }

i=input()
while i != "EOF":
    program+=[Instruction(i)]
    i=input()

while registers["IP"]+registers["PO"]<len(program):
    current=program[registers["IP"]+registers["PO"]]
    mo=registers["MO"]
    if registers["CC"]:
        if(current.instruction=="VAL"):
            registers["RA"]=int(current.parameter)
        elif(current.instruction=="SET"):
            memory[mo+int(current.parameter)]=registers["RA"]
        elif(current.instruction=="GET"):
            registers["RA"]=memory[mo+int(current.parameter)]
        elif(current.instruction=="ADD"):
            registers["RA"]+=memory[mo+int(current.parameter)]
        elif(current.instruction=="SUB"):
            registers["RA"]-=memory[mo+int(current.parameter)]
        elif(current.instruction=="RGG"):
            registers["RA"]=registers[current.parameter]
        elif(current.instruction=="RGS"):
            registers[current.parameter]=registers["RA"]
    if(current.instruction=="RST"):
        registers["CC"]=1
    registers["IP"]+=1
