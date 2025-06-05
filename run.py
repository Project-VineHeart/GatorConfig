from app import app


def main():
    host = '0.0.0.0'
    port = 5000
    debug = True
    
    app.run(host=host, port=port, debug=debug)

   
if __name__ == '__main__':
    main()