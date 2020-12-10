import java.util.HashSet;
import java.util.Set;

class Program3 {

    private static final String FIRST_WIRE = "R990,U475,L435,D978,L801,D835,L377,D836,L157,D84,R329,D342,R931,D522,L724,U891,L508,U274,L146,U844,R686,D441,R192,U992,L781,D119,R436,D286,R787,D85,L801,U417,R619,D710,R42,U261,R296,U697,L354,D843,R613,U880,R789,D134,R636,D738,L939,D459,L338,D905,R811,D950,L44,U992,R845,U771,L563,D76,L69,U839,L57,D311,L615,D931,L437,D201,L879,D1,R978,U415,R548,D398,L560,D112,L894,D668,L708,D104,R622,D768,R901,D746,L793,D26,R357,U216,L216,D33,L653,U782,R989,U678,L7,D649,R860,D281,L988,U362,L525,U652,R620,D376,L983,U759,R828,D669,L297,U207,R68,U77,R255,U269,L661,U310,L309,D490,L55,U471,R260,D912,R691,D62,L63,D581,L289,D366,L862,D360,L485,U946,R937,D470,L792,D614,R936,D963,R611,D151,R908,D195,R615,U768,L166,D314,R640,U47,L161,U872,R50,U694,L917,D149,L92,U244,L337,U479,R755,U746,L196,D759,L936,U61,L744,D774,R53,U439,L185,D504,R769,D696,L285,D396,R791,U21,L35,D877,L9,U398,R447,U101,R590,U862,L351,D210,L935,U938,R131,U758,R99,U192,L20,U142,L946,D981,R998,U214,R174,U710,L719,D879,L411,U839,L381,U924,L221,D397,R380,U715,R139,D367,R253,D973,L9,U624,L426,D885,R200,U940,R214,D75,R717,D2,R578,U161,R421,U326,L561,U311,L701,U259,R836,D920,R35,D432,R610,D63,R664,D39,L119,D47,L605,D228,L364,D14,L226,D365,R796,D233,R476,U145,L926,D907,R681,U267,R844,U735,L948,U344,L629,U31,L383,U694,L666,U158,R841,D27,L150,D950,L335,U275,L184,D157,R504,D602,R605,D185,L215,D420,R700,U809,L139,D937,L248,U693,L56,U92,L914,U743,R445,U417,L504,U23,R332,U865,R747,D553,R595,U845,R693,U915,R81";
    private static final String SECOND_WIRE = "L1004,U406,L974,D745,R504,D705,R430,D726,R839,D550,L913,D584,R109,U148,L866,U664,R341,U449,L626,D492,R716,U596,L977,D987,L47,U612,L478,U928,L66,D752,R665,U415,R543,U887,R315,D866,R227,D615,R478,U180,R255,D316,L955,U657,R752,U561,R786,U7,R918,D755,R506,U131,L875,D849,R823,D755,L604,U944,R186,D326,L172,U993,L259,D765,R427,D193,R663,U470,L294,D437,R645,U10,L926,D814,L536,D598,R886,D290,L226,U156,R754,D105,L604,D136,L883,U87,R839,D807,R724,U184,L746,D79,R474,U186,R727,U9,L69,U565,R459,D852,R61,U370,L890,D439,L431,U846,R460,U358,R51,D407,R55,U179,L385,D652,R193,D52,L569,U980,L185,U813,R636,D275,L585,U590,R215,U947,R851,D127,L249,U954,L884,D235,R3,U735,R994,D883,L386,D506,L963,D751,L989,U733,L221,U890,L711,D32,L74,U437,L700,D977,L49,U478,R438,D27,R945,D670,L230,U863,L616,U461,R267,D25,L646,D681,R426,D918,L791,U712,L730,U715,L67,U359,R915,D524,L722,U374,L582,U529,L802,D865,L596,D5,R323,U235,R405,D62,R304,U996,L939,U420,L62,D299,R802,D803,L376,U430,L810,D334,L67,U395,L818,U953,L817,D411,L225,U383,R247,D234,L430,U315,L418,U254,L964,D372,R979,D301,R577,U440,R924,D220,L121,D785,L609,U20,R861,U288,R388,D410,L278,D748,L800,U755,L919,D985,L785,U676,R916,D528,L507,D469,L582,D8,L900,U512,L764,D124,L10,U567,L379,D231,R841,D244,R479,U145,L769,D845,R651,U712,L920,U791,R95,D958,L608,D755,R967,U855,R563,D921,L37,U699,L944,U718,R959,D195,L922,U726,R378,U258,R340,D62,L555,D135,L690,U269,L273,D851,L60,D851,R1,D315,R117,D855,L275,D288,R25,U503,R569,D596,L823,U687,L450";

    /**
     * Main method.
     * 
     * @param args
     * @throws Exception
     */
    public static void main(final String[] args) {
        System.out.println("Start program.");

        String firstWireArray[] = FIRST_WIRE.split(",");
        String secondWireArray[] = SECOND_WIRE.split(",");

        // walk the path
        Set<String> firstStepList = walk(firstWireArray);
        Set<String> secondStepList = walk(secondWireArray);

        // calculate intersections
        Set<String> intersections = new HashSet<String>(firstStepList);
        intersections.retainAll(secondStepList);

        int closestIntersection = 0;

        // get the closest intersection by comparing the distances 
        for (String intersection : intersections) {
            String[] resultSplit = intersection.split("\\.");
            int posX = Math.abs(Integer.parseInt(resultSplit[0]));
            int posY = Math.abs(Integer.parseInt(resultSplit[1]));
            int distance = posX + posY;

            //System.out.println(intersection);
            //System.out.println("distance: " + distance);

            if (closestIntersection == 0 || distance < closestIntersection) {
                closestIntersection = distance;
                System.out.println("closestIntersection: " + closestIntersection);
            }
        }
        System.out.println("End program.");
    }

    public static Set<String> walk(String strArray[]) {
        int posX = 0;
        int posY = 0;

        Set<String> stepList = new HashSet<String>();

        for (String instruction : strArray) {
            String direction = instruction.substring(0, 1);
            int steps = Integer.parseInt(instruction.substring(1, instruction.length()));

            //System.out.println(String.format("Direction: %s - Steps:  %s", direction, steps));

            if ("R".equals(direction)) {
                for (int j = 0; j < steps; j++) {
                    posX++;
                    String step = String.format("%s.%s", posX,posY);
                    stepList.add(step);
                    //System.out.println(step);
                }

            } else if ("L".equals(direction)) {
                for (int j = 0; j < steps; j++) {
                    posX--;
                    String step = String.format("%s.%s", posX,posY);
                    stepList.add(step);
                    //System.out.println(step);
                }
            } else if ("U".equals(direction)) {
                for (int j = 0; j < steps; j++) {
                    posY++;
                    String step = String.format("%s.%s", posX,posY);
                    stepList.add(step);
                    //System.out.println(step);
                }
            } else if ("D".equals(direction)) {
                for (int j = 0; j < steps; j++) {
                    posY--;
                    String step = String.format("%s.%s", posX,posY);
                    stepList.add(step);
                    //System.out.println(step);
                }
            }
        }
        return stepList;
    }

}