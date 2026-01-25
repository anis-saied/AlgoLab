package games;

import java.util.Arrays;
import java.util.Random;

import javax.swing.JFrame;

import arrays.ArrayHelpers;

public class Conway {

	private GridCanvas grid;

	public Conway() {
		// 5 rows, 10 columns, 20 pixels for height and width
		configureGame();



	}

	private void configureGame() {
		Random random = new Random();
		int rows = random.nextInt(20);
		int cols = random.nextInt(20);
		grid = new GridCanvas(rows, cols, 50);
		
		// make alive n cells in the grid
		int n = random.nextInt(rows * cols);
		for(int i=0; i<n; i++) {
			//choose random coordinates
			int x = random.nextInt(rows);
			int y = random.nextInt(cols);
			grid.turnOn(x,y);			
		}
	}

	public int countAlive(int r, int c) {
		int count = 0;
		for (int i = r - 1; i <= r + 1; i++) {
			for (int j = c - 1; j <= c + 1; j++) {
				if (i == r && j == c)
					continue;
				count += grid.test(i, j);
			}
		}
		return count;
	}

	public void update() {
		int[][] counts = countNeighbors();
		if(ArrayHelpers.all(counts, 0)) {
			// all the cells are death
			System.exit(0);
		}
		updateGrid(counts);
	}

	private int[][] countNeighbors() {
		int rows = this.grid.numRows();
		int cols = this.grid.numCols();

		int[][] counts = new int[rows][cols];
		for (int r = 0; r < rows; r++) {
			for (int c = 0; c < cols; c++) {
				counts[r][c] = countAlive(r, c);
			}
		}
		return counts;
	}

	private void updateGrid(int[][] counts) {
		int rows = this.grid.numRows();
		int cols = this.grid.numCols();
		
		for (int r = 0; r < rows; r++) {
			for (int c = 0; c < cols; c++) {
				Cell cell = grid.getCell(r, c);
				updateCell(cell, counts[r][c]);
			}
		}
	}

	public static void updateCell(Cell cell, int count) {
		if(cell.isOn()) {
			if(count<2 || count>3) {
				cell.turnOff();
			}
		}else {
			if(count==3) {
				cell.turnOn();
			}
		}
		
	}

	public static void main(String[] args) {
		String title = "Conway's Game Of Life";
		Conway game = new Conway();
		JFrame frame = new JFrame(title); // create a window on the screen
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setResizable(false);
		frame.add(game.grid);// add the GridCanvas inside the frame
		frame.pack();// resize the frame to fit the canvas
		frame.setVisible(true); // makes the frame visible
		game.mainloop();
	}



	/**
	 * Simulate the time steps of the game of life
	 */
	private void mainloop() {
		// each time step
		while (true) {
			// update the state of the game
			 this.update();
			// repaint the grid
			grid.repaint(); // repaint comes from the Canvas class
			
			try {
				// to see the animation
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// do nothing
			}
		}

	}

}
