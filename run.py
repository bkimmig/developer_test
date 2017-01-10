from app import app

# Run a local test server.
# Import the app from the init of the application

if __name__ == "__main__":
    app.run(debug=True, port=3000)