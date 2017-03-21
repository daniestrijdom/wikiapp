wikiapp README
==================

wikiapp is a single page web app that scrapes the table of contents from wikipedia for specified search terms

Getting Started
---------------

- cd <directory containing this file>

- $VENV/bin/pip install -e .

- $VENV/bin/pserve development.ini --reload

If serving on your local machine, navigate to localhost:6543 in your browser.

Example
-------

- Type a search term into the text input.
- Click 'Submit' or press Enter
- After seeing your result, click on 'Reset' to go back to initial state or search again.

Example output

![alt tag](https://github.com/daniestrijdom/wikiapp/blob/master/example.PNG)
