import stuoe_extensions

def helloworld():
    return 'sometime'

class amazingExtensions(stuoe_extensions.Extensions):
    def __init__(self):
        self.title = 'amazing'
        self.add_route('/hello',helloworld)
