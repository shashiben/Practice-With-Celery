from celery import Celery
app = Celery('tasks', broker='pyamqp://guest@localhost//',backend='db+sqlite:///db.sqlite3')

def initCelery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

    
@app.task
def printHello(text):
    return "Hello "+str(text)