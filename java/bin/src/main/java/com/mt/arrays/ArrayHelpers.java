package arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class ArrayHelpers {

	public static void main(String[] args) {
//		Object[] arr = { 1, 2, 3, 4, 5, 6.0 };
//		ArrayHelpers.shuffle(arr);
//		System.out.println(Arrays.toString(arr));
		int[] a = { 10, 2, 5, 0, 11, 9, 15, 13, 4, 6, -1, 88, 31, 88 };
		int[] sortedArray = ArrayHelpers.mergeSort(a);
		System.out.println("merge sort =" + Arrays.toString(sortedArray));
	}

	public static void swapElements(Object[] arr, int i, int j) {
		Object obj = arr[i];
		arr[i] = arr[j];
		arr[j] = obj;
	}

	public static int randomInt(int low, int heigh) {
		Random random = new Random();
		return random.nextInt(low, heigh + 1);
	}

	public static void shuffle(Object[] arr) {
		int n = randomInt(0, arr.length); // number of swapping
		int j, k;
		for (int i = 0; i < n; i++) {
			j = randomInt(0, arr.length - 1);
			k = randomInt(0, arr.length - 1);
			swapElements(arr, j, k);
		}
	}

	/**
	 * merge sort, complexity of n log_2(n)
	 * 
	 * @param arr integer array
	 * @return sorted integer array
	 */
	public static int[] mergeSort(int[] arr) {
		if (arr.length <= 1)
			return arr;
		else {
			int mid = arr.length / 2;
			int[] sub1 = new int[mid];
			for (int i = 0; i < mid; i++)
				sub1[i] = arr[i];

			int[] sub2 = new int[arr.length - mid];
			for (int i = 0; i < arr.length - mid; i++)
				sub2[i] = arr[mid + i];

			// THEORY: THE LEAP OF FAITH (from the book think java 2 , section 8.4)

			// we suppose that sub1 and sub2 will be (are) sorted correctly
			sub1 = mergeSort(sub1);
			sub2 = mergeSort(sub2);

			// then we just merge them
			int[] result = new int[arr.length];
			int k = 0; // index for result
			int i = 0; // index for sub1
			int j = 0; // index for sub2
			// merge sub1 and sub2 into result array
			while (k < result.length) {
				if (i < sub1.length) {
					if (j < sub2.length) {
						if (sub1[i] < sub2[j]) {
							result[k] = sub1[i];
							i++;
						} else {
							result[k] = sub2[j];
							j++;
						}
						k++;
					} else {
						// reach the end of sub2
						// add the rest of sub1 to result
						for (int z = i; z < sub1.length; z++) {
							result[k] = sub1[z];
							k++;
						}
					}
				} else {
					// reach the end of sub1
					// add the elements of sub2 to result
					for (int z = j; z < sub2.length; z++) {
						result[k] = sub2[z];
						k++;
					}
				}
			}
			return result;
		}
	}

	public static int[] getRow(int[][] array, int index) {
		return array[index];
	}

	public static int[][] getColumn(int[][] array, int index) {
		int rows = array.length;
		int[][] col = new int[rows][1];
		for (int r = 0; r < rows; r++) {
			col[r][0] = array[r][index];
		}
		return col;
	}

	public static void displayArray(int[][] array) {

		int[] row;

		StringBuilder strBuilder = new StringBuilder();
		int i;
		String str;
		strBuilder.append("[\n");
		for (i = 0; i < array.length - 1; i++) {
			row = ArrayHelpers.getRow(array, i);
			str = Arrays.toString(row);
			strBuilder.append(" " + str + ",\n");
		}
		row = ArrayHelpers.getRow(array, i);
		str = Arrays.toString(row);
		strBuilder.append(" " + str + "\n]");

		System.out.println(strBuilder.toString());
	}

	public static boolean contains(int[] array, int value) {
		Arrays.sort(array);
		int index = Arrays.binarySearch(array, value);
		return index != -1 ? true : false;
	}

	public static boolean contains(int[][] array, int value) {
		int rows = array.length;
		int index;
		for (int r = 0; r < rows; r++) {
			int[] row = array[r];
			Arrays.sort(row);
			index = Arrays.binarySearch(array, value);
			if (index != -1)
				return true;
		}
		return false;
	}

	public static boolean all(int[][] array, int value) {
		int rows = array.length;
		int cols = array[0].length;

		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < cols; j++) {
				if (array[i][j] != value)
					return false;
			}
		}
		return true;
	}

}
