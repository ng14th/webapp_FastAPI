# -*- coding: utf-8 -*-
from datetime import datetime
from umongo import Document, fields, EmbeddedDocument
from app.core.database.mongo import umongo_cnx


@umongo_cnx.register
class MongoCreateUpdateMixin(Document):
    create_at = fields.DateTimeField(allow_none=True)
    update_at = fields.DateTimeField(allow_none=True)

    class Meta:
        abstract = True

    def pre_insert(self):
        if not self.create_at:
            self.create_at = datetime.utcnow()
        if not self.update_at:
            self.update_at = datetime.utcnow()

    def pre_update(self):
        self.update_at = datetime.utcnow()
