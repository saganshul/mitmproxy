class AntiComp:
    def __init__(self):
        self.enabled = False

    def configure(self, options, updated):
        self.enabled = options.anticomp

    def request(self, flow):
        if self.enabled:
            flow.request.anticomp()
