from flask import Flask
from routes.mine import mine_bp

from flask_cors import CORS

app = Flask(__name__)

# 注册Blueprint
app.register_blueprint(mine_bp)

if __name__ == '__main__':
    app.run(debug=True)