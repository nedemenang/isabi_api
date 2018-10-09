from app.blueprints.base_blueprint import Blueprint, BaseBlueprint, request
# from app.controllers.meal_controller import MealController

url_prefix = '{}/sample'.format(BaseBlueprint.base_url_prefix)
sample_blueprint = Blueprint('sample', __name__, url_prefix=url_prefix)
# meal_controller = MealController(request)

@sample_blueprint.route('/', methods=['GET'])
def list_meals():
	return "this blue print is working"

# @meal_blueprint.route('/<int:meal_id>/', methods=['GET'])
# def get_meal(meal_id):
# 	return meal_controller.get_meal(meal_id)

# @meal_blueprint.route('/', methods=['POST'])
# def create_meal():
# 	return meal_controller.create_meal()

# @meal_blueprint.route('/<int:meal_id>/', methods=['PATCH', 'PUT'])
# def update_meal(meal_id):
# 	return meal_controller.update_meal(meal_id)

# @meal_blueprint.route('/<int:meal_id>/', methods=['DELETE'])
# def delete_meal(meal_id):
# 	return meal_controller.delete_meal(meal_id)

