The Readme woo! 


pip install -r requirements.txt


To use wordnet, you have to download the wordnet corpus from nltk. To do this, first make sure you ran pip install -r requirments.txt. Then run the python interpreter in the command line. Type these lines:
    import nltk
    nltk.download()
A graphical nltk downloader will open.
Click on the second tab ('Corpora'). Scroll down and look for wordnet. Double click on wordnet and it will install. Exit the GUI and exit the python interpreter.

To run our program from within the source directory, simply run python Findpuns.py

The output is the number of puns incorrectly classified.
