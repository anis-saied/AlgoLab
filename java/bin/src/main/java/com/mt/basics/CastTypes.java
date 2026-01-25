package basics;

public class CastTypes {

	public static void main(String[] args) {
		
		// Java performs integer division when operands are integers
		int a = 1, b=3;
		System.out.println("1/3 = " + a/b);
		
		// use Floating-point number : double
		System.out.println("1/3.0 = "+ 1/3.0);
		
		// Java executes operations from left to right
		System.out.println("Hello" + 1 + 2);
		System.out.println(1 + 2 + "Hello");
		
		
		// cast double to integer: use (int) cast operator
		int c = (int) (4.0 / 3.0);
		System.out.println(c);
		
		// Type casting takes precedence over arithmetic operations.
		System.out.println((int) 2.5 * 2.0); // 4.0 not 5.0

		// the % is the “remainder operator” (not modulus).
		// modulus is the number you dividing by (example: in 10 % 2; the 2 is modulus)
		System.out.println("15 % 2 = " + 15 % 2);
	}

}
