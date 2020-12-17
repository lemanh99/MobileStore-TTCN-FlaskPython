def application(env, start_response):
    import sys
    import socket
    from datetime import date
    from string import Template

    with open ("ROOT/run.py", "r") as index_file:
         data=index_file.read().replace('\n', '')
         index_object = Template(data)
         index_formated=index_object.substitute(mydate=date.today().year, hostname=socket.gethostname())
         if sys.version.split(' ')[0].split('.')[0] == '3':
            index_formated = index_formated.encode('utf-8')
    start_response('200 OK', [('Content-Type','text/html')])
    return [ index_formated  ]
