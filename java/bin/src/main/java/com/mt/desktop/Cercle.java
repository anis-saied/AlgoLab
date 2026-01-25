package desktop;
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;

public class Cercle extends Canvas{
	private static final int WIDTH = 300;
	private static final int HEIGHT = 300;
	
	public static void main(String[] args) {
		JFrame frame = new JFrame();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Cercle cercle = new Cercle();
		cercle.setSize(WIDTH, HEIGHT);
		cercle.setBackground(Color.WHITE);
		frame.add(cercle);
		frame.pack();
		frame.setVisible(true);
	}
	
	public void paint(Graphics g) {
		g.fillOval(0, 0, 200, 200);
	}

}
