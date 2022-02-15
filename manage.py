from main import app
if __name__ == '__main__':
    app.run(debug=True,port=2990)

app = create_app('production')