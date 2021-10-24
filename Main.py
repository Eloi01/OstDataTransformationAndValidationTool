import Controller
import pathlib

input_path = pathlib.Path(r'InputData\Output_Hermann_Preprocessing.json')
configuration_path = pathlib.Path(r"InputData/ConfigurationFiles/Configuration.xml")
output_path = pathlib.Path(r"Output\PythonTestFile.json")
log_output_path = pathlib.Path(r'Output\PythonTestFile_LOG.txt')
log_failed_items_path = pathlib.Path(r'Output\FailedItems_LOG.txt')

if __name__ == "__main__":
    """Starts the transformation and validation process."""
    Controller.start_tool(input_path, configuration_path, output_path, log_output_path, log_failed_items_path)
