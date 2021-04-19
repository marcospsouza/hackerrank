import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    
    private static final Scanner scanner = new Scanner(System.in);
    
    static ArrayList<Long> parseInput() {                
        Integer arraySize = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        
        String[] arrayItems = scanner.nextLine().split(" "); 
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        
        scanner.close();
           
        ArrayList<Long> array = new ArrayList();
        for (int i = 0; i < arraySize; i++) {
            array.add(Long.parseLong(arrayItems[i]));
        }
        
        return array;        
    }

    static void writeResult(long result) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        
        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();
    }
    
    // Complete the aVeryBigSum function below.
    static long aVeryBigSum(ArrayList<Long> array) {
        return array.stream().mapToLong(value -> value).sum();
    }

    public static void main(String[] args) throws IOException {   
        ArrayList<Long> array = parseInput();
        long result = aVeryBigSum(array);
        writeResult(result);
    }
}
