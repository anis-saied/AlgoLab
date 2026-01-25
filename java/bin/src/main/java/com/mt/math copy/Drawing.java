package math;

import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;

import javax.swing.JFrame;

public class Drawing extends Canvas {
	private ArrayList<Actor> list;

	public Drawing(int width, int height) {
		setSize(width, height);
		setBackground(Color.WHITE);
		list = new ArrayList<Actor>();
	}

	public void add(Actor dp) {
		list.add(dp);
	}

	// override the paint method inherited from the Canvas
	public void paint(Graphics g) {
		for (Actor dp : list) {
			dp.draw(g);
		}
	}

	public void step() {
		for (Actor dp : list) {
			dp.step();
		}
		repaint(); // clears and redraw the canvas
	}

	public static void main(String[] args) {
		// created some regular polygons
		DrawablePolygon dp1 = new RegularPolygon(3, 50, Color.GREEN);
		DrawablePolygon dp2 = new RegularPolygon(6, 50, Color.ORANGE);
		DrawablePolygon dp3 = new RegularPolygon(360, 50, Color.BLUE);
		DrawablePolygon dp4 = new BlinkingPolygon(5, 50, Color.RED);

		// move them out of the corner
		dp1.translate(100, 80);
		dp2.translate(250, 120);
		dp3.translate(400, 160);
		dp4.translate(50, 150);

		// create drawing and add polygons
		Drawing drawing = new Drawing(500, 250);
		drawing.add(dp1);
		drawing.add(dp2);
		drawing.add(dp3);
		//drawing.add(dp4);

		//
				
		// setup the window frame
		JFrame frame = new JFrame("Drawing");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.add(drawing);
		frame.pack();
		frame.setVisible(true);

		//
		while (true) {
			drawing.step();
			try {
				Thread.sleep(1000/30); // 1/30 second
			} catch (InterruptedException e) {
				// do nothing
			}
		}

	}

}
