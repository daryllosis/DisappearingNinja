from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninjas.html', myimage = "static/images/tmnt.png")


@app.route('/ninja/<color>')
def ninjaColor(color):
    if color == "red":
        myimage = '/static/images/raphael.jpg'
    elif color == "blue":
        myimage = "/static/images/leonardo.jpg"
    elif color == "orange":
        myimage = "/static/images/michelangelo.jpg"
    elif color == "purple":
        myimage = "/static/images/donatello.jpg"
    else:
        myimage = "/static/images/notapril.jpg"
    return render_template('ninjas.html', myimage = myimage)





if __name__ == "__main__":
    #run our server
    app.run(debug=True)




        #     {% if color == "red" %}
        #     <img src="{{url_for('static', filename='images/raphael.jpg')}}">
        # {% elif color == "orange" %}
        #     <img src="{{url_for('static', filename='images/michelangelo.jpg')}}">
        # {% elif color == "purple" %}
        #     <img src="{{url_for('static', filename='images/donatelo.jpg')}}">
        # {% elif color == "blue" %}
        #     <img src="{{url_for('static', filename='images/leonardo.jpg')}}">
        # {% else  %}
        #     <img src="{{url_for('static', filename='images/notapril.jpg')}}">
        # {% endif %}