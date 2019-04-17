## Movie Trailer Website
This website is developed as a project of [Full Stack Web Developer Nanodegree Program](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004/), offered by [Udacity](https://www.udacity.com/).

#### Dependencies
This project requires [Python](https://www.python.org/) 3.x to run. Please make sure you have the latest version of [Python](https://www.python.org/) installed in your system. If not, follow this [guide](https://www.python.org/about/gettingstarted/) to install [Python](https://www.python.org/) to your system.

#### What's included
The project folder consists of four files:
* **entertainment_center.py** This file contains all the data and function calls required to run the website.
* **fresh_tomatoes.py** This file contains all the logic required to generate a HTML file, which can be run in browser.
* **media.py** This file contains all the class definitions used in this project.
* **README.md**

#### How to run?
* Make sure you satisfy all the **Dependencies** mentioned above.
* Download the project folder.
* Open your terminal, and navigate to the root of the project folder.
* Run the following command in your terminal:

 `python -m entertainment_center.py`

* A browser window will open and load the movie trailer website in a new tab.

#### How it works?

When you run `python -m entertainment_center.py` in your terminal, the code inside the file entertainment_center.py gets executed, which calls a function inside the file fresh_tomatoes.py, which then generates a HTML file, and loads it in the browser window.

#### How to make changes?


To make changes like adding/deleting/modifying Movies or Tv Shows, edit the entertainment_center.py file. It is very simple to understand. I recommend you to go through the whole file, read through the code and comments, and once you have understood it, you will be able to easily modify it.

To make changes to style, look and feel of the website, you will have to modify the file fresh_tomatoes.py, It contains the template for the HTML file, and the functions to append the data from the file entertainment_center.py dynamically to the generated website. The code in fresh_tomatoes.py is well commented and fairly easy to understand it. You will be able to make changes to it once you understand it.

To make changes to the class structure, edit the file media.py. Once again, this file is well commented. You will be able to make changes to it after you understand it.
