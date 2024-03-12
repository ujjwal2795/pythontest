# pythontest
pythontest
To run the application, you need to follow these steps:

Create a Virtual Environment (Optional):
Open a terminal or command prompt in the project root directory.
Run the following commands to create and activate a virtual environment:

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install Dependencies:
While the virtual environment is active, install the required dependencies (Flask) using the following command:
pip install -r requirements.txt

Run the Application:
Execute the following command to run the Flask application:
python app/app.py

This will start the Flask development server, and you should see output indicating that the server is running.

Access the Application:
Open a web browser and go to http://127.0.0.1:5000/. You should see the "Hello, World!" message.

Run Unit Tests:

While the Flask application is running, open a new terminal and run the unit tests:
python app/tests/test_app.py
The tests should run, and you'll see the output indicating whether they passed or failed.
