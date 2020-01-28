# -- FILE: features/environment.py
#import os
#import tempfile
from behave import fixture, use_fixture

# application we want to test
from reloj_app import app

@fixture
def reloj_client(context, *args, **kwargs):
#    context.db, app.config['DATABASE'] = tempfile.mkstemp()
    app.testing = True
    context.client = app.test_client()
#    with app.app_context():
#        init_db()
    yield context.client
    # -- CLEANUP:
#    os.close(context.db)
#    os.unlink(app.config['DATABASE'])

def before_feature(context, feature):
    # -- HINT: Recreate a new app client before each feature is executed.
    use_fixture(reloj_client, context)