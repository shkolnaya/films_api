from src import api
from src.resourses.actors import ActorListApi
from src.resourses.aggregations import AggregationApi
from src.resourses.auth import AuthRegister, AuthLogin
from src.resourses.films import FilmListApi
from src.resourses.smoke import Smoke

api.add_resource(Smoke, '/smoke')
api.add_resource(FilmListApi, '/films', '/films/<uuid>')
api.add_resource(ActorListApi, '/actors', '/actors/<uuid>')
api.add_resource(AggregationApi, '/aggregations')
api.add_resource(AuthRegister, '/register', strict_slashes=False)
api.add_resource(AuthLogin, '/login', strict_slashes=False)
