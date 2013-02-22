from fabric.api import *

env.supervisorapp = 'inmobiliaria'
env.localfolder = '***REMOVED***'
env.hosts = ['***REMOVED***']
env.remotedir = '/home/ubuntu/inmoviliaria/inmobiliaria'
env.activate = 'source /home/ubuntu/inmoviliaria/bin/activate'

##################################################################################

def virtualenv(command):
    with cd(env.remotedir):
        run(env.activate + ' && ' + command)

def pushpull():
    #Local commands
    with cd(env.localfolder):
        local('git push')
    #Remote commands
    with cd(env.remotedir):
        #update git repository
        run('git pull')

def syncdb():
    virtualenv('python manage.py syncdb')

def install_requirements():
    virtualenv('pip install -r %srequirements.txt' % (env.remotedir))

@task(alias='dp', default=True)
def deploy():
    pushpull()
    #syncdb
    syncdb()
    #restart the gunicorn server
    restartunicorn()

@task(alias='ru')
def restartunicorn():
    run(r'sudo supervisorctl status %s | sed "s/.*[pid ]\([0-9]\+\)\,.*/\1/" | xargs kill -HUP' % (env.supervisorapp))

@task(alias='rn')
def restartnginx():
    run('sudo service nginx restart')
