package main

type error interface {
	Error() string
}

type PathError struct {
	Op string
	Path string
	Err error
}

func (e *PathError) Error() {
	return e.Op + " " + e.Path + ": " + e.Err.Error()
}

for try := 0; try < 2; try++ s {
	file err = os.Create(filename)
	if err == nil {
		return
	}

	//err.(type) type assertion
	if e, ok := err.(*os.PathError); ok && e.Err == syscall.ENOSPC {
		deleteTempFiles()
		continue
	}

	return
}

// the usual way to report an error is to return an error as an extra value the
// if the error is so vital that program must stop running, we use panic()

panic("a critical error happened, please check it with administrator")
// but in real library function should avoid panic. It is unreasonable to
// interupt a program running from a library. but if the library could not set
// itself up, it looks like good to panic

var user = os.Getenv("USER")

func init() {
	if user == "" {
		panic("no value for $USER")
	}
}

// panic will unwind the stack of the goroutine until it reaches the top level
// stack of the program, which ends with dying. However, recover build-in
// function could help to control this process to resume normal execution.
// Because of unwinding happening only in defer functions, recover() works well
// putting it inside a defer function.

func server(workChan <-chan *Work) {
	for work := range workChan {
		go safelyDo(work)
	}
}

func safelyDo(work *Work) {
	defer func() {
		if err := recover(); err != nil {
			log.Println("work failed", err)
		}
	}()

	do(work)
}

// recover() alway returns nil if calling from normal goroutine.
