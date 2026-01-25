package utils;

public class Exos {

	public static boolean isAbecedarian(String str) {
		String alphabet = "";
		for (char c = 'A'; c <= 'Z'; c++) {
			alphabet += String.valueOf(c).toUpperCase();
		}
		System.out.println(alphabet);
		
		for(int i = 0; i<str.length(); i++) {
			String str1 = str.substring(i).toUpperCase();
			char currentChar = str1.charAt(0);
			int from = alphabet.indexOf(currentChar);
			if (from <0)
				return false;
			alphabet = alphabet.substring(from+1);
		}
		return true;
	}

	public static boolean isDoublon(String str) {
		int counter;
		char currentChar;
		for (int i=0;i<str.length();i++) {
			counter = 0;
			currentChar = str.charAt(i);			
			for (int j=0; j<str.length(); j++) {
				if (str.charAt(j) == currentChar)
					counter++;
			}
			if (counter != 2)
				return false;
		}
		return true;
	}
	
	public static void main(String[] args) {
		String str = "aabbddeesstt";
		System.out.printf("%s is %sabecedarian\n", str, isAbecedarian(str) ? "" : "not ");
		System.out.printf("%s is %sdoublon", str, isDoublon(str) ? "" : "not ");
		
	}

}
