CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web',
    'args': (
    '--bind=0.0.0.0:8080',
    '--workers=3',
    'hello.wsgi_application',
    ),
}
