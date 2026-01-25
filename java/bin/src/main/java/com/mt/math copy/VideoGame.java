package math;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.Timer;

public class VideoGame implements ActionListener{
	private Drawing drawing;
	
	public VideoGame() {
		Sprite sprite = new Sprite("C:\\Users\\Anis\\Projets\\workspace-STS\\thinkJava\\src\\math\\gamer.png", 25, 150);
		drawing = new Drawing(800, 600);
		drawing.add(sprite);
		drawing.addKeyListener(sprite);//inherited from Canvas
		drawing.setFocusable(true);
		
		// setup the window frame
		JFrame frame = new JFrame("Video Game");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.add(drawing);
		frame.pack();
		frame.setVisible(true);

	}
	@Override
	public void actionPerformed(ActionEvent e) {
		//invokes step on all the actors of the drawing 
		drawing.step(); // repaint the Canvas
		
	}
	
	public static void main(String[] args) {
		VideoGame game = new VideoGame();
		Timer timer = new Timer(33, game);
		// every 33 milliseconds, the timer invokes actionPerformed, 
		timer.start();
	}

}
