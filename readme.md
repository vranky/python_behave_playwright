Local
* virtualenv -p python3 python_3_9
* source python_3_9/bin/activate
* python3 -m pip install -r requirements.txt
* python3 -m playwright install
* DEBUG=pw:api behave -D ENV=test --tags @wip -f allure_behave.formatter:AllureFormatter -o report/allure-results

Docker 
- docker build --tag at-tests-10.0 .
- docker run --tty at-tests-10.0:latest behave
  