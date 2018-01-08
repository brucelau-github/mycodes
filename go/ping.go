package main

import (
	"fmt"
	"os"
	"os/exec"
	"time"
)

func pingHost(host string, sigs chan<- bool, hosts chan<- string) {
	pingCmd := exec.Command("ping", "-c 1 -q -W 2", host)

	var timer *time.Timer
	timer = time.AfterFunc(50 * time.Second, func() {
		pingCmd.Process.Kill()
	})

	_, err := pingCmd.Output()

	if err == nil {
		fmt.Printf("%s: ", host)
		fmt.Printf("active")
		fmt.Println()
		hosts <- host
	}

	timer.Stop()
	sigs <- true
}

func saveFile(hosts <-chan string) {
	f, e := os.Create("active_hosts.log")
	if e != nil {
		panic(e)
	}
	defer f.Close()

	for host := range hosts {
		_, e := f.WriteString(host + "\n")
		if e != nil {
			panic(e)
		}
	}
}

func main() {
	sigs := make(chan bool, 10)
	hosts := make(chan string, 20)

	workers := 0

	startTime := time.Now()

	go saveFile(hosts)

	for i := 1; i < 255; i++ {
		for j := 1; j < 255; j++ {
			go pingHost(fmt.Sprintf("211.157.%d.%d", i, j), sigs, hosts)
			workers++
		}
	}

	for i := 1; i <= workers; i++ {
		<-sigs
	}

	close(hosts)

	runningTime := time.Now().Sub(startTime)
	fmt.Println("spends: ", runningTime, "m")
}
