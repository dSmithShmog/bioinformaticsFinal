TITLE: PKU (Gene) Simulator
AUTHOR: Dillan Smith

Purpose: To visually model how Phenylketonuria -- PKU -- or any other given genetic property spreads in a community within an 
enclosed 'space'

Description: This uses Python and PyGame to visually model a group of 'people' bouncing around in a confined space. 
A certain number of them have PKU, a rare Mendelian genetic disease. This means that it has two loci that are either 
dominant or recessive which makes predicting how it spread to children predictable. Individuals bounce around and
when they make contact they produce a child that either does or does not have PKU.

Future Work: Unfortunately I ran into some serious system issues where the script is only capable of showing a couple hundred 
individuals before essentially crashing. I would need to model well over 10000 for this to have any meaning. I would also like
to make the system flexible enough to model more varied diseases and to control the geography of what is now a 2D empty space.