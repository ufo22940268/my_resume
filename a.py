from fabric.api import *

# the user to use for the remote commands
env.user = 'root'
# the servers where the commands are executed
env.hosts = ['192.241.196.189']


def deploy():
    local('tar --exclude "../resume/\.*" -cvf /tmp/k.tar ../resume')
    put('/tmp/k.tar', '/tmp/k.tar')

    with cd('/usr/share/nginx/html/'):
        run('tar -xvf /tmp/k.tar')
