package basics;

public class BooleanNotes {
	
	// write a boolean method to hide tests inside methods
	public static boolean isSingleDigit(int x) {
		return x > -10 && x < 10;
	}

	public static void main(String[] args) {
		// Rational operators : ==, !=, >, <, <=, >=
		// Logical operators: &&, ||, !
		
		// Morgan's law : how to negate a logical expression
		/*
		 * !(A && B) => !A || !B
		 * !(A || B) => !A && !B
		 * !(A==0 && B>1) => A!=0 || B<=1
		 */
		
		int x = 5;
		// flag: variable represents condition or status
		boolean flag = (x % 2 == 0);
		
		// Do not compare flag to true of false
		if (!flag) { // do not write if(flag == true) => verbose
			System.out.println("x is odd");
		}

		
		
		
	}

}
