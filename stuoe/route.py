def init_route(app):
    @app.route('/static/<file>')
    def staticfile(file):
        try:
            return open('storage/static/file/' + file,'rb').read()
        except:
            return abort(404)
