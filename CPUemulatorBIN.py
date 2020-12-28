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
        self.instruction=content[:8]
        self.parameter=content[8:]

program=[]
memory=[0]*(2**20)
registers={
    "00000000":0, #Accumulator
    "00000001":0, #Instruction pointer
    "00000010":0, #Program offset
    "00000011":0, #Memory offset
    "00000100":1  #Condition control
    }

inp=input()
s=""
for j in inp:
    s+=j
    if len(s) == 16:
        program+=[Instruction(s)]
        s=""

while registers["00000001"]+registers["00000010"]<len(program):
    current=program[registers["00000001"]+registers["00000010"]]
    mo=registers["00000011"]
    if registers["00000100"]:
        if(current.instruction=="00000101"):     #VAL
            registers["00000000"]=int(current.parameter,2)
        elif(current.instruction=="00000010"):   #SET
            memory[mo+int(current.parameter,2)]=registers["00000000"]
        elif(current.instruction=="00000001"):   #GET
            registers["00000000"]=memory[mo+int(current.parameter,2)]
        elif(current.instruction=="00000011"):   #ADD
            registers["00000000"]+=memory[mo+int(current.parameter,2)]
        elif(current.instruction=="00000100"):   #SUB
            registers["00000000"]-=memory[mo+int(current.parameter,2)]
        elif(current.instruction=="00000110"):   #RGG
            registers["00000000"]=registers[current.parameter]
        elif(current.instruction=="00000111"):   #RGS
            registers[current.parameter]=registers["00000000"]
    if(current.instruction=="00001000"):         #RST
        registers["00000100"]=1
    registers["00000001"]+=1
