package math;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

/**
 * KeyListener : receive keyboard events: detect and response to key press
 * 
 * KeyEvent: specifies witch key was pressed, released or typed (pressed and
 * released)
 */
public class Sprite implements Actor, KeyListener {
	// the location of the sprite
	private int xpos;
	private int ypos;

	// the velocity of the sprite in the x and y directions
	private int dx;
	private int dy;
	private Image image;

	public Sprite(String path, int xpos, int ypos) {
		// the initial position
		this.xpos = xpos;
		this.ypos = ypos;

		try {
			this.image = ImageIO.read(new File(path));
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	@Override
	public void keyTyped(KeyEvent e) {
		// do nothing

	}

	@Override
	public void keyPressed(KeyEvent e) {
		switch (e.getKeyCode()) {
		case KeyEvent.VK_UP: 
			dy =-5;
			break;
		case KeyEvent.VK_DOWN: 
			dy = +5;
			break;
		case KeyEvent.VK_LEFT: 
			dx =-5;
			break;
		case KeyEvent.VK_RIGHT: 
			dx = +5;
			break;
		}
	}

	@Override
	public void keyReleased(KeyEvent e) {
		switch(e.getKeyCode()) {
		case KeyEvent.VK_UP:
		case KeyEvent.VK_DOWN:
			dy=0;
			break;
		case KeyEvent.VK_LEFT:
		case KeyEvent.VK_RIGHT:
			dx=0;
			break;
		}

	}

	@Override
	public void draw(Graphics g) {
		g.drawImage(image, xpos, ypos, null);

	}

	@Override
	public void step() {
		xpos += dx;
		ypos += dy;
	}

}
