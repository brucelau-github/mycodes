package main

import "fmt"
import "net"
import "net/url"

func main() {
	p := fmt.Println
	s := "https://bruce:password@dev.nuance.com:2323/path?key1=4&key=value#fragment"

	l, err := url.Parse(s)
	if err != nil {
		panic(err)
	}

	p(l.Scheme)
	p(l.User)
	p(l.User.Username())
	psd, _ := l.User.Password()
	p(psd)

	p(l.Host)
	host, port, _ := net.SplitHostPort(l.Host)
	p(host)
	p(port)
	p(l.Path)
	p(l.Fragment)
	p(l.RawQuery)

	m, _ := url.ParseQuery(l.RawQuery)
	p(m)
	p(m["key1"][0])
}
