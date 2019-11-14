import web

from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = input()
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
