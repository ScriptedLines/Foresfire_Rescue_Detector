
# UAS-DTU Departmental Task

Created by Aaryaman Bisht
24/A11/006



## Installation

To install my project:
Download the detect.py and the Images folder
And replace the path of main_folder in detect.py to the location of the images folder
for eg:
main_folder="....\\Images"



    
## Deployment

To deploy this project:
Ensure there are images in the imae folder, either use the default images or create you own!

Also Ensure you got the latest version of Python installed, and also the modules:
1) OpenCV
2) Numpy
3) os




## Usage

The program simulates a scenario where a fire has broken out in a civilian area, and our UAV has collected images of the affected region. Our goal is to gather information about the buildings and grass areas from these images and calculate rescue priorities for search and rescue operations.

It takes 10 images as input in .png format
The brown area is burnt grass
The green area is unburnt (green) grass
The blue and red triangles are houses
Each house colour has an associated priority
Blue house have a priority of 2
Red houses have a priority of 1



![Logo](https://i.ibb.co/5rPkW3R/Screenshot-2024-10-01-234705.png)

We need to give output image in form


![Logo](https://i.ibb.co/4NtDmX9/Screenshot-2024-10-02-172845.png)


And this returns:
The number of houses on the burnt grass (Hb) and the number of houses on the green grass (Hg), saved in a list

The total priority of houses on the burnt grass (Pb) and the total priority of houses on the green grass (Pg), saved in a list

A rescue ratio of priority Pr where Pr = Pb / Pg , saved in a list

A list of the names of the input images , arranges in descending order of their rescue ratio
(Pr)
## Example Use Case

For the Images given in the repository, it returns the following data:

The list of number of house in burnt grass and no.of hosues in green grass:
 [[3, 2], [6, 4], [5, 4], [8, 6], [3, 4], [6, 3], [6, 4], [2, 6], [7, 5], [6, 4], [6, 4]]

The total priority of houses on the burnt grass (Pb) and the total priority of houses on the green grass (Pg):
 [[4, 2], [8, 6], [8, 6], [12, 10], [4, 7], [9, 4], [10, 5], [3, 10], [10, 8], [8, 5], [8, 6]]

A rescue ratio of priority Pr where Pr = Pb / Pg:
 [0.5, 1.3333333333333333, 2.5, 2.6666666666666665, 2.6666666666666665, 1.6, 2.0, 3.3333333333333335, 2.0, 0.8571428571428571, 1.3333333333333333]
 
A list of the names of the input images , arranged in descending order of their rescue ratio:
 ['7.png', '3.png', '4.png', '2.png', '6.png', '8.png', '5.png', '1.png', '11.png', '10.png', '0.png']


## Documentation

Refer to the documentation below:

[Documentation](https://github.com/ScriptedLines/ForestFire_Rescue_Detector/blob/main/Documentation.docx)

