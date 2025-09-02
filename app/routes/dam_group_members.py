# app/routes/dam_group_members.py

from flask_restx import Namespace, Resource, fields
from ..models import DamGroupMember

dam_group_members_bp = Namespace('DamGroupMembers', description='Endpoints for managing dam group members')

group_member_model = dam_group_members_bp.model('GroupMember', {
    'group_name': fields.String(required=True, description='The name of the group'),
    'dam_id': fields.String(required=True, description='The ID of the dam'),
})

@dam_group_members_bp.route('/', endpoint='dam_group_members_list')
class GroupMembersList(Resource):
    @dam_group_members_bp.doc('list_dam_group_members')
    @dam_group_members_bp.marshal_list_with(group_member_model)
    def get(self):
        return DamGroupMember.query.all()

@dam_group_members_bp.route('/<string:group_name>', endpoint='dam_group_members_by_group')
@dam_group_members_bp.param('group_name', 'The name of the group')
class GroupMembersByGroup(Resource):
    @dam_group_members_bp.doc('get_members_by_group')
    @dam_group_members_bp.marshal_list_with(group_member_model)
    def get(self, group_name):
        items = DamGroupMember.query.filter_by(group_name=group_name).all()
        if not items:
            dam_group_members_bp.abort(404, "No members found for the specified group.")
        return items
