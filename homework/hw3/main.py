import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import glob

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

class Info(object):
    def __init__(self, path):
        info_file = open(os.path.join(path, 'info.txt'))
        (self.title, self.year, self.critic,
         self.total) = info_file.read().splitlines()
        self.dirname = path.split(os.sep)[-1]

class Item(object):
    def __init__(self, quote, critic, reviewer, company):
        self.quote = quote
        self.critic = critic
        self.reviewer = reviewer
        self.company = company

class Reviews(object):
    def __init__(self, path):
        self.left = []
        self.right = []

        file_names = glob.glob(os.path.join(path, 'review[0-9]*.txt'))
        self.count = len(file_names)
        file_names.sort()

        for i in range(self.count):
            review_file = open(file_names[i])
            (quote, critic, reviewer, company) = file.read(review_file).splitlines()
            item = Item(quote, critic, reviewer, company)
            
            if i < self.count / 2:
                self.left.append(item)
            else:
                self.right.append(item)

class ReviewsModule(tornado.web.UIModule):
    def render(self, review_items):
        return self.render_string('review.html',
                                  review_items=review_items)
    
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        film = self.get_argument('film')
        path = os.path.join(os.path.dirname(__file__),
                                'Static', 'moviesfiles', film)

        info = Info(path)

        overview_file = open(os.path.join(path, 'generaloverview.txt'))

        overview = list()
        for line in overview_file:
            line = line.strip()
            (term, sep, data) = line.partition(':')
            overview.append((term, data))

        reviews = Reviews(path)

        self.render('movie.html', info=info, overview=overview,
                    reviews=reviews)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=
        [(r'/', IndexHandler)],
        template_path=os.path.join(os.path.dirname(__file__), 'Templates'),
        static_path=os.path.join(os.path.dirname(__file__), 'Static'),
        ui_modules={'Reviews': ReviewsModule},
        debug=True
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
