from eve import Eve
from settings import domain

DOMAIN = domain.DOMAIN
app = Eve()

if __name__ == '__main__':
    app.run()
