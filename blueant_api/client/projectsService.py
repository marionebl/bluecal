from zeep import CachingClient as Client


def client(c):
    return Client(c.url + 'ProjectsService?wsdl')
