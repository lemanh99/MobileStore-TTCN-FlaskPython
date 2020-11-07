from shop import app
app.config['SECRET_KEY'] = 'any secret string'



if __name__=="__main__":
    app.run(debug=True)