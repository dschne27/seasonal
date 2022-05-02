def factory():
    from models import db, User
    from views import create_app
    from flask_migrate import upgrade,migrate,init,stamp

    app = create_app()
    app.app_context.push()
    db.create_all()


    # migrate database to latest revision

    init()
    stamp()
    migrate()
    upgrade()

factory()