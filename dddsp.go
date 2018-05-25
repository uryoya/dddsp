package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"os"
	"sync/atomic"
	"time"
)

type ReqCounter int64

func (r *ReqCounter) Inc() {
	atomic.AddInt64((*int64)(r), 1)
}

func main() {
	args := os.Args[1:]
	if len(args) < 2 {
		fmt.Fprintf(os.Stderr, "USAGE: dddsp <port> <domain>")
		os.Exit(1)
	}
	port := args[0]
	domain := args[1]

	var rc ReqCounter
	// regist to handler
	http.HandleFunc("/bid", func(w http.ResponseWriter, r *http.Request) {
		rc.Inc()
		fmt.Println(rc)
		// // 1/100 の確率でsleep
		// if rand.Intn(100) == 1 {
		// 	time.Sleep(1 * time.Second)
		// }
		time.Sleep(110 * time.Millisecond)
		price := rand.Intn(90) + 10 // 10 <= price < 100
		fmt.Fprintf(w,
			"{\"url\": \"http://%s/image/999\", \"price\": %d}",
			domain,
			price)
	})

	// start server
	fmt.Fprintf(os.Stderr, "Server on %s", port)
	if err := http.ListenAndServe(port, nil); err != nil {
		fmt.Println(err)
	}
}
