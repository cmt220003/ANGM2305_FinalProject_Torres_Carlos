from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import low_pass_filter, high_pass_filter
import pygame
import numpy
import threading
import threading
import time
import math
# Create a an Audio Visualizer.
def song_file():
    # Use pydub for audio analysis and frequency block breakdown into Bass, Midrange and Treble.
    song = AudioSegment.from_file("dullscythe.wav")
    return song

# Bass analysis (30–299 Hz)
def bass_analysis(segment):
    low_passed = low_pass_filter(segment, 299)  # Low-Pass filter below 299 Hz
    bass_only = high_pass_filter(low_passed, 30)  # High-pass filter above 30 Hz
    return bass_only.dBFS  # Get amplitude in dBFS (decibels relative to full scale)

# Midrange analysis (300–5999 Hz)
def midrange_analysis(segment):
    low_passed = low_pass_filter(segment, 5999)    # Low-pass filter below 5999 Hz
    mid_only = high_pass_filter(low_passed, 300)  # High-pass filter above 300 Hz
    return mid_only.dBFS

# Treble analysis (6000–20,000 Hz)
def treble_analysis(segment):
    treble_only = high_pass_filter(segment, 6000)  # High-pass filter above 6000 Hz
    return treble_only.dBFS

def adjust_amplitude(amplitude, min_amp=-60, max_amp=0):
    return max(min(amplitude, max_amp), min_amp)

# Set up the screen
def screen_window():
    pygame.init()
    screen = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Audio Visualizer - Dullscythe by Porter Robinson")
    return screen

def bass_visual(screen, amplitude, base_thickness=2, thickness_factor=0.5, fade_opacity=128):
    # Use pygame to create a red circle pulse with parameters of size, thickness, and decay.
    amplitude = adjust_amplitude(amplitude)
    color = (255, 0, 0)
    center = (480, 270)
    max_radius = 600
    # Radius increases with amplitude.
    radius = int((amplitude + 60) * 3)  # Adjust scaling for visible changes
    radius = min(radius, max_radius)
    # Increase thickness with radius.
    thickness = int(base_thickness + radius * thickness_factor)
    # Calculate alpha based on radius.
    max_alpha = 255
    alpha = max(int(max_alpha - (radius / max_radius) * (max_alpha - fade_opacity)), fade_opacity)
    # Create a transparent surface to draw cricle on.
    overlay = pygame.Surface((960, 540), pygame.SRCALPHA)
    pygame.draw.circle(overlay, (*color, alpha), center, radius, thickness)
    # Blit the overlay onto screen
    screen.blit(overlay, (0, 0))

def midrange_visual(screen, amplitude):
    # Use pygame to create a visual of blue bars that sit vertically at the center bottom of the screen. With parameters of how thick the bars are how far apart they are and how high up they go when activated.
    amplitude = adjust_amplitude(amplitude)
    color = (0, 0, 255)
    num_bars = 9
    bar_width = 30
    spacing = 50
    max_height = 150
    for i in range(num_bars):
        bar_height = min(int((amplitude + 60) * 3), max_height)
        x = 480 + (i - num_bars // 2) * (bar_width + spacing)
        y = 540 - bar_height
        pygame.draw.rect(screen, color, (x, y, bar_width, bar_height))

def treble_visual(screen, amplitude):
    # Use pygame to create a green waveform that sits horizontally across the middle of the screen
    amplitude = adjust_amplitude(amplitude)
    color = (0, 255, 0)
    for x in range(0, 960, 20):
        y = 270 + int((amplitude + 60) * (x % 2 * 2 - 1))
        pygame.draw.line(screen, color, (x, 270), (x, y), 1)

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("dullscythe.wav")
    pygame.mixer.music.play()
    
def main():
    play_song()
    
    # Load the song and set up segments for analysis.
    song = song_file()
    segment_lenght= 25 # miliseconds
    segments = [song[i:i + segment_lenght] for i in range(0, len(song), segment_lenght)]

    # set up the screen
    screen = screen_window()
    clock = pygame.time.Clock()

    threading.Thread(target=play_song, daemon=True).start()
    time.sleep(0.25)

    running = True
    while running:
        screen.fill((0, 0, 0,)) # Black Background

        current_time = pygame.mixer.music.get_pos()
        if current_time == -1:
            print("Error: No Audio Detected.")
            break

        current_segment = current_time // segment_lenght

        if current_segment <len(segments):
            # Get Current segment and analyze frequencies.
            segment = segments[current_segment]
            bass_amp = bass_analysis(segment)
            mid_amp = midrange_analysis(segment)
            treble_amp = treble_analysis(segment)

            #run visuals
            bass_visual(
                screen,
                amplitude=bass_amp, 
                base_thickness=2, 
                thickness_factor=0.05,
                fade_opacity=128
            )
            midrange_visual(screen, mid_amp)
            treble_visual(screen, treble_amp)
        else:
            print("End of Audio Segments.")
            running = False

        pygame.display.flip()
        clock.tick(20) #FPS Limit

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()