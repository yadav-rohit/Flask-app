from website import app

# --Dev Environment Settings --------------------------------#

if __name__ == '__main__':
    INTERFACE = app.config['INTERFACE']
    PORT = app.config['HTTP_PORT']
    DEBUG = app.config['DEBUG']
    app.run(host=INTERFACE, port=PORT, debug=DEBUG)

# --Production Environment Settings ---------------------------#
