import os

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': {'Team #{}'.format(i): '10.60.{}.1'.format(i)
              for i in range(1, 45 + 1)},
    'FLAG_FORMAT': os.environ.get(r'FLAG_FORMAT', r'[A-Z0-9]{31}='),

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.

    'SYSTEM_PROTOCOL': os.environ.get('SYSTEM_PROTOCOL', 'volgactf'),
    'SYSTEM_HOST': os.environ.get('SYSTEM_HOST', '10.10.10.10'),
    'SYSTEM_PORT': int(os.environ.get('SYSTEM_PORT', 31337)),
    'SYSTEM_URL': os.environ.get('SYSTEM_URL', 'http://monitor.ructfe.org/flags'),
    'SYSTEM_TOKEN': os.environ.get('SYSTEM_TOKEN', 'your_secret_token'),
    
    
    'TEAM_TOKEN': os.environ.get('TEAM_TOKEN', 'your_secret_token'),
    
    #'SYSTEM_PROTOCOL': 'ructf_tcp',
    #'SYSTEM_HOST': '127.0.0.1',
    #'SYSTEM_PORT': 31337,

    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': 'your_secret_token',

    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_HOST': '127.0.0.1',

    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,
    # 'TEAM_TOKEN': 'your_secret_token',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': float(os.environ.get('SUBMIT_FLAG_LIMIT', 100)),
    'SUBMIT_PERIOD': float(os.environ.get('SUBMIT_PERIOD', 5)),    
    'FLAG_LIFETIME': float(os.environ.get('FLAG_LIFETIME', 60)),

    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    'SERVER_PASSWORD': os.environ.get('SERVER_PASSWORD', '1234'),

    # Use authorization for API requests
    'ENABLE_API_AUTH': False,
    'API_TOKEN': '00000000000000000000'
}
