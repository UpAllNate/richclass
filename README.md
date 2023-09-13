# RichClass: Python classes for simplifying

RichClass is a collection of python classes that aim to rapidly bridge the gap between verbose code and creating feature rich objects with common sense features. The flagship class for this package's release being RichPath, a class that builds on the pathlib.Path class which includes a method detect() which returns True if the directory or file exists. 

# Classes
## RichPath
This class simultaneously maintains both attributes:
* path_str... the path represented as a string
* path_obj... the path represented as a pathlib.Path object

Several additional attributes are available:
* **self.type** of a type enumerated by RichPathTypes
* **self.logger** The value is None by default, or a Logger class object if passed at initializing
* **self.logging_en** True if the RichClass initializing method is passed a Logger class object
* **self.required** If true, will raise a FileNotFoundError exception on failed self.detect()

Several methods are available for a class instance of RichPath:
* **detect** searches for the existence of the directory or file specified in the RichPath object and returns bool result
* **update_path_str** allows you to update the path of the RichPath object with a directory or file string
	* Calls self.detect() and returns bool result
* **update_path_obj** allows you to update the path of the RichPath object with a pathlib.Path class object
	* Calls self.detect() and returns bool result

