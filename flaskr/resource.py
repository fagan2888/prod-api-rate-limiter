from flask import (
    Blueprint, request, jsonify
)

from .core import limiter


bp = Blueprint('resource', __name__, url_prefix='/resource')

# Set a default limit of 1 request per second,
# which can be changed granurarly in each route.
limiter.limit('1/second')(bp)


@bp.route('/test', methods=('GET', 'POST'))
@limiter.limit('1 per 10 second')
def test():
    if request.method == 'POST':
        response = {'message': 'This was a POST'}
    else:
        response = {'message': 'This was a GET'}
    return jsonify(response), 200
