from flask import Flask


def create_app():
    app = Flask(__name__)

    from .blueprints.public import routes
    from .blueprints.budget.routes import bp as budget_bp
    app.register_blueprint(routes.bp)
    app.register_blueprint(budget_bp)

    return app
