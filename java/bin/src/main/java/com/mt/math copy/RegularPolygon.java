package math;

import java.awt.Color;

public class RegularPolygon extends DrawablePolygon {

	public RegularPolygon(int nsides, int radius, Color color) {
		
		// validate the arguments in the most general constructor
		if(nsides<3) throw new IllegalArgumentException("Invalid nsides");
		if(radius<=0) throw new IllegalArgumentException("Invalid radius");
		if(color==null) throw new IllegalArgumentException("Invalid color");
		
		// Initialize DrawablePolygon attributes
		this.npoints = nsides;
		this.xpoints = new int[nsides];
		this.ypoints = new int[nsides];
		this.color = color;

		// the amount to rotate for each vertex (in radians)
		double theta = 2.0 * Math.PI / nsides;

		// compute x and y coordinates, centered at at the origin
		double x, y;
		for (int i = 0; i < nsides; i++) {
			x = radius * Math.cos(i * theta);
			y = radius * Math.sin(i * theta);
			xpoints[i] = (int) Math.round(x);
			ypoints[i] = (int) Math.round(y);
		}
	}

	// second constructor to make color optional
	public RegularPolygon(int nsides, int radius) {
		//this used to invoke another constructor in the same class
		this(nsides, radius, Color.GRAY); 
	}
	
	// another constructor to make radius parameter optional
	public RegularPolygon(int nsides) {
		//this used to invoke another constructor in the same class
		this(nsides, 50); 
	}
	
	
	
	public static void main(String[] args) {
		// the vertices are centered at the point (0,0)
		RegularPolygon rp = new RegularPolygon(6);
		
		// center the rp at (100,100)
		rp.translate(100, 100);

	}

}
