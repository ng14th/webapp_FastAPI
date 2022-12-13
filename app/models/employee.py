from app.core.mixins.mongodb_mixins import MongoCreateUpdateMixin
from app.core.database.mongo import umongo_cnx
from umongo import fields

@umongo_cnx.register
class EmployeeInformations(MongoCreateUpdateMixin):
    tenant_id = fields.StringField(require = True)
    username = fields.StringField(require = True)
    full_name = fields.StringField(require = True)
    phone = fields.StringField(allow_none = True)
    
    class Meta:
        collection_name = "EmployeeInformations"
    