## 1.
  Here before starting the required work we will have to install ROS2 and make the enviroment and to other work so before starting this is the procedure.
  ### Step 1
    Check for Locale if it supports UTF-8
    UTF-8 means Unicode which considers 8 bit width used for communication So to install it enter the given code in the terminal
    
    
    locale  # check for UTF-8
    sudo apt update && sudo apt install locales
    sudo locale-gen en_US en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    export LANG=en_US.UTF-8
    locale  # verify settings  
    By the above code you can setup Locale.

  ### Step 2
    We will need to add ROS 2 but before that we will need to add an Universe Repositariy which have the cabability to check the authenicity of the ROS@  such that tampering.
    
    
    sudo apt install software-properties-common
    sudo add-apt-repository universe
    sudo apt update && sudo apt install curl -y
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee        /etc/apt/sources.list.d/ros2.list > /dev/null
  ### Step 3
    Installing ROS2 Packages needed but before that we will have to first update our system and upgrade our ubuntu software so
    sudo apt update
    sudo apt upgrade
    Here we will install the desktop version of the ROS since i have done dual boot of my computer.
    sudo apt install ros-humble-desktop
  ### Step 4
    Setting up the Enviroment of ROS2 since when you type ROS2 in the terminal you will get an error as command not found hence to avoid this we will have to first to enter the enviroment of ROS2 which we have downloaded first and to enter the enviroment we will have to each time in a new terminal need to write 
    
    source /opt/ros/humble/setup.bash
    But this can be repetititve hence to avoid this we can just open the hidden file of the ROS and at the end we can just write the code used above to do this process.
    
    Open a new terminal and write
    gedit ~/.bashrc
    
    after opening the editor and the last line after 117 at 118 write the code
    source /opt/ros/humble/setup.bash
    So now we dont to repetively enter the source /opt/ros/humble/setup.bash this whenever we need to use the ROS2 program codes since we have created the enviroment for it as default now in our terminal.
## 2.
  Here we will be simulating subscriber and publisher such that here the publisher will be publishing the data here we will be publishing Hello world with an interval of 1 sec multiple times and the suscriber will taking the message form the publiher and printing the meage we will seeing the connnection of each other by the azure graph feature to visualize the connection between each node.
  ### Step 1.
    here we will be running an talker node which will be acting as an publisher node it can activated by the code.
    ros2 run demo_nodes_cpp talker
  ### Step 2.
    In a new terminal here we will be running an subscriber node which will act as an listener node it will be activated by the code given.
    ros2 run demo_nodes_cpp listener
  ### Step3.
    Now in a new terminal we will use rqt grapgh to showcase the connection between the nodes in an graphical manner.
    rqt_graph
  ### Step Fun.
    Here we can create an turtle mapping system which can be directed with the help of the directions provided by the user which will act as an publisher and the screen showing turtle will move according the to the commands will act as an subscriber.
    ros2 run turtlesim turtlesim_node
    
    In a new terminal we will type 
    ros2 run turtlesim turtle_teleop_key
    and we can visualize the nodes connection by writing in an new terminal rqt_graph
## 3.
  Here we will creating an workspace in the terminal so we will be installing colcon for our workspace.
  ### Step1.
    sudo install colcon
    sudo apt  install python3-colcon-common-extensions
    here we will be installing colcon which is essential for managing software packages.
  ### Step2.
    Here we first go into the directory.
       cd /usr/share/colcon_argcomplete/hook/
      If we find the files present in the directory we will find the file as colcon-argcomplete.bash.
      first edit the bash file by gedit ~/.bashrc and copy paste the path of the file
        gedit ~/.bashrc
        cd /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
  ### Step3.
    Now we will create an src folder or an source folder in our workspace but before that we will create an directory of our workspace
      mkdir ros2_ws
    And in the workspace we will create an directory src
      mkdir src
    now in the workspace we will build our workspace with the help of colcon by the command
      colcon build
    now when we will check the list of directories present in the workspace we can see multiple directories.
  ### Step 4.
    Now we will open install folder and when all directories are listed we can see that there are mutiple directories where we can see one as setup.bash so we will source setup.bash to the original bash script such that workspace can be accesesed and it can recognize all the ros2 packages.
      source ~/ros2_ws/install/setup.bash
    copy this in the gedit ~/.bashrc
    hence workspace created.
## 4.
  Here now since workspace is correctly configured now we need to just initiate our package.
  Packages help us to compile our code in a better way.Since once package is created we can create node inside the package and start with actual coding.
  ### Step1.
    So first we will go in our worksapce directory which we have created as ros2_ws and go in the src sub directory of it by the code 
      cd ros2_ws
      cd src
  ### Step2.
    Now we will create our package by the name of my_robot_controller where we will specify it as an python package so we will use rclpy as an python library
      ros2 pkg create my_robot_controller --build-type ament_python --dependencies rclpy
    when seen the list of directories in the src directory we can see an new directory as the name of the package created as my_robot_controller
  ### Step 3.
    Now we will  install visual Studio because it will help in writing the python scripts needed for the nodes.
      sudo install code --classic
      code .
  ### Step 4.
    Now we will build our workspace in ros2_ws by the same command used colcon build
      colcon build
## 5.
  Objective to create an Node which act as an publisher which created in ROS2 with the help OOPS in Python program.
  ### Step1.
    To create an directory inside of the directory of my_robot_controller by the same name and in the new directory an new pyhton file is creted as the name of my_first_node.py and make it executable and edit the code.
      touch my_first_node.py
      chmod +x my_first_node.py
      code .
      ./my_first_node.py
    Install the ROS library in VS code for the ability to run the codes.
    after writing the code use the command ./my_first_node.py to run the code
  ### Step 2.
    install the Node so for installation we will go in vs code and open the setup/py and put the required in code in the test_node.and do colcon build in the ros workspace.
# 5.
  ## Step 1.
  
    
      
    
      
      

      




    
