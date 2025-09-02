# app/routes/dams.py

from flask_restx import Namespace, Resource, fields
from ..models import Dam
from ..utils.db import get_or_404

dams_bp = Namespace('Dams', description='Endpoints for managing dams')

dam_model = dams_bp.model('Dam', {
    'dam_id': fields.String(required=True, description='The ID of the dam'),
    'dam_name': fields.String(required=True, description='The name of the dam'),
    'full_volume': fields.Integer(description='The full volume of the dam', allow_null=True),
    'latitude': fields.Float(description='The latitude of the dam', allow_null=True),
    'longitude': fields.Float(description='The longitude of the dam', allow_null=True),
})

@dams_bp.route('/', endpoint='dams_list')
class DamsList(Resource):
    @dams_bp.doc('list_dams')
    @dams_bp.marshal_list_with(dam_model)
    def get(self):
        return Dam.query.all()

@dams_bp.route('/<string:dam_id>', endpoint='dams_detail')
@dams_bp.param('dam_id', 'The ID of the dam')
class DamDetail(Resource):
    @dams_bp.doc('get_dam')
    @dams_bp.marshal_with(dam_model)
    def get(self, dam_id):
        return get_or_404(Dam, dam_id, "Dam not found.")
