#-----------------------------------------
# main2.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
 return render_template('hello.html')

@app.route('/book/')
def book():
 return render_template('book1.html')



if __name__ == "__main__":
 app.run()
#----------------------------------------
# end of main2.py
#----------------------------------------- 
