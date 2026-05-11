#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    
    def __init__(self):
        super().__init__("py_test") 
        '''Using the parent constructor - super to initialise the node by giving it 
           the name 'py_test'.'''
        self.get_logger().info("Hello World!")
        self.counter = 0
        self.create_timer(1.0,self.timer_callback)
        '''create_timer is a standard function that requires two parameters, one is the time
           interval and another is the function that has to be executed.'''

    def timer_callback(self):
        self.get_logger().info(f"Hello {self.counter}")
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    #spin is a standard function that allows a node to process any callback(s).
    rclpy.shutdown()

if __name__ == "__main__":
    main()
''' For running the 'python3 my_first_node.py' from the destination of the file. 
Unlike C, python requires the standard entry block point to check if the file is file being 
run by the user. If yes, it runs main(), else it is imported as a library.'''

'''To avoid going to the destination of the file and executing the file uisng the command 
'python3 NAME.py', we go to the 'setup.py' file and enter the instructions in entry points 
to create a new executable file.'''