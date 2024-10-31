# ANGM2305_FinalProject_Torres_Carlos
Description- 
    I will be creating a music visualizer for an mp3  file. This project will specifically focus on the song "Dullscythe" by Porter Robinson. If the project is succesful i might change it so it may work with any song.

Features- 
    -I will be using the pip library PyDub that will help me analyze the audio of the mp3 file so that i may break the audio down into its main frequency components. 
    -Then i will use PyGame to create the visuals for the audio file.
    -The Audio will be broken down into the frequency components of bass, midrange, and the higher frequencies
    -Then PyGame will have three different classes or functions that will tell the program what to draw depending on the frequency information given to it by PyDub.

Challenges-
    - The biggest and most obvious challenge is that i have never used PyDub before and will have to do research into how it works and what its limitations are.
    - Another challenge that i might have will be the communication between the PyDub and PyGame data. Im not exactly sure how i will manage that but i will look into it.
    - I will also have to make sure my laptop can process this kind of program with the complex visual and audio playback.

Outcomes-
    -For outcomes i hope i can get three basic visualizer graphics working.
    - I would like a circle pulse for the Bass.
    - A volume bar graphic for the Midranges.
    - Particles that fly out of the center of the screen       outwards for the High Frequencies.
    This is the minimal viable outcome.
    - For a more complete and artistic look i hope to add more specific frequency ranges and more stylized graphics.

MileStones-
    Week 1- Install PyDub and give the program the function of audio analysis. Obtain the mp3 file of the song. split the audio into 3 frequency blocks. Build Main PyGame window and set the event loop.
    
    Week 2- Create audio analysis of loudness levels over time chunks in the song. Also create a starting simple visual for each frequency block to know it works.
    
    week 3- Create the main visual components of the visualizer for the frequency blocks and timed event loops.
    Choose decay time, screen presence, volume interaction and other details.
    
    Week 4- Add detailed visuals by possibly breaking down the song further into more specific frequency blocks and loudness levels. Then add more visuals for those blocks.
    
    Week 5- Optimization, polishing, and final testing. Possibly look into adapting visualizer for any mp3 file.