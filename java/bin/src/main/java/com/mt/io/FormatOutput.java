package io;

public class FormatOutput {

	public static void main(String[] args) {
		// by default: 16 decimal places
		System.out.println("4.0 / 3.0 = "+ 4.0 / 3.0); // 1.3333333333333333
		
		// formatted string : floatting-point rounded to 3 decimal places
		System.out.printf("4.0 / 3.0 = %.3f \n", 4.0 / 3.0); // by default format string ends with new line character
		
		// %d : decimal (base 10) , displays integer values
		// at least 8 digits, padded with zeros
		// "cin : %08d" : is the format String
		// %08d : is the format specifier : specifies the data type
		System.out.printf("cin : %08d \n", 1234);
		
		// %d with double value
		// java.util.IllegalFormatConversionException: d != java.lang.Double
		// System.out.printf("value = %d \n", 2.5);
		
		// %f with integer value
		// java.util.IllegalFormatConversionException: f != java.lang.Integer
		// System.out.printf("value = %f \n", 10);
	}

}
