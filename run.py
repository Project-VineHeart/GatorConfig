"""
# run.py
This script is the entry point for running the Flask application.
# It initializes the application and starts the server.
"""
from app import app


def main():
    """
    Main function to run the Flask application.
    """
    host = '0.0.0.0'
    port = 5000
    debug = False
    # Uncomment the line below to enable debug mode
    # debug = True
    
    app.run(host=host, port=port, debug=debug)

   
if __name__ == '__main__':
    main()