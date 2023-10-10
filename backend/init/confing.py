import os
import re
import yaml
from dotenv import load_dotenv
from core.architecture import Singleton


class Config(metaclass=Singleton):
    def __init__(self, config_file_path: str = None):
        """
        Initializes a configuration manager using a YAML configuration file.

        Args:
            config_file_path (str): Path to the YAML configuration file.
        """

        load_dotenv()
        self.__env_tag = "!ENV"
        self.__env_pattern = re.compile(".*?\${(\w+)}.*?")
        self.__parse_config(config_file_path or os.path.join("resources", "config.yml"))

    def get_param(self, param: str, as_type: type = None):
        """
        Get a parameter from the configuration using dot-separated keys.

        Args:
            param (str): Dot-separated parameter key (e.g., "section.subsection.param").
            as_type (type, optional): The desired data type of the retrieved parameter.

        Returns:
            object: The value of the requested parameter.
        """

        tree = param.split(".")
        value = self.config
        for key in tree:
            value = value[key]
        if as_type:
            value = as_type(value)
        return value

    def __parse_config(self, path):
        """
        Load a YAML configuration file and resolve any environment variables.
        Environment variables must have !ENV before them and be in this format: ${VAR_NAME}.

        Args:
            path (str): Path to the YAML configuration file.
        """

        loader = yaml.SafeLoader

        loader.add_implicit_resolver(self.__env_tag, self.__env_pattern, None)
        loader.add_constructor(self.__env_tag, self.__constructor_env_variables)

        with open(path) as conf_data:
            self.config = yaml.load(conf_data, Loader=loader)

    def __constructor_env_variables(self, loader: yaml.loader, node):
        """
        Extracts the environment variable from the node's value.

        Args:
            loader (yaml.loader): YAML loader.
            node (yaml.nodes.ScalarNode): Scalar node containing a string with environment variables.

        Returns:
            str: The resolved value with environment variables replaced.
        """

        value = loader.construct_scalar(node)
        match = self.__env_pattern.findall(value)
        if match:
            full_value = value
            for g in match:
                full_value = full_value.replace(f"${{{g}}}", os.environ.get(g, ""))
            return full_value
        return value
