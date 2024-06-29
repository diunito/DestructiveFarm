import os

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': {'Team #{}'.format(i): os.environ.get('TEAM_FORMAT', '10.60.{}.1').format(i)
              for i in range(1, int(os.environ.get('TEAM_NUM', 45)) + 1)},
    'FLAG_FORMAT': os.environ.get('FLAG_FORMAT', r'[A-Z0-9]{31}='),

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.
    # (Default values are there just for reference)

    'SYSTEM_PROTOCOL': os.environ.get('SYSTEM_PROTOCOL', 'ructf_http'),
    # HOST, PORT, TOKEN for tcp
    'SYSTEM_HOST': os.environ.get('SYSTEM_HOST', '10.10.10.10'),
    'SYSTEM_PORT': int(os.environ.get('SYSTEM_PORT', 31337)),
    'TEAM_TOKEN': os.environ.get('TEAM_TOKEN', 'your_secret_token'),
    # URL, TOKEN for http
    'SYSTEM_URL': os.environ.get('SYSTEM_URL', 'http://monitor.ructfe.org/flags'),
    'SYSTEM_TOKEN': os.environ.get('SYSTEM_TOKEN', 'your_secret_token'),
    # usable for both http and tcp (handling http/tcp is in the single scripts)
    'SYSTEM_ID_FLAGS_IP': os.environ.get('SYSTEM_ID_FLAGS_IP', 'monitor.ructfe.org'),
    'SYSTEM_ID_FLAGS_PORT': os.environ.get('SYSTEM_ID_FLAGS_PORT', '81'),
    
    # 'SYSTEM_PROTOCOL': 'ructf_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,

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
    'SUBMIT_FLAG_LIMIT': int(os.environ.get('SUBMIT_FLAG_LIMIT', 100)),
    'SUBMIT_PERIOD': float(os.environ.get('SUBMIT_PERIOD', 5)),
    'FLAG_LIFETIME': float(os.environ.get('FLAG_LIFETIME', 60)),

    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    'SERVER_PASSWORD': os.environ.get('SERVER_PASSWORD', '1234'),

    # Use authorization for API requests
    'ENABLE_API_AUTH': bool(os.environ.get('ENABLE_API_AUTH', "false").lower() == "true"), # bool() just to be sure
    'API_TOKEN': os.environ.get('API_TOKEN', 'Tok3N'),

    # Custom library folder (for example containing custom python modules)
    # This path will be added by start_sploit.py
    # to $PYTHONPATH (for python scripts)
    # and to $LIBPATH (for bash scripts)
    'LIBPATH': os.environ.get('LIBPATH', '')
}
