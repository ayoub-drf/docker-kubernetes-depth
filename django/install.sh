apt-get update && apt-get install -y libpq-dev libjpeg-dev libcairo2 gcc

apt-get remove --purge -y
apt-get autoremove -y
apt-get clean
rm -rf /var/lib/apt/lists/*