import  java.time.*;

public class Program2 {
    
    private static int[] expenseReport = {1933,1963,1924,1832,1949,1826,1681,1548,1881,1973,1558,1979,1803,1975,1867,1934,1986,1220,1878,1985,2006,1535,1522,1884,1380,1922,1905,1582,1456,1877,1959,1953,634,1875,366,1968,1887,1848,1779,1894,1606,1429,1900,1309,2007,1944,1901,1559,1484,1996,1837,1892,1989,1684,1952,1990,1974,1890,1883,1993,1592,1889,1735,1577,1568,1957,1980,1537,1992,1950,1836,1397,1660,2010,1627,1991,1888,107,1977,1898,1532,1726,1899,1960,1962,2000,1903,1937,1931,1895,1868,1600,1926,1946,1964,1956,1915,1506,1580,1984,1870,2008,1885,1503,1927,841,1997,2002,1869,1874,1906,1911,508,1718,1961,1909,1914,1940,1879,1965,1929,1932,1579,1902,1783,1983,166,1972,2003,2005,1918,1893,1427,1945,1982,1847,1425,1941,1958,1842,1928,1840,1789,1654,1665,1387,1908,1891,1873,1839,1943,1616,1490,144,1981,1988,1853,1994,42,1954,1762,1792,1896,1907,1976,1886,1971,1998,1912,1967,1857,1951,1925,1921,1518,1593,2004,1999,1571,1923,463,1897,1861,1467,1920,1504,2009,1942,1995,1947,1872,1969,1910,1955,1939,1966,1687,1827,675,1520};
    private static int sumValue = 2020;
    private static boolean exitWhenFound = true;

    /**
     * Main method.
     * @param args
     */
    public static void main(String[] args) {
        Instant start = Instant.now();
        System.out.println("Start Program2.");
        int numberOfComparisons = 0;

        for (int k = 0; k < expenseReport.length; k++) {
            for (int i = 0; i < expenseReport.length; i++) {
                for (int j = 0; j < expenseReport.length; j++) {
                    // only compare the current value with all OTHER values in the array
                    if (k != i && k != j && i != j) {
                        numberOfComparisons++;

                        int valueZero = expenseReport[k];
                        int valueOne = expenseReport[i];
                        int valueTwo = expenseReport[j];

                        // compare values
                        if ((valueZero + valueOne + valueTwo) == sumValue) {
                             // time passes  
                            Instant end = Instant.now();
                            Duration timeElapsed = Duration.between(start, end);

                            System.out.println(String.format("Solution: %s * %s * %s == %s", valueZero, valueOne, valueTwo, (valueZero * valueOne * valueTwo)));
                            
                            if (exitWhenFound) {
                                System.out.println(String.format("numberOfComparisons: %s", numberOfComparisons));
                                System.out.println(String.format("timeElapsed: %s", timeElapsed));
                                System.exit(0);
                            }
                        }                  
                    }
                }
            }
        }
        System.out.println(String.format("numberOfComparisons: %s", numberOfComparisons));
    }
}
