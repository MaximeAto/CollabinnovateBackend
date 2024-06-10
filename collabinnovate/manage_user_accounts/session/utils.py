import re

#validateur d'adresse ip
def is_valid_ip(ip):
  ip_regex = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
  return re.match(ip_regex, ip) is not None