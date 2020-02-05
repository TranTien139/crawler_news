import requests
import subprocess

url = "http://coinup24.com/"
html = requests.get(url)
p = subprocess.Popen(['java', '-jar', './coinup_parser-1.0.jar', url, html.text], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for output_line in iter(p.stdout.readline, b''):
    print(output_line)
