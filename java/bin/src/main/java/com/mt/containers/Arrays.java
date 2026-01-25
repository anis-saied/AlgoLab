package containers;

import utils.StringUtils;

public class Arrays {

	
	public static double[] powArray(double[] a, int n) {
		for(int i=0; i<a.length; i++) {
			a[i] = Math.pow(a[i], n);
		}
		return a;
	}
	public static void main(String[] args) {
		// array²
		double[] arr = {1.0, 2.0, 3.0};
		double[] arrPow = Arrays.powArray(arr, 2);
		for(double e: arrPow) {
			System.out.printf("%4.2f\t",e);
		}
		StringUtils.newLine();
	}

}
