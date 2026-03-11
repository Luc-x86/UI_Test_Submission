# Setup

Download PyCharm onto your PC if you have not already using the following link: https://www.jetbrains.com/pycharm/download/?section=windows
Once you have installed the required software, open PyCharm
Open the project file in Pycharm
Open the PyCharm terminal and type the following commands:
 		- pip install pytest-playwright
 		- playwright install

# Running

To run the test, open the terminal and run the command "pytest"
The test should run in headed mode by default, to change this, edit the "browser = firefox.launch(headless=False)" in the conftest file to say headless=True

# Assumptions

This test assumes you have a stable internet connection and the website is able to respond before timeouts occur.

# Tradeoffs

Theses tests currently do not run in terminal as it needs to be run in order to create the required data needed across all tests.

# Improvements if given more time

If given more time this test would also close browser windows before opening the next test.
