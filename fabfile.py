from fabric.api import *

env.hosts = ['denger@de.footter.com:21948']

def update():
    local('hg push')
    with cd('work/mercurial'):
        run('hg pull')
        run('hg up')
        run('supervisorctl restart wsgi')

