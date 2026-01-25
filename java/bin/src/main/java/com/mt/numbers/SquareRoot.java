package numbers;

public class SquareRoot {

	public static void main(String[] args) {
		// x1 = (x0 + a/x0)/2
		// read a double number
		// guess the square root (not using Math.sqrt)
		// begin with x0 = a/2
		double a = new ReadNumber().readDouble("a=");
		int iteration = 0, maxIterations = 1000;
		double x1, x0 = a / 2;
		do {
			x1 = (x0 + a / x0) / 2;
			x0 = x1;
			iteration ++;
		} while (iteration < maxIterations &&  Math.abs(x0 - x1) > 1e-10);
		String result = String.format("sqrt(%.2f) = %.3f", a, x1);
		System.out.println(result);

	}

}
