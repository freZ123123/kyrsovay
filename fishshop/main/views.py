from aifc import Error

from django.shortcuts import render, get_object_or_404
from .models import Fish


def show_posts(request, post_id):
    post = get_object_or_404(Fish, pk=post_id)



def index(request) :
    return render(request, 'main/index.html')


def about(request) :
    fishs = Fish.objects.all()
    return render(request, 'main/about.html', {'Рыба' : fishs})


def range(request) :
    return render(request, 'main/range.html')


def delivery(request) :
    return render(request, 'main/delivery.html')


def accept(request) :
    return render(request, 'main/accept.html')


def bays(request) :
    return render(request, 'main/bays.html')


from flask import Flask, jsonify


app = Flask(__name__)


def not_found_error(error):
    return jsonify({'error': 'Not Found'}), 404


def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run()
