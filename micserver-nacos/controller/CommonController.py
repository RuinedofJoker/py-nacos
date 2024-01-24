from flask import Blueprint, request, Response
import requests

common = Blueprint('common', __name__)

@common.route('/')
def index():
    return '{"test":"index"}'