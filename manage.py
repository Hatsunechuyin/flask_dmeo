from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
   # app.run(host='127.0.0.1', port=2000, debug=True)