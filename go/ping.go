package main

import (
	"fmt"
	"os/exec"
	"time"
)

func ping(hosts <-chan string, sigs chan<- bool) {
	for host := range hosts {
		pingCmd := exec.Command("ping", "-c 2", host)
		_, err := pingCmd.Output()

		if err == nil {
			fmt.Printf("%s: ", host)
			fmt.Printf("active")
			fmt.Println()
		}

	}
	sigs <- true
}

func pingHost(host string, sigs chan<- bool) {
	pingCmd := exec.Command("ping", "-c 2", host)
	_, err := pingCmd.Output()

	if err == nil {
		fmt.Printf("%s: ", host)
		fmt.Printf("active")
		fmt.Println()
	}

	sigs <- true
}

func main() {
	//hosts := make(chan string, 255)
	sigs := make(chan bool, 10)

	workers := 254 * 254

	startTime := time.Now()

	//	for i := 1; i <= workers; i++ {
	//		go ping(hosts, sigs)
	//	}

	for i := 1; i < 255; i++ {
		for j := 1; j < 255; j++ {
			go pingHost(fmt.Sprintf("211.157.%d.%d", i, j), sigs)
		}
	}

	for i := 1; i <= workers; i++ {
		<-sigs
		//fmt.Println("worker ", i, "of 10 ends")
	}

	runningTime := time.Now().Sub(startTime)
	fmt.Println("spends: ", runningTime.Minutes(), "m")
}
