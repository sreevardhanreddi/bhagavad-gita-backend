from flask import Blueprint

main = Blueprint('main_blueprint', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    return "RadhaKrishna"