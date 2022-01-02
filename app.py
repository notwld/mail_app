from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'EMAIL_HERE' #make sure to turn off safety feature in gmail settings
app.config['MAIL_PASSWORD'] = 'PASS_HERE'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.static_folder = 'static'
app.secret_key = 'some_secret'
mail = Mail()
mail.init_app(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        sender_email = request.form['email']
        recipient = request.form['recipient']
        subject = request.form['subject']
        msgbody = request.form['msg']
        msg = Message(subject, sender=sender_email, recipients=[recipient])
        msg.body = msgbody
        mail.send(msg)
        print('Message sent!')
        return redirect(url_for('index'))

    return render_template('index.html')

app.run(debug=True)


    #will update later
