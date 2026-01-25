package files;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileHelpers {

	
	public static void main(String[] args) {

		String path = "C:\\Users\\Anis\\Desktop\\ds2.txt";
		File f = new File(path );
		try (Scanner scan = new Scanner(f)) {
			System.out.println(scan.nextLine());
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

	}

}
