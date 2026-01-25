package numbers;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.Iterator;

import utils.StringUtils;

public class Big {

	public static BigInteger factorial(int n) {
		if (n < 2) {
			return BigInteger.ONE;
		} else {
			return BigInteger.valueOf(n).multiply(factorial(n - 1));
		}
	}

	public static BigInteger pow(int x, int n) {
		if (n == 0)
			return BigInteger.ONE;
		else if (n == 1)
			return BigInteger.valueOf(x);
		else {
			BigInteger t = pow(x, n / 2);
			if (n % 2 == 0)
				return t.multiply(t);
			else {
				return BigInteger.valueOf(x).multiply(t).multiply(t);
			}
		}
	}

	/**
	 * add the n first terms to calculate exp(x)
	 * 
	 * exp(x) = 1 + x + x²/2! + x^3/3!+...+x^n/n!
	 * @param x
	 * @param n
	 * @return
	 */
	public static double myexp(int x, int n) {
		double e = 1;
		for (int i = 1; i <= n; i++) {
			double N = Big.factorial(i).doubleValue();
			System.out.printf("%20d!=%20f\t", i, N);
			double X = Big.pow(x, i).doubleValue();
			System.out.printf("%5d^%2d=%10f", x, i, X);
			e += X / N;
			System.out.printf("%10s term[%2d] = %10f\n", "", i, X / N);
		}
		StringUtils.newLine();

		return e;
	}

	public static double myexp2(int x, int n) {
		double[] terms = new double[n];
		terms[0]=1;
		for (int i = 1; i < n; i++) {
			terms[i] = terms[i-1] * (x/(i*1.0));
		}
		return Arrays.stream(terms).sum();
	}

	public static void main(String[] args) {
		int n = 10;
		// System.out.printf("%d! = %d",n,Big.factorial(n));

		StringUtils.newLine();

		int x = 1;
		// System.out.printf("%d^%d = %d", x ,n,Big.pow(x, n));

		double r = Big.myexp(x, n);
		System.out.printf("e(%d)=%f", x, r);
		
		StringUtils.newLine();
		System.out.printf("e2(%d)=%f", x, Big.myexp2(x, n));
		
	}

}
