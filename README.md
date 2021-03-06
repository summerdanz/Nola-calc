## Local Development Instructions

### Machine configuration:

* If you don't have Homebrew, install it- terminal (anywhere)

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

* Install Node/npm - terminal (anywhere)

`brew install node`

* if Github is not configured:

  first step: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/

  second step: https://help.github.com/articles/connecting-to-github-with-ssh/

* Clone repository

`git clone https://github.com/summerdanz/Nola-calc.git`

* Install dependencies-terminal (inside project root)

`cd Nola-calc`

`npm install`

* Install dependencies- terminal (inside fullstack_template/static)

`npm install`

* Install python3 - terminal (anywhere)

`brew install python`

* Use pip (comes with python) to install pipenv

`pip3 install --user pipenv`

`sudo pip3 install virtualenv`

*  intall dependencies (`cd fullstack_template/server`)

`pipenv install requests`

* activate virtual environment (inside fullstack_template/server)

`pipenv shell`

* install flask (inside fullstack_template/server)

`pip3 install flask`

* install flask_cors (inside fullstack_template/server)

`pip3 install flask_cors`

--


### To run local development environment:

* inside fullstack_template/static:

`npm run watch`  (ctrl + c to stop)

* In a new terminal window, inside fullstack_template/server:

`python3 server.py`

* find project at `localhost:5000`

** make sure cookies are disabled on this url in Google Chrome


### Resources

* tutorial for setup: https://codeburst.io/creating-a-full-stack-web-application-with-python-npm-webpack-and-react-8925800503d9
* component library: https://www.material-ui.com/#/
* setup flask: http://flask.pocoo.org/docs/0.12/installation/
* problems setting up flask: https://stackoverflow.com/questions/31252791/flask-importerror-no-module-named-flask?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
* helpful hints: https://github.com/klaseskilson/react-flask-todilo
