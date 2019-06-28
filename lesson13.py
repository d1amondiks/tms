# -*- coding: utf-8 -*-
from flask import Flask, render_template


test_app = Flask('test_app')
test_app.debug = True


@test_app.route('/')
@test_app.route('/index')
def home():
    return render_template('index.html')

@test_app.route('/base')
def base():
    return render_template('base.html')

@test_app.route('/<region>')
def home3(region):
    return render_template('%s.html' % region, title='%s' % region)

if __name__ == '__main__':
    test_app.run(host='localhost')