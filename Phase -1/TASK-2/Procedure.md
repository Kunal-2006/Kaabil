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
    rose2 run turtlesim turtle_teleop_key
    
