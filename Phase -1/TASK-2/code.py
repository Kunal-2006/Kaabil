"""This is the base Code frame to create an Node such that is can communicate"""
#!/usr/bin/env python3
import rclpy"""The library which is imported for the ROS usage with the help of python"""

def main(args=None):
  rclpy.init(args=args)"""Starts the ROS communication"""

  #
  """The whole Node will created inside """

  rclpy.shutdown()"""Stops the ROS communication"""
if __name__ =='__main__':
  main()
##############################################################################################################
"""This is the code to print Hello World """
#!/usr/bin/env python3
import rclpy"""The library which is imported for the ROS usage with the help of python"""
from rclpy.node import Node

class MyNode(Node):"""class can have access to ROS2"""
  def __init__(self):
      super().__init__("first_node")    """first node is the node name used"""
      self.get_logger().info("Hello from ROS2")   """The message which is going to get printed"""
def main(args=None):
  rclpy.init(args=args)"""Starts the ROS communication"""
  node=MyNode()
  rclpy.shutdown()"""Stops the ROS communication"""
if __name__ =='__main__':
  main()
#############################################################################################################
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback) """created a timer by which after 1 second it will print Hello"""

    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_)) """ print Hello and the nummber of the times hello printed with the help of concatanation.
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()



  
