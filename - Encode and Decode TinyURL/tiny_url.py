import requests
class Codec:

    def encode(self, longUrl: str) -> str:
        full_url = "http://tinyurl.com/api-create.php?url=" + longUrl
        r = requests.get(full_url)
        if r.status_code == 200:
            return r.text
        
    def decode(self, shortUrl: str) -> str:
        r = requests.get(shortUrl, allow_redirects=False)
        if r.status_code == 301:
            return r.headers['Location']
        

def main():
    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    #print(codec.encode("http://www.fullondesign.co.uk/"))
    #print(codec.decode('https://tinyurl.com/d4px9f'))
    url = "http://inw.net.ua"
    codec.decode(codec.encode(url))


if __name__ == '__main__':
    main()