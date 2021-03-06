from app import create_app, db
from flask_migrate import Migrate


app = create_app()
Migrate(app, db)

@app.shell_context_processor
def make_shell():
    return dict(db=db)

