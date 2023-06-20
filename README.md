Intern Management System:
This is a simple Flask application that serves as an Intern Management System. It allows you to register interns, retrieve all interns, edit intern details, delete interns, search for interns, and sort interns based on different criteria. The application uses a RESTful API design and in-memory data storage.

Installation:
1.Clone the repository:
  git clone https://github.com/your-username/intern-management-system.git

2.Navigate to the project directory:
  cd intern-management-system

3.Create a virtual environment (optional but recommended):
  python3 -m venv venv

4.Activate the virtual environment:
  
-On macOS and Linux:
  source venv/bin/activate

-On Windows:
  venv\Scripts\activate 

5.Install the required dependencies:   
  pip install -r requirements.txt


Usage:

1.Start the Flask application:
  python app.py

2.Access the API endpoints using a tool like cURL, Postman, or a web browser.

API Endpoints:
Register a new intern:
-Endpoint: "/interns"
-Method: POST
-Payload:

{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "start_date": "2023-06-01",
    "end_date": "2023-09-01"
}

-Response:

{
    "message": "Intern registered successfully"
}

Retrieve all interns:
-Endpoint: "/interns"
-Method: GET
-Response:

{
    "interns": [
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "start_date": "2023-06-01",
            "end_date": "2023-09-01"
        },
        {
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "start_date": "2023-07-01",
            "end_date": "2023-10-01"
        }
    ]
}

Edit intern details 
-Endpoint: "/interns/<email>"
-Method: PUT or PATCH
-Payload:

{
    "name": "John Doe",
    "start_date": "2023-06-15"
}


-Response:

{
    "message": "Intern details updated successfully"
}


Delete an intern
-Endpoint: "/interns/<email>"
-Method: DELETE
-Response:

{
    "message": "Intern deleted successfully."
}

Search for interns: 
-Endpoint: "/search?query=<search_query>"
-Method: GET
-Response:

{
    "interns": [
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "start_date": "2023-06-01",
            "end_date": "2023-09-01"
        }
    ]
}


Sort interns:
-Endpoint: "/sort?sort_by=<field>"
-Method: GET
-Response:

{
    "interns": [
        {
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "start_date": "2023-07-01",
            "end_date": "2023-10-01"
        },
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "start_date": "2023-06-01",
            "end_date": "2023-09-01"
        }
    ]
}


Contributions are welcome! If you find any issues or want to enhance the Intern Management System, feel free to open a pull request.
