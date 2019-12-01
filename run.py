#!ambapi/bin/python

from app.app import create_app

if __name__ == "__main__":
    print('Enter...')
    application = create_app()
    application.run()
