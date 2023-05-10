# Assignment-2

Contains all files used in Assignment 2
This includes the following:

Geology.txt
Population.txt
Transport.txt
agentframework.py
geometry.py
io.py
Out.txt
model.py
README.MD
Site Suitabilty.txt

Software Licence: PD

Purpose of the software:
To identify a suitable location for a rock aggregate factory in the UK. 

Method:
The software takes into consideration three factors: geology, transport and population. 
These factors are represented as raster data. The software reads and displays this data. The data contains values with a range of 0-225. The higher the value, the more suitable the more suitable the location is for a factory. 
The software multiples each factor by a weighted factor and then adds the resulting raster together to produce an overall result output raster.
The result raster is then displayed and written to a file. 
A graphical user interface is then provided to enable to client to easily adjust the weighted values applied to each factor when considering the importance of each one. This enables them to quickly decide which factor is more important while trying to indentify a suitable location for the factory. 

How to run the software:
The software can be run by loading it into Spyder (Anaconda3) and running the Site Suitability.py file. This should provide and output raster which will be displayed as a GUI. The client will then be able to manually adjust the weighting applied to the following factors: geology, transport and population. By adjusting the weighting of each factor, a different output will be displayed by the GUI resulting in a different suitable location for the factory.

Testing:
The software was tested throughout it's development to ensure that the software still ran and that there were no errors in the code after each modication. The evidence of the code's development is found in the original source code files. Each source code file contains a history.py section which is a detailed log of the file run history. Each time the file was modified and new code was added, the file was run to ensure that it still worked. 

Limitations:
Some of the source files are unable to run successfully due to various errors in the code. 

model.py: undefined names in the source code. For example: 'neighbourhood', 'get_max_distance', 'sum_agentstores' and 'sum_environment'. Also,  Module not found error. No module named 'agentframework'.
site_suitability.py: Module not found error. No module named 'agentframework'. 
geometry.py: No errors.
agentframework.py: TypeError: 'Agent' object is not subscriptable.

These issues were encountered during development and unfortunately they are unresolved. Therefore, the code does not run as expected and there is no final output. 


