# CharterHacks-Project

Installations and other Guidelines
-> Create a conda env with python version 3.7.5 using command
    conda create -n charterhacks python=3.7.5 anaconda

-> Select the interpreter in this conda env in VSCode
    >Bottom left of screen it'll show something like Python 3.x.x - click on this and a select interpreter menu should open up - select the Python 3.7.5 64-bit ('charterhacks': conda) interpreter (make sure this is the one being used everytime you open up the project!)
    >In the terminal window where you get your outputs, make sure the line starts with (charterhacks) C:\
        **If it isnt like this, in the terminal type 
            conda activate charterhacks

-> To test the GUI code, you will have to install the framework Kivy, and all it's dependencies, pip install   all dependencies from - https://kivy.org/doc/stable/installation/installation-windows.html
    Use the pip install commands in the terminal in VSCode after making sure step 2 (the one above this) is complete
    
->Put all code files you make in Scripts, and any images/fonts/sounds that we'll need in Resources.