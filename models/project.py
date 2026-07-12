class Project:

    def __init__(
        self,
        name,
        description,
        status,
        progress,
        next_action,
        priority
    ):

        self.name = name
        self.description = description
        self.status = status
        self.progress = progress
        self.next_action = next_action ## makluman, bahagian class jangan letak coma, nnty die ingat tuple, bila run tak kluar atau crash.
        self.priority = priority