package games;

import java.awt.Canvas;
import java.awt.Graphics;

public class GridCanvas extends Canvas {
	private Cell[][] array; // 2D array of Cells

	public GridCanvas(int rows, int cols, int size) {
		array = new Cell[rows][cols];
		for (int r = 0; r < rows; r++) {
			int y = r * size;
			for (int c = 0; c < cols; c++) {
				int x = c * size;
				array[r][c] = new Cell(x, y, size);
			}
		}

		// set the canvas size
		setSize(cols * size, rows * size);
	}

	// to draw the grid, we simply draw each cell
	public void draw(Graphics g) {
		// for each row in the array
		for (Cell[] row : array) {
			// for each cell in the row
			for (Cell cell : row) {
				// draw the cell in the graphics context
				cell.draw(g); // each cell know how to draw itself (they know its x, y and size)
			}
		}
	}

	public void paint(Graphics g) {
		draw(g);
	}

	public int numRows() {
		return array.length;
	}

	public int numCols() {
		return array[0].length;
	}

	public Cell getCell(int r, int c) {
		return array[r][c];
	}

	public void turnOn(int r, int c) {
		array[r][c].turnOn();
	}

	@Override
	public String toString() {
		return "Grid:";
	}

	public int test(int r, int c) {
		try {
			if (array[r][c].isOn())
				return 1;
		} catch (ArrayIndexOutOfBoundsException e) {
			// cell dosen't exist
		}
		return 0;
	}



	public static void main(String[] args) {
		GridCanvas gc = new GridCanvas(3, 3, 50);
		System.out.println(gc);
	}

}
