package main

import "os"
import "fmt"

func main() {
	defer func() {
		if err := recover(); err != nil {
			fmt.Println("recover a panic", err)
		}
	}()

	panic("a problem")
	// the belowing code would not run after panicing
	fmt.Println("after panic")

	_, err := os.Create("/tmp/file")
	if err != nil {
		panic(err)
	}
}
