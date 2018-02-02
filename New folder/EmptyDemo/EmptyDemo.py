from flask import Flask, render_template, request, session
from wtforms import Form, StringField, validators

import datetime
import Processes

app = Flask(__name__)


@app.route('/')
def graph():
    session['userid'] = 'John'
    now = datetime.datetime.now()
    todayDate = str(now.day)+'-'+str(now.month)+'-'+str(now.year)
    nowMonth = str(now.month)
#    percentage = Processes.percentage_cal()
    #otherPercentage = 100-(Processes.percentage_cal())
    user = Processes.payTotal(session['userid'])
    user1 = Processes.overDueAmt(session['userid'])
    user2 = Processes.processUser2(session['userid'])


    return render_template('loans.html',
                           todayDateNow = now,
                           todaythedate = todayDate,
                           duedate = nowMonth,
                           #tvePercentage = percentage,
                           #nvePercentage = otherPercentage,
                            getuser = user, getuser2 = user1,
                           userget = user2)

@app.route('/update/<string:postlist>/')
def update_totalPayAmount(postlist):

    print(postlist)
    poList = postlist.split('$')
    name = poList[0]
    totalpayable1 = postlist[1]
    payamount = poList[2]
    print(name)
    print(poList[1])
    print(payamount)

    Processes.reduceAfterpay(name,poList[1],payamount)
    print('Amount has Decreased')

    return render_template('loans.html')









if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()



