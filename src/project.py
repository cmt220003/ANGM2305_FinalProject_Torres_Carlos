# Create a an Audio Visualizer for Dullscythe by Porter Robinson.
import pydub
import numpy
import pygame


def song_file():
    # Use pydub for audio analysis and frequency block breakdown into Bass, Midrange and Treble.
    from pydub import AudioSegment
    song = AudioSegment.from_file("dullscythe.mp3")


def bass_analysis():
    # analyze frequency and audio loudness of bass section based on pydub.

def midrange_analysis():
    # analyze frequency and audio loudness of midrange based on pydub.

def treble_analysis():
    # analyze frequency and audio loudness of treble based on pydub.

def screen_window():
    # Create a black screen for the following track to be able to draw on using pygame. A screen of 960px by 540px.

def bass_visual():
    # Use pygame to create a red circle pulse with parameters of size, thickness, and decay.

def midrange_visual():
    # Use pygame to create a visual of blue bars that sit vertically at the center bottom of the screen. With parameters of how thick the bars are how far apart they are and how high up they go when activated.

def treble_visual():
    # Use pygame to create a green waveform that sits horizontally across the middle of the screen

def main():
    # create a while running loop to run bass_visual, midrange_visual, and treble_visual simultaneously along with the mp3 file chosen.

if __name__ == "__main__":
    main()