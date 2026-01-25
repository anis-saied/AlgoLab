package math2d;

import java.awt.*;
import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;

public class Geometry {

	public void show(Point p) {	
		String str = "";
		for(int i=0; i<(int)p.x; i++)
			str+= " ";
		System.out.printf("\s*\n", str);
	}

	public static void main(String[] args) {
		Point p = new Point();
		Geometry geo = new Geometry();
		Random random = new Random();

		int n = 5; // Interval in seconds
		Timer timer = new Timer();
		TimerTask task = new TimerTask() {
			@Override
			public void run() {
				int dx = random.nextInt(100);
				int dy = random.nextInt();
				p.translate(dx, dy);
				geo.show(p);
				
			}
		};

		timer.scheduleAtFixedRate(task, 0, n * 100);
	}

}
