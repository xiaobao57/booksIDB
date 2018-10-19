#-----------------------------------------
# main1.py
# creating flask application with
# templates
#-----------------------------------------
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
 return render_template('hello.html')
if __name__ == "__main__":
 app.run()
#----------------------------------------
# end of main1.py
#----------------------------------------- 
