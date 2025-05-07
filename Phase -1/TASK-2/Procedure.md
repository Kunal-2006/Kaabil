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
    
