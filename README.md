# Niryo
 
### The folders are divided into the several functionalities of Ned and Use Cases we have tried out for the Niryo Robot


1. Ned_API examples:
   - Vision conditioning conveyor belt
2. Ned ROS applications:
   - Simulations:
        - Webots
        - Moveit
        - Gazebo
   - Use Cases
   
   
 ## General Points to Consider when setting up the Ned Robot:
 
 Since we used the ros melodic version for setting up the niryo robot the respective ubuntu version, needed to be installed on the remote pc. This was of the ubuntu version 18.04.
 
 The Ned 1 package comes with a ready assembled robot. Depending on the application, there might be specific setups needed. However these will be described carefully in each application at the readme file. Therefore the software steps needed for ned 1 will be listed here:
 
 1. First it is highly adviced to install the niryo studio related to the operating system of the computer and the version of the niryo robot on this website: https://niryo.com/download/ 
 
 Once installed you can find the ip address of the robot by clicking on the magnifier as shown on the figure below.
 <img src="images/magnifier.png" width="300" height="200">
 
 
 After clicking on the magnifier you can see the options from the dropdown menu and also the ip address of the robot which you want to connect to.
 <img src="images/pop_up_ip_address.png" width="300" height="200">
 
 2. Once you are connected to the niryo robot, there should be a 3D CAD physical model that should be visible on the studio. If there is a camera plugged into the robot via usb, then this should also appear under "Camera Streaming". This you can see next to the "3D View" tab.
 <img src="images/connected_ip_address.png" width="300" height="200">
 
 3. Afterwards, if you would like to work on the niryo studio itself, you can see the figure below on which there are many options to program the robot via a GUI interface. 
 <img src="images/niryo_studio_frontend.png" width="300" height="200"> 
