DC Assignment - 2

The assignment is based on using Hadoop Framework to process big data efficiently.

The selected dataset for this assignment was OpenImages Dataset (https://github.com/openimages/dataset), where I selected two CSV files:

	1. images.csv (https://storage.googleapis.com/openimages/2017_11/images_2017_11.tar.gz) (990 MB compressed, 3.5 GB on expansion).
	2. annotations-machine.csv (https://storage.googleapis.com/openimages/2017_11/annotations_machine_2017_11.tar.gz) (447 MB compressed, 3 GB on expansion).

Below, there is a description for each of the CSV files:

	1. images.csv: Contains the fields ImageID, Subset, OriginalURL, OriginalLandingURL, License, AuthorProfileURL, Author, Title, OriginalSize, OriginalMD5, Thumbnail300KURL.
	There are three CSV files of the same name for each train, test and validation. The fields used for tasks are Author, Title and ImageID.

	2. annotations-machine.csv: Contains the fields ImageID, Source, LabelName, Confidence.
	There are three CSV files of the same name for each train, test and validation. The fields used for tasks are ImageID, LabelName and Confidence.

The tasks are:

	Task 1. Most prominent author in terms of image published in a category. (images.csv)
 	Task 2. Image(s) represented by a subset of categories. (annotations-machine.csv)
 	Task 3. Group images based on occurrence of a particular string. (For example, image titles having “bus” in their display names) (images.csv)
 	Task 4. Getting true positives from the labeled images based on confidence score (The higher the confidence, the smaller chance for the label to be a false positive. Hence, selecting higher thresholds to get true positives) (annotations-machine.csv)

Note: Confidence Score are given as these are machine annotations and range from 0.00 to 1.00. It represents the probability of an image to belong in a particular category.

Requirements:

	1. Java Development Kit
	2. Hadoop Framework
	3. Python2
	4. mrjob (Python Dependency) (Installed using ``sudo pip install mrjob`` in Terminal)

Notes/Attempts:

	1. Hadoop Configuration took a lot of time as there were multiple files to be configured like core-site.xml, hdfs-site.xml etc.
	2. Configuration plays an important role in execution of the codes.
	3. mrjob is a simple wrapper for mapper.py and reducer.py when used with hadoop-*streaming*-.jar file (available within Hadoop Framework). Individual mapper.py and reducer.py files can be written for each individual task to reduce dependency on mrjob.

Code Details:

	Each code has comments for each of the sections and functions.

Running the Code:

	To run each of the tasks, the below steps need to be followed:

		1. Put images.csv and annotations-machine.csv in HDFS by executing the below command:

			``hdfs dfs -put images.csv/annotations-machine.csv /path/to/hdfs/``

		2. To run each of the tasks with Hadoop, execute the following command:

			``python task[1/2/3/4].py -r hadoop hdfs://path/to/hdfs/filename.csv``

Sample Outputs:

	I have a uploaded a folder with sample outputs of each task.
