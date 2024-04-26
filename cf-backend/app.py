from flask import Flask
from routes.mine import mine_bp
from routes.projectsView import getProjects_bp
from routes.projectDetails import getProjectDetails_bp
from routes.search import search_bp

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 注册Blueprint
app.register_blueprint(mine_bp)
app.register_blueprint(getProjects_bp)
app.register_blueprint(getProjectDetails_bp)
app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True)