import java.util.Arrays;

/**
 * 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
 * 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
 * 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
 * 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
 */

class Program {

    private static int[] seqList = {1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,1,31,5,35,1,9,35,39,2,13,39,43,1,43,10,47,1,47,13,51,2,10,51,55,1,55,5,59,1,59,5,63,1,63,13,67,1,13,67,71,1,71,10,75,1,6,75,79,1,6,79,83,2,10,83,87,1,87,5,91,1,5,91,95,2,95,10,99,1,9,99,103,1,103,13,107,2,10,107,111,2,13,111,115,1,6,115,119,1,119,10,123,2,9,123,127,2,127,9,131,1,131,10,135,1,135,2,139,1,10,139,0,99,2,0,14,0};
    //private static int[] seqList = {1,0,0,0,99};
    //private static int[] seqList = {2,4,4,5,99,0};
    //private static int[] seqList = {2,4,4,5,99,0};
    //private static int[] seqList = {1,1,1,4,99,5,6,0,99};

    /**
     * Main method.
     * @param args
     */
    public static void main(final String[] args) {
        System.out.println("Start program.");
        seqList[1] = 12;
        seqList[2] = 2;

        System.out.println("Start seqList: " + Arrays.toString(seqList));

        for (int i = 0; i < seqList.length; i = i+4) {          
            // exit;
            if (seqList[i] == 99) {
                break;
            // add
            } else if (seqList[i] == 1) {
                seqList[seqList[i+3]] = seqList[seqList[i+1]] + seqList[seqList[i+2]];
            // multiply
            } else if (seqList[i] == 2) {
                seqList[seqList[i+3]] = seqList[seqList[i+1]] * seqList[seqList[i+2]];
            }
        }

        System.out.println("End seqList: " + Arrays.toString(seqList));
    }



}