package arrays;

import java.util.Arrays;

/**
 * the array:  is a memory location
 * the array variable: is a reference to this location (to this array)
 */
public class BasicArray {

	public static void main(String[] args) {
		int[] arr; // declare an int array
		// arr refer to an array of 3 integers
		arr = new int[3]; // allocates memory for the array, 
		// the new operator initializes all of its elements to 0
		
		
		// initialize array with array literal
		int[] a = {1,2,3};
		
		// [I@79fc0f2f : [ => array, I => integers, @79fc0f2f => address of the array in memory
		System.out.println(a);  
		
		// display array
		String str = Arrays.toString(a);
		System.out.println(str);
	}

}
