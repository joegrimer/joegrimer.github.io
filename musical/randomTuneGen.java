/* RandomTuneGen - java
 * Joseph Grimer November 2017
 * I set out the initial goal!
 * I intended to create a reasonably-nice music generator, and it worked!
 * I could add more and more and more. it's rather crummy at the moment.
 * But it's not too shabby!
 * 
 * List of Bugs:
 * When the random number 7 is returned from rand14 - to generate tones, * it seems to make 1.20000002 when I try to convert it to a sensible double
 * 
 * Potential Improvements:
 * Add different kinds of "modifiers" to build on the random tune and generate more varied note-set transformations:
 * - a +1 octave modifier
 * 
 * Inspired by:
 * A video of a young girl being given four random notes from a hat, and using them to produce a full piece of music
 * 
 * More notes:
 * I think i might go and learn a bit of real music theory before coming to have another look at this project.
 */

package randomTuneGen;

import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.SourceDataLine;

public class randomTuneGen {


	public static void main(String[] args) throws LineUnavailableException{

		// making the music
		double[] tones;
		tones = new double[60]; // 60 notes
//		tones[0] = 0.9;
//		tones[1] = 2.0;
//		tones[2] = 1.0;
//		tones[3] = 0.5;
	
//		tones[4] = 0.0;
		
		short meter = 4;
		
		tones[0] = 0.5 + (0.1*rand14());
		tones[1] = 0.5 + (0.1*rand14());
		tones[2] = 0.5 + (0.1*rand14());
		tones[3] = 0.5 + (0.1*rand14());
		System.out.println("first four tones are: "+tones[0]+"<>"+tones[1]+"<>"+tones[2]+"<>"+tones[3]);
		
		for(int h=1;h<=2;h++) {
			// copy preceding 4 notes
			tones[h*meter + 0] = tones[(h-1)*meter + 0];
			tones[h*meter + 1] = tones[(h-1)*meter + 1];
			tones[h*meter + 2] = tones[(h-1)*meter + 2];
			tones[h*meter + 3] = tones[(h-1)*meter + 3];
			
			// vary tune
			int whichToChange = rand(4);
			tones[(h*meter)+whichToChange] = 0.5 + (0.1*(double)rand14());
		}
		
		/*
		for(double tn : tones) {
			System.out.println(tn);
		}
		/* */
		
		// current theory... vary 1 note
		
//		double tone = 2.5;
		
		/*
		// running the music
		// initialising sound object
		byte[] buf = new byte[ 1 ];
		AudioFormat af = new AudioFormat( (float)44100, 8, 1, true, false );

		SourceDataLine sd1 = AudioSystem.getSourceDataLine( af );
		sd1.open();
		sd1.start();

		// looping through tones
		for(int i =0; i < tones.length;i++) {
			double tone = tones[i];
			// 44100 seems to be about a second
			int second = 44100;
			int time = (int) (0.4 * second);
			for(int j = 0; j < time; j++) {
//				double angle = i / ( (float)44100 / 440 ) * tone * Math.PI; // original
				double angle = j / ( 100.22727 ) * tone * Math.PI;
				buf[ 0 ] = (byte)( Math.sin( angle ) * 100);
				sd1.write( buf, 0, 1);
			}
		}

		// running the finally constructed sound object
		sd1.drain();
		sd1.stop();
		/* */
		
		System.out.println("End of program.");
		System.exit(0); // very important! // maybe the JVM won't get confused now?

	}
	private static int rand(int outOf) {
		
		return (int) Math.floor(Math.random() * outOf);
	}
	private static int rand14() {
		
		int randomNumber = (int) Math.floor(Math.random() * 14);
		System.out.println("returning random: " + randomNumber);
		return randomNumber;
	}
	
}