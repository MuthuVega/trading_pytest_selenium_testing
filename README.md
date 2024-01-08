# OANDA trading testing using pytest and selenium
Test framework built using selenium and python to test OANDA frontend trading and v20 REST API endpoints.

For the frontend testing , a Page Object Model has been built for the login page.
For REST API testing , a trading API class has been developed with the generic methods and are called from the tests.

The tests are run on GitHub actions and the test results uploaded as test artifacts.

# Set up

`pip install -r requirements.txt`

# Notes

You will need your own DEMO user credentials to run the tests locally.

Create an environment variable named OANDA_DEMO_API_KEY and store the API key to run the REST API tests locally.
