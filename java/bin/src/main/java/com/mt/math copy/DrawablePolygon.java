package math;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Polygon;
/**
 * in terms of inheritance, DrawablePolygon is both a Polygon and Actor
 * 
 * we can do:
 * 
 * Polygon p = new DrawablePolygon();
 * Actor c = new DrawablePolygon();
 * 
 * we can also replace DrawablePolygon by heir sub classes
 * 
 * Actor c = new RegularPolygon();
 */
public class DrawablePolygon extends Polygon implements Actor {
	protected Color color;

	public DrawablePolygon() {
		super(); // to initialze xpoints, ypoints and npoints
		color = Color.GRAY;
	}

	public void draw(Graphics g) {
		g.setColor(color);
		g.fillPolygon(this);
	}

	public void step() {
		// do nothing
	}
	
	public static void main(String[] args) {
		DrawablePolygon p = new DrawablePolygon();
		p.addPoint(57, 100);
		p.addPoint(100, 35);
		p.addPoint(143, 110);
		p.color = Color.GREEN;
	}
}
