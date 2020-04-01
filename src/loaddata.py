from urllib.request import urlopen, Request
import pickle


site = Request("https://anushk.dev/files/outdata", headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0'
})
data = pickle.load(urlopen(site))
