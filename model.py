class Report:
    __slots__ = ['date_reported', 'location', 'case_incidents']
    def __init__(self, date_reported, location, case_incidents):
        self.date_reported = date_reported
        self.location = location
        self.case_incidents = case_incidents
    def __repr__(self):
        return 'Report(%s, %s, %s)' % (self.date_reported, self.location, self.case_incidents)