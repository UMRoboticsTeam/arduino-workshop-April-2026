# Notes for presenters

## April 2nd, 2026

After a long conversation with a small focus group of attendees, we concluded the following.

There were some specific diffulcties encountered by some members:

* If an attendee falls behind, there is no corrective action they can make.
* Some students are Comp.Sci students with good coding skills, they need an introduction to the physical components (inputs/outputs).
    * > "As a computer science student I can do the coding, I just don't know what the physical devices expect or what I can expect as output from them." (paraphrasing)

Discussed potential changes to be made for next time:

* Some components of the workshop were very good and don't need adjusted:
    1. The setup/loop code explanation & that component of the presentation.
    2. The physical description of the Arduino (power, analog pins, digital pins, etc.) & presentation.
    3. The arduino kits themselves were great!

* Recommendations for next time (in no order):
    * IMPORTANT: Allocate more time! Personally, I (Quinn T.) believe this is a good direction to go in. Minimum 3 hours to do a good introduction and give people time to experiment and try their own things, and also get help with those things.
    * Have a reference list of important methods and constants on the whiteboard with description of what they do.
        * Think: pinMode, Serial.begin, Serial.println, digitalWrite, digitalRead, analogWrite, analogRead, constants (INPUT, OUTPUT, HIGH, LOW)
    * Include a link to the presentation slides for attendees so they can go back when necessary

I asked the members for some of the most important things not to forget (because it was a long conversation):
* Include a motivation
* Start from a blank program (empty setup and loop)
* Explain as you go (Blink, Hello)
    * Easiest way to introduce methods: Line-by-line explaining what the purpose of each line is as you write it.
* If pre-written code is used, they should be expected to already understand it, and you should explain it again.
    * Meaning it should both be simple enough and use methods they already know.
* A bit more focus on the hardware itself would be appreciated.
    * A slide or two explaining how the components we are using work. For example, PWM was never explained.
    * Also, explain some other components in case they want to use them. (example: potentiometer, LED, other things in the kit)

### Recommended changes to slides
1. Keep the slides the same up to and including setup
2. Add reference slides near the beginning for methods and constants
3. Add a link to the slides for them to open (so they can go back to the reference)
4. Rely less on the Arduino examples, instead write them and explain line by line as you go.
5. Include diagrams for how things should be wired (something made from draw.io would prob work), like block diagrams.
    * An example diagram an attendee made that he would find helpful: (I digitized it with draw.io, probably should add colour)
        * ![image](./example.drawio.svg)
6. Add slides explaining the hardware itself, like servo and ultrasonic sensor.

Hope this helps!
