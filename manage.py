from app import create_app

manager = create_app()

if __name__ == '__main__':
    manager.run()
   # app.run(host='127.0.0.1', port=2000, debug=True)