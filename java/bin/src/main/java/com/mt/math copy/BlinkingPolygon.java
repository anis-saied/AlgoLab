package math;

import java.awt.Color;
import java.awt.Graphics;

public class BlinkingPolygon extends RegularPolygon {
	protected boolean visible;
	protected int count;

	public BlinkingPolygon(int nsides, int radius, Color c) {
		super(nsides, radius, c);
		visible = true;
		count = 0;
	}

	public void draw(Graphics g) {
		if (visible) // draw the polygon only if it is visible
			super.draw(g);
	}

	public void step() {
		count++;
		if (count == 10) {
			visible = !visible;
			count = 0;
		}
	}

}
