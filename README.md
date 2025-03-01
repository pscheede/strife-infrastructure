# strife-infrastructure

## Usage / Installation

1. create new user `sudo useradd -r -s /usr/sbin/nologin strifeuser`
2. `sudo mkdir /opt/strife`
3. `sudo chown -R strifeuser:strifeuser /opt/strife`
4. `cd /opt/strife`
5. `sudo -u strifeuser git clone https://github.com/pscheede/strife-infrastructure.git .`
6. `sudo -u strifeuser python3 -m venv .venv`
7. `sudo -u strifeuser .venv/bin/pip install -r requirements.txt`
8. create .env file with `GH_TOKEN` secret
9. run `./modify-sudoers.bash`, then follow the instruction in the output
10. symlink service TODO
11. enable and start service TODO
12. TODO nginx config

## Roadmap
- webserver for webhooks
- configuration in this repo
- pull build from GitHub CI
- restart docker build
- app configuration & runtime in this repo
