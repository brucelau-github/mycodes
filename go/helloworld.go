package main

import (
	"fmt"
	"strings"
)

func main() {
	var tasks = make(chan string, 20)
	go func() {
		fmt.Println("\nworker is ready to process")
		for t := range tasks {
			fmt.Println("\nafter change to upper case", strings.ToUpper(t))
		}
	}()

	var input string
	for {
		fmt.Printf("enter the string( ! to quit):")
		fmt.Scanln(&input)
		if strings.Compare(input, "!") == 0 {
			break
		}
		tasks <- input
	}
	close(tasks)
}
