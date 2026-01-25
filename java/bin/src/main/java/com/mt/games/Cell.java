package games;

import java.awt.Color;
import java.awt.Graphics;

public class Cell {
	public static final Color[] COLORS = {Color.WHITE, Color.BLACK};
	private final int x;
	private final int y;
	private final int size;
	private int state;
	
	
	
	public Cell(int x, int y, int size) {
		this.x = x;
		this.y = y;
		this.size = size;
		this.state = 0;
	}

	
	public void draw(Graphics g) {
		// draw the center of the cell
		g.setColor(COLORS[this.state]);
		g.fillRect(x+1, y+1, size-1, size-1); 
		
		// draw the border of the cell 
		g.setColor(Color.LIGHT_GRAY);
		g.drawRect(x, y, size, size);
	}

	
	public boolean isOff() {
		return this.state ==0;		
	}
	
	
	public boolean isOn() {
		return this.state==1;
	}
	
	public void turnOff() {
		this.state = 0;
	}

	public void turnOn() {
		this.state = 1;
	}
	
	
	@Override
	public String toString() {
		return String.format("Cell[%d,%d]=%b\n", x,y,isOn());
	}
	public static void main(String[] args) {
		Cell cell = new Cell(0,0,10);
		System.out.print(cell);
	}

}
