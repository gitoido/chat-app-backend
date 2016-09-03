from eve import Eve
import config

app = Eve(settings=config.app)

if __name__ == '__main__':
    app.run()
