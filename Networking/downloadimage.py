import urllib.request

url = "https://golang.org/lib/godoc/images/go-logo-blue.svg"

urllib.request.urlretrieve(url, "go.svg")

#or 

urllib.request.urlretrieve("https://golang.org/lib/godoc/images/go-logo-blue.svg", "golang.svg")