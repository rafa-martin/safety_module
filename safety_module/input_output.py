from rclpy.node import Node
from robotnik_msgs.msg import InputsOutputs
import yaml


class InputOutputNode(Node):
    def __init__(self):
        super().__init__("safety_module_node")
        self.get_logger().info("starting node")
        self.__read_params()
        self.__setup()

    def __read_params(self):
        """
        This method is used to read the parameters from the parameter server
        """
        # config_file[String]: Path to the configuration file
        self.declare_parameter("config_file", "")
        config_file = (
            self.get_parameter("config_file").get_parameter_value().string_value
        )
        self.__config = yaml.safe_load(open(config_file, "r"))
        self.get_logger().info(f"Loaded config: {self.__config}")

    def __setup(self):
        """
        This method is used to create the publishers and subscribers
        """
        self.__io_sub = self.create_subscription(
            InputsOutputs, "~/io", self.__io_callback, 10
        )

    def __io_callback(self, msg: InputsOutputs):
        """
        This method is called when a new InputsOutputs message is received
        """
        self.get_logger().info(f"Received InputsOutputs message: {msg}")
