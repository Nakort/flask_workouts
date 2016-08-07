from flask               import Flask

app = Flask(__name__)
app.config.from_object('config.BaseConfiguration')

from app.workouts.routes import workouts
app.register_blueprint(workouts)

from app.results.routes  import results
app.register_blueprint(results)
