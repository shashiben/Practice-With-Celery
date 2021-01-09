from flask import Flask
from tasks import printHello
from tasks import initCelery
from mail import otpSendViaMail
from mail import OTPGen 


app=Flask(__name__)
app.config['CELERY_BROKER_URL']='pyamqp://'
app.config['CELERY_RESULT_BACKEND']='rpc://'

celery=initCelery(app)

@app.route('/',methods=["GET"])
def printYo():
    return ('YO',201)

@app.route('/sendHello/<name>',methods=["GET"])
def method_name(name):
    a=printHello(name)
    return (a,201)

@app.route('/sendMail/<email>',methods=['GET'])
def send_mail(email):
    otp_send_mail.delay(email,OTPGen())
    return("An email sent to your account,please check out!")

@celery.task(name='tasks.reverse')
def reverse(string):
    return string[::-1]

@celery.task(name='app.otp_send_mail')
def otp_send_mail(email,number):
    otpSendViaMail(email,number)
    return number
