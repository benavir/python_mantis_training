from sys import maxsize


class Project:

    def __init__(self, id=None, name=None, status=None, inherit_global=None, view_state=None, description=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.name == other.name
