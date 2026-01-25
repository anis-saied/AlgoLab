package containers;

import java.util.ArrayList;
import java.util.List;

public class Stack {
	private List<Object> data;

	public Stack() {
		this.data = new ArrayList<>();
	}

	public void push(Object obj) {
		data.add(obj);
	}

	public Object peek() {
		if (data.size() > 0)
			return data.getLast();
		return null;
	}

	public Object pop() {
		if (data.size() > 0)
			return data.removeLast();
		return null;
	}

	public boolean isEmpty() {
		return this.data.size() == 0;
	}

	public int size() {
		return this.data.size();
	}

	public boolean has(Object obj) {
		return this.data.contains(obj);
	}

	@Override
	public String toString() {
		
		String str ="";
		for(Object obj: this.data.reversed()) {			
			str += String.format("|%4s|\n", obj); 
		}
		return str;
	}

	public static void main(String[] args) {
		Stack s = new Stack();
		s.push(1);
		s.push(10);
		s.push(100);
		System.out.print(s);
	}

}
