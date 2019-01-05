class Report:
    __slots__ = ['date_reported', 'location', 'case_incidents']
    def __init__(self, report_number, date_reported, location, case_incidents):
        self.report_numner = report_number
        self.date_reported = date_reported
        self.location = location
        self.case_incidents = case_incidents
    def __repr__(self):
        return 'Report(%d, %s, %s, %s)' % (self.report_number, self.date_reported, self.location, self.case_incidents)