from app import create_app

app = create_app()

if __name__ == '__main__':
    #TODO: Remove debug=True in production
    app.run(debug=True)