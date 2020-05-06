from application import app, db
from flask import render_template, request, Response
import requests
from application.models import Prize

@app.route('/', methods=['GET'])   
def home():
#    three_lower = requests.get('http://application2:5001/generator/three_lower')
#    get_sixdig = requests.get('http://application3:5002/generator/sixdig')
#    username = three_lower.text+str(get_sixdig.text)
#    return render_template('home.html', title='home', username=username)

# second iteration
    two_upper = requests.get('http://application2:5001/generator/two_upper')
    get_eightdig = requests.get('http://application3:5002/generator/eightdig')
    username = two_upper.text+str(get_eightdig.text)
    return render_template('home.html', title='home', username=username)

# first iteration
@app.route('/prize/<prizeusername>', methods=['GET', 'POST'])
#def prize(prizeusername):
#    prize = requests.post('http://application4:5003/prizeshort', data=prizeusername)
#    user_data = Prize(username=prizeusername, prize=prize.text)
#    db.session.add(user_data)
#    db.session.commit()


#    return render_template('prize.html', title='prize', prizeusername=prizeusername, prize=prize.text)


### second iteration
def prize(prizeusername):
    prize = requests.post('http://application4:5003/prizelong', data=prizeusername)
     user_data = Prize(username=prizeusername, prize=prize.text)
     db.session.add(user_data)
     db.session.commit()
    
    return render_template('prize.html', title='prize', prizeusername=prizeusername, prize=prize.text)
