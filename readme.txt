Matrix Selenium - Home Exam
==============================

A file structure template, development environment and rule set for python home exam project.

News Storage System Documentation – Matrix
------------

Structure
------------

The project is designed in an OOP manner like requested.
Base Class – BaseExtractor.py
Child Classes – FlightExtractor.py, NewsExtractor.py
Summarizer.py - Used for NLP model to summarize the BBC articles
Constants.py - Constants for classifying type of header and content in NewsExtractor.

The BaseExtractor class inherits the Selenium Web driver object (self), so for every class that inherits BaseExtractor
it has all the functionality of the web driver.

Solving the exercise
------------

In order to solve the extraction problem (getting the data) I used a chrome extension called XPath Helper.
This extension allows me to write a XPath query and highlights the query results on the website.
After checking the structure of both website – BBC and IAA I have constructed the relevant functions in the base class
of my extractor by using get by XPath methods.

Core code components
------------

BaseExtractor inherits from the web driver and given binaries and web driver path can work properly.
In order to get the data without errors I had to configure an Options object from the Selenium package.
Option 1 – Running on headless mode: this enabled my code to run faster as there was no need to load the GUI of Firefox.
Option 2 – Binary location need to be specified to the options object in order for it to work.
In addition, for not missing any data I had to make sure the window opened is maximized
(and prevent errors regarding the extractions).

For every function from the Selenium package, I used the "good practice" WebDriverWait object in order to wait for web
elements to load properly then extract them.
For example in the FlightExtractor I had to make sure I was getting all the tables of the flights so I needed to exhaust
the show more flights button until its gone then scrape the data.
In short – for each function I used from Selenium I used WebDriverWait and passed the return value to the class calling
it for "good practice" and getting the required data.

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>