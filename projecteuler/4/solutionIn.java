import java.util.ArrayList;
import java.util.Collections;

//import java.awt.List;
//import java.util.ArrayList;

/* Euler 1 - Joseph Grimer Nov 2017
//A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//
//Find the largest palindrome made from the product of two 3-digit numbers.
// nb 999*999 is a six-digit number and 100*100 is a 5 digit number
// 20/nov/2017 SOLVED - not efficient enough. Could be made 1/4 speed (I reckon) by tracking down where the highest 
 * location to start would be and finding the circle of efficiency
 */


public class main {

	public static void main(String[] args) {
		System.out.println("Euler 4 - The Pallindrone - Joseph Grimer - November 2017\n");

	    System.out.println("functional pallindrome checker: " + checkPallindrome(123545321));

		// initiate vars
		int result = 0;
//		int[] results = null;
		ArrayList<Integer> results = new ArrayList<Integer>(10);
//            count.add(i,0);

//	    outerloop: // label for nested break
	    for(int i=999;i>=100;i--) {
		    for(int j=i;j>=100;j--) { // j=i is more efficient? not sure if reference, which would break it.
		    	int product = i*j;
		        if(checkPallindrome(product)) {
		            System.out.println("\n\nI found a pallindrome: " + (product) + "It is a product of " + i + " and " +j);
		            if (product > result) result = product;
		        }
	            results.add(product); // adding to start or end?
		    }
	    }
	    System.out.println("\nfinal: " + result + " result");
//	    Collections.sort(results);
//	    System.out.println("\n\nStats: " + results);
	    System.out.println("\n\nend of program");
        System.exit(0); // very important! // maybe the JVM won't get confused now?
	}

	// checks for pallindrome... returns a boolean
	static boolean checkPallindrome(int posPall) {
		String strnum = Integer.toString(posPall); // BUG??
	    int leftPointer = 0;
	    int rightPointer = strnum.length()-1;
		
	    while (leftPointer<rightPointer) {
			
			boolean matches = ( strnum.charAt(leftPointer) == strnum.charAt(rightPointer) );
			if (!matches) return false;

			leftPointer++;
			rightPointer--;
		}
	    // else
		return true;
	}
}
