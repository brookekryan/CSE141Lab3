/**
 * Created by brookeryan on 11/12/16.
 */
public class Lab3 {
    private static final int A_B_TYPE_ARGS = 3;
    private static final int A_B_TYPE_BITS = 3;
    private static final int C_TYPE_ARGS = 2;
    private static final int C_TYPE_BITS = 8;
    private static final int BASE_10 = 10;


    public static void main (String[] args) throws Exception {
        String instruction = "ld 32";
        System.out.println(convertInstruction(instruction.split(" ")));
        String instruction2 = "add %r0, %r1";
        System.out.println(convertInstruction(instruction2.split(" ")));
        String error = "imsk 7";
        System.out.println(convertInstruction(error.split(" ")));
    }

    /*
     * Splits the lines of the files by newline
     * Writes to output file
     */
    public static void convertFile() {
        // Split the file name into strings
        //
        // convertInstruction();
    }

    /*
     * Converts one instruction to binary
     */
    private static String convertInstruction(String[] instruction) throws Exception {
        String operation = instruction[0];
        String output = "";

        // Separate them by their opcode value
        // Call the appropriate
        switch(operation) {
            //A-type and B-type instructions:
            case "imsk":
                output = "0";
                break;
            case "add":
            case "bs":
            case "abs":
                output = "001";
                break;
            case "addi":
            case "bns":
            case "slt":
            case "set":
                output = "010";
                break;
            case "sub":
            case "xor":
            case "slti":
            case "str":
                output = "011";
                break;
            case "and":
            case "ba":
                output = "100";
                break;
            case "andi":
            case "bono":
                output = "101";
                break;
            case "sl":
            case "bevn":
                output = "110";
                break;
            case "sr":
            case "sd":
                output = "111";
                break;
            //C-type instructions:
            case "ld":
            case "st":
                output = "1";
                break;
            case "":
                return "";
            default:
                System.err.println("Invalid input on line " + instruction[0]);
                break;
        }
        return output = output + setRegImm(instruction);       // Converts other arguments to binary
    }

    /*
     * Convert registers and immediate values to binary string
     */
    private static String setRegImm(String[] instruction) throws Exception {
        int length = instruction.length;
        int bits = setBits(length);
        int immediate;
        String outputString = "";
        String s = "";

        // Converts arguments from Reg or Imm string to a binary string
        for (int i=1; i<length; i++) {
            // Replace anything that's not an integer
            s = instruction[i].replaceAll("[^\\d.]", "");

            //Converts from string to decimal to binary
            immediate = Integer.parseInt(s, BASE_10);
            s = Integer.toBinaryString(immediate);

            // Ensures correct number of bits
            while (s.length()<bits) {
                s = "0" + s;
            }

            outputString = outputString + s;
        }

        return outputString;
    }

    /*
     * Sets appropriate number of bits
     */
    private static int setBits(int length) throws Exception {
        if (length == A_B_TYPE_ARGS)
            return A_B_TYPE_BITS;
        else if (length == C_TYPE_ARGS)
            return C_TYPE_BITS;
        else
            throw new Exception("Error, invalid instruction format");
    }

}

