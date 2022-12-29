from app.core.mixins.mongodb_mixins import MongoCreateUpdateMixin
from app.core.database.mongo import umongo_cnx
from umongo import fields, Document

@umongo_cnx.register
class User(Document):
    tenant_id = fields.StringField(require = True)
    email = fields.StringField(require = True)
    password = fields.StringField(require = True)
    username = fields.StringField(require = True)
    full_name = fields.StringField(require = True)
    phone_number = fields.StringField(allow_none = True)
    
    class Meta:
        collection_name = "User"
        
@umongo_cnx.register
class UserMeMe(Document):
    tenant_id = fields.StringField(require = True)
    email = fields.StringField(require = True)
    username = fields.StringField(require = True)
    full_name = fields.StringField(require = True)
    phone_number = fields.StringField(allow_none = True)
    
    class Meta:
        collection_name = "UserMeMe"