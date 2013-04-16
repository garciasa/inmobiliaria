from fabric.api import *

env.supervisorapp = 'inmobiliaria'
env.localfolder = '***REMOVED***'
env.key_filename = '***REMOVED***'
env.hosts = ['***REMOVED***']
env.remotedir = '/home/ubuntu/inmoviliaria/inmobiliaria'
env.activate = 'source /home/ubuntu/inmoviliaria/bin/activate'

##################################################################################

def virtualenv(command):
    with cd(env.remotedir):
        run(env.activate + ' && ' + command)
'''
def pushpull():
    #Local commands
    with cd(env.localfolder):
        local('git push')
    #Remote commands
    with cd(env.remotedir):
        #update git repository
        run('git pull')
'''

def pushpull(branch='master'):
   #Local commands
   with cd(env.localfolder):
       local('git push %s %s'% (env.remotename,branch))
   #Remote commands
   with cd(env.remotedir):
       #update git repository
       run('git checkout %s' % (branch))
       run('git pull %s %s' % (env.remotename,branch))



def syncdb():
    virtualenv('python manage.py syncdb')

def install_requirements():
    virtualenv('pip install -r %srequirements.txt' % (env.remotedir))

@task(alias='dp', default=True)
def deploy(branch='master'):
    pushpull(branch)
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

