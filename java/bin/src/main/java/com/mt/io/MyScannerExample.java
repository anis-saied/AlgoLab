package io;
import java.util.Scanner;

public class MyScannerExample {

	public static void main(String[] args) {
		// 
		String line;
		Scanner in = new Scanner(System.in);

		System.out.print("Print something: ");
		line = in.nextLine(); // reads characters (entire line of input) until it gets to a newline
		
		System.out.println("line: "+ line);
		
		System.out.print("type an integer =");
		int a = in.nextInt(); // reads characters until it gets to a non-digit
		// when you read a line after an int or double, add an extar in.nextline()
		
		System.out.print("type a double value:");
		double d = in.nextDouble(); // reads input from the keyboard and return the value as a double
		System.out.printf("readed value: %f \n", d); 
		
		// check if the next input can be interpreted as a double
		System.out.println("type a double to check it:");
		if(in.hasNextDouble()) {
			d= in.nextDouble();
			System.out.printf("double is %f \n", d);
		}else {
			String word = in.next(); // return only the next token of input
			System.out.printf("is just a String  %s \n", word);
		}
		
		
		in.close();
	}

}
