package strings;

import containers.Stack;

public class Parser {
	private String data;

	public Parser(String data) {
		this.data = data;
	}

	public double eval(String str) {
		Stack s = new Stack();
		for (char c : str.toCharArray()) {			
			if (c != ' ')
				s.push(c);
		}
		System.out.print(s);
		return 0;
	}

	public static void main(String[] args) {
		String str = "12 3+4";
		Parser parser = new Parser(str);
		parser.eval(str);

	}

}
