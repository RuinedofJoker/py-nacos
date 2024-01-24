from flask import Blueprint, request, Response

ai = Blueprint('ai', __name__, url_prefix='/ai')

@ai.route('/test')
def testAi():
    return {"ai":"response"}