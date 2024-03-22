class Event:
    def __init__(self, name, requirements, success_outcome, partial_success_outcome, failure_outcome):
        self.name = name
        self.requirements = requirements
        self.success_outcome = success_outcome
        self.partial_success_outcome = partial_success_outcome
        self.failure_outcome = failure_outcome


