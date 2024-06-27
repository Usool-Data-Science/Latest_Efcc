from flask import Blueprint

app_views = Blueprint('app_views', __name__)#, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.complainant import *
from api.v1.views.suspect import *
# from api.v1.views.recovery import *
from api.v1.views.petition import *
from api.v1.views.fingerprint import *
from api.v1.views.identity import *