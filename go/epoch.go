package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	now := time.Now()
	secs := now.Unix()
	nanos := now.UnixNano()

	p(now)

	millis := nanos / 1000000
	p(secs)
	p(millis)
	p(nanos)

	p(time.Unix(secs, 0))
	p(time.Unix(0, nanos))

	rfc3339 := time.RFC3339

	p(now.Format(rfc3339)) // 2018-01-05T13:04:31-05:00
	t1, _ := time.Parse(rfc3339, "2018-01-05T13:04:31-05:00")
	p(t1)

	p(now.Format("3:04PM"))
	p(now.Format(time.ANSIC)) // Fri Jan  5 13:22:20 2018

}
