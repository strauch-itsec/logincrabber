# Flask Login JSON App

This project is a simple Flask application that provides a login form and saves the entered user data to a JSON file. It also includes a second page that displays the saved user data.

## Project Structure

```
flask-login-json-app
├── app.py                # Main entry point of the Flask application
├── requirements.txt      # Lists the dependencies required for the project
├── data
│   └── users.json       # Stores user data in JSON format
├── templates
│   ├── login.html       # HTML code for the login form
│   └── users.html       # Displays the saved user data
└── README.md            # Documentation for the project
```

## Requirements

To run this application, you need to have Python and Flask installed. You can install the required packages using the following command:

```
pip install -r requirements.txt
```

## Running the Application

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the application using the command:

```
python app.py
```

4. Open your web browser and go to `http://127.0.0.1:5000` to access the login form.

## Usage

- Enter your details in the login form and submit.
- The entered data will be saved to `data/users.json`.
- You can view the saved user data by navigating to the appropriate page in the application.

## License

This project is open-source and available under the MIT License.