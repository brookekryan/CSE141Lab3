import sys
import re
def compile():
    # Initialize Variables
    commentChar = '#'

    codeFilename = str(sys.argv[1])
    # Create a list of instructions from the text file.
    instructions = [line.rstrip('\n') for line in open('code.txt')]
    # Instruction Mask
    imsk = "000"

    branches = {}


    outstring = ""
    # Step 1: Read in all branches
    for index, inst in enumerate(instructions):
        # Remove Comments
        noCommentInstruction = inst.split(commentChar, 1)[0]
        # Split instruction into a list of variables
        iList = re.sub("[^\w]", " ", noCommentInstruction).split()
        if len(iList) == 1:
            branches[iList[0]] = index;
    print branches

    # Step 2: Process instructions line by line
    for inst in instructions:
        # Remove Comments
        noCommentInstruction = inst.split(commentChar, 1)[0]
        # Split instruction into a list of variables
        iList = re.sub("[^\w]", " ", noCommentInstruction).split()
        if len(iList) == 1:
            continue
        #print iList
        # Step 2: Switch case for the command that was read in
        instruction = iList
        opcode = convert_instr_to_bits(instruction[0])
        #imsk 000
        if instruction[0] == "add":      # Type A instruction
        # Step 4: Ensure instruction mask is correct
            if(imsk != "000"):
                imsk = "000"
                outstring += switch_imsk("000")
            itype = "A"
        elif instruction[0] == "addi":   # Type B instruction
            if(imsk != "000"):
                imsk = "000"
                outstring += switch_imsk("000")
            itype = "B"
        elif instruction[0] == "sub":    # Type A instruction
            if(imsk != "000"):
                imsk = "000"
                outstring += switch_imsk("000")
            itype = "A"
        elif instruction[0] == "and":    # Type A instruction
            if(imsk != "000"):
                imsk = "000"
                outstring += switch_imsk("000")
            itype = "A"
        elif instruction[0] == "andi":   # Type B instruction
            if(imsk != "000"):
                imsk = "000"
                outstring += switch_imsk("000")
            itype = "B"
        elif instruction[0] == "sl":     # Type B instruction
            if(imsk != "000"):
                imsk = "000"
                outstring += switch_imsk("000")
            itype = "B"
        elif instruction[0] == "sr":     # Type B instruction
            if(imsk != "000"):
                imsk = "000"
                outstring += switch_imsk("000")
            itype = "B"
        #imsk 001
        elif instruction[0] == "bs":     # Type B instruction
            if(imsk != "001"):
                imsk = "001"
                outstring += switch_imsk("001")
            itype = "B"

        elif instruction[0] == "bns":    # Type B instruction
            if(imsk != "001"):
                imsk = "001"
                outstring += switch_imsk("001")
            itype = "B"
        elif instruction[0] == "xor":    # Type A instruction
            if(imsk != "001"):
                imsk = "001"
                outstring += switch_imsk("001")
            itype = "A"
        elif instruction[0] == "ba":     # Type A instruction
            if(imsk != "001"):
                imsk = "001"
                outstring += switch_imsk("001")
            itype = "A"
        elif instruction[0] == "bono":   # Type B instruction
            if(imsk != "001"):
                imsk = "001"
                outstring += switch_imsk("001")
            itype = "B"
        elif instruction[0] == "bevn":   # Type B instruction
            if(imsk != "001"):
                imsk = "001"
                outstring += switch_imsk("001")
            itype = "B"
        elif instruction[0] == "sd":     # Type B instruction
            if(imsk != "001"):
                imsk = "001"
                outstring += switch_imsk("001")
            itype = "B"
        #imsk 010
        elif instruction[0] == "abs":    # Type A instruction
            if(imsk != "010"):
                imsk = "010"
                outstring += switch_imsk("010")
            itype = "A"
        elif instruction[0] == "slti":   # Type B instruction
            if(imsk != "010"):
                imsk = "010"
                outstring += switch_imsk("010")
            itype = "B"
        #imsk 110
        elif instruction[0] == "ldr":    # Type A instruction
            if(imsk != "110"):
                imsk = "110"
                outstring += switch_imsk("110")
            itype = "A"
        elif instruction[0] == "ld":     # Type C instruction
            if(imsk != "110"):
                imsk = "110"
                outstring += switch_imsk("110")
            itype = "C"
        #imsk 111
        elif instruction[0] == "set":    # Type B instruction
            if(imsk != "111"):
                imsk = "111"
                outstring += switch_imsk("111")
            itype = "B"
        elif instruction[0] == "str":    # Type A instruction
            if(imsk != "111"):
                imsk = "111"
                outstring += switch_imsk("111")
            itype = "A"
        elif instruction[0] == "st":     # Type C instruction
            if(imsk != "111"):
                imsk = "111"
                outstring += switch_imsk("111")
            itype = "C"
        else:
            print "nice lines of assembly noob, do better"
            return
            itype = "D"


        # Step 3: Set register and immediate values
        if itype == "A":
            r1string = convert_reg_to_bits(instruction[1])
            r2string = convert_reg_to_bits(instruction[2])
            outstring += opcode + r1string + r2string + '\n'
        elif itype == "B":
            r1 = convert_reg_to_bits(instruction[1])
            Imm = bin(int(instruction[2])).split('b')[1]
            if len(Imm) > 3:
                print "Immediates are too big ya dingbat"
                return
            outstring += opcode + r1 + "0"*(3-len(Imm)) + Imm + '\n'
        elif itype == "C":
            Imm = bin(int(instruction[1])).split('b')[1]
            outstring += opcode + "0"*(8-len(Imm))+ Imm + '\n'
        else:
            print "Review those instruction types you wanker"
            return
        # Step 5: Concatenate to output string
#    print outstring
    print outstring
def switch_imsk(imsk):
    if imsk == "000":
        bits = "000000000"
    elif imsk == "001":
        bits = "000000001"
    elif imsk == "010":
        bits = "000000010"
    elif imsk == "011":
        bits = "000000011"
    elif imsk == "100":
        bits = "000000100"
    elif imsk == "101":
        bits = "000000101"
    elif imsk == "110":
        bits = "000000110"
    elif imsk == "111":
        bits = "000000111"
    else:
        bits = "error"
    return bits + '\n'

def convert_reg_to_bits(reg):
    if reg == "r0":
        return "000"
    elif reg == "r1":
        return "001"
    elif reg == "r2":
        return "010"
    elif reg == "r3":
        return "011"
    elif reg == "r4":
        return "100"
    elif reg == "r5":
        return "101"
    elif reg == "r6":
        return "110"
    elif reg == "r7":
        return "111"
    else:
        bits = "Nice registers clown"
    return bits

def convert_instr_to_bits(instr):
    instr = str(instr)
    if instr == "add" or instr == "bs" or instr == "halt":
        return "001"
    elif instr == "addi" or instr == "bns" or instr == "tbd" or instr == "set":
        return "010"
    elif instr == "sub" or instr == "xor" or instr == "ldr" or instr == "str" or instr == "abs":
        return "011"
    elif instr == "and" or instr == "ba" or instr == "slt":
        return "100"
    elif instr == "andi" or instr == "bono" or instr == "slti":
        return "101"
    elif instr == "sl" or instr == "bevn":
        return "110"
    elif instr == "sr":
        return "111"
    elif instr == "st":
        return "1"
    elif instr == "ld":
        return "1"
    else:
        print "Check your instructions goofus: " + instr + "??"
        return "error"

compile()

#TODO: Handle Branching: Possibly try to
# Write branch name to string and then parse string for
# The branch name and then replace it with the binary location of PC

# Handle Comments
