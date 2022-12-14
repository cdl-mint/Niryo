# Application exemples: Vision tic tac toe

Documentation from the official niryo website is available [here](https://niryo.com/docs/niryo-one/niryo-one-industrial-demonstrators/vision-tic-tac-toe/).

There were several modifications we did on the Tic-Tac-Toe software of Ned:

1. The exemplary python code for the Tic-Tac-Toe game was modified such that the tokens were taken from the sides of the playing field and not from a stack.
2. The tokens used did not belong to the accessories provided by the Niryo company but rather were our own. See picture:  Since they were easier to pick up with the vacuum pump. 
3. The lightning settings were not modified software wise but since we worked with the robot under 



For getting started with playing the Tic-Tac-Toe, make sure to know the ip address of the niryo robot, this you can find via the general description of setting up the niryo robots at the beginning of the Niryo folder.

Afterwards pull the code from this folder and run the "tictactoe_vision.py" code on any python editor you wish. What is important is that the pyniryo package is installed via: pip install pyniryo

Things to change in the code itself: 
- the ip address (tictactoe_vision.py  line 14)
  - Data which needs to be changed in the tic_tac_toe_config.yaml file:
     - workspace of the niryo robot (this is done via calibration of the visual set)
     - observation pose (this position should contain all landmarks inside of the vision)


In order to change the workspace make sure to mount the tip on to the robot as shown on figure:
<img src="images/calibration_tip.jpeg" alt="Logo" width="300" height="200">
     
In order to change the configurations on the yaml file please see the readme file at the beginning of the Niryo readme file


Furthermore, please see this youtube link on our CDL-MINT channel. It is a demonstration that was presented at the Haus der Industrie in Vienna : Youtube Link: [[https://www.youtube.com/channel/UC4Gn8bjBU00AME4R17MIqgA](https://www.youtube.com/watch?v=NVb2YjT2sRI)](youtube channel)


