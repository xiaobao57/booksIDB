#-----------------------------------------
# main.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
 return render_template('hello.html')

@app.route('/about')
def about():
 return render_template('about.html')

###NEeed to delete
#----------------------------------------
# Test Nav
#----------------------------------------

@app.route('/navtest')
def navtest():
 return render_template('navtest.html')
 
#----------------------------------------
# Books
#----------------------------------------

@app.route('/sorcerors-stone/')
def sorcerors_stone():
 return render_template('sorcerors-stone.html')

@app.route('/mistborn/')
def mistborn():
 return render_template('mistborn.html')

@app.route('/all-the-pres-men/')
def all_the_pres_men():
 return render_template('all-the-pres-men.html')


#----------------------------------------
# Authors
#----------------------------------------

@app.route('/jk-rowling/')
def jk_rowling():
 return render_template('jk-rowling.html')

@app.route('/brandon-sanderson/')
def brandon_sanderson():
 return render_template('brandon-sanderson.html')

@app.route('/carl-bernstein/')
def carl_bernstein():
 return render_template('carl-bernstein.html')

#----------------------------------------
# Publishers
#----------------------------------------

@app.route('/pottermore/')
def pottermore():
 return render_template('pottermore.html')

@app.route('/simon-schuster/')
def simon_schuster():
 return render_template('simon-schuster.html')

@app.route('/palgrave-mac/')
def palgrave_mac():
 return render_template('palgrave-mac.html')

if __name__ == "__main__":
 app.run()
#----------------------------------------
# end of main.py
#----------------------------------------
