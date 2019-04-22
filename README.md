
# Simple IRC read-only client

Change the `config.template.json` to `config.json` and run with:

    python main.py

Tail the output.txt

## Daemonising

Copy `irc-read-only.service` to `/etc/systemd/system/irc-read-only.service`

    chmod 644 /etc/systemd/system/irc-read-only.service

Clone this repo / copy contents to `/var/www/irc-read-only-client`

    chmod 755 /var/www/irc-read-only-client
    chown www-data:www-data /var/www/irc-read-only-client  # Make sure `/var/www/irc-read-only-client` user and group is www-data
    chmod 755 /var/www/irc-read-only-client/main.py  # Make sure `main.py` is executable.

    systemctl status irc-read-only
    systemctl enable irc-read-only
    systemctl start irc-read-only
    tail -f -n 30 /var/log/syslog # to debug
