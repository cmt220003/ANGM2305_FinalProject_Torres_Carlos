# Create a an Audio Visualizer for Dullscythe by Porter Robinson.
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import low_pass_filter, high_pass_filter
import numpy
import pygame
import threading
import math
import time



def song_file():
    # Use pydub for audio analysis and frequency block breakdown into Bass, Midrange and Treble.
    song = AudioSegment.from_file("dullscythe.wav")
    return song

def bass_analysis(segment):
    # analyze frequency and audio loudness of bass section based on pydub.
    low_passed = low_pass_filter(segment, 299)  # Low-Pass filter below 299 Hz
    bass_only = high_pass_filter(low_passed, 30)  # High-pass filter above 30 Hz
    print("success 1")
    return bass_only.dBFS  # Get amplitude in dBFS (decibels relative to full scale)
    

def midrange_analysis(segment):
    # analyze frequency and audio loudness of midrange based on pydub.
    low_passed = low_pass_filter(segment, 5999)    # Low-pass filter below 5999 Hz
    mid_only = high_pass_filter(low_passed, 300)  # High-pass filter above 300 Hz
    print("success 2")
    return mid_only.dBFS

def treble_analysis(segment):
    # analyze frequency and audio loudness of treble based on pydub.
    treble_only = high_pass_filter(segment, 6000)  # High-pass filter above 6000 Hz
    print("success 3")
    return treble_only.dBFS

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