package main

import (
	"fmt"
	"sync"
)

type SafeURLs struct {
	mu   sync.Mutex
	urls map[string]bool
}

func (s *SafeURLs) Add(url string) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.urls[url] = true
}
func (s *SafeURLs) Contains(url string) bool {
	s.mu.Lock()
	defer s.mu.Unlock()
	_, ok := s.urls[url]
	return ok
}

type Fetcher interface {
	// Fetch returns the body of URL and
	// a slice of URLs found on that page.
	Fetch(url string) (body string, urls []string, err error)
}

// Crawl uses fetcher to recursively crawl
// pages starting with url, to a maximum of depth.
func Crawl(url string, depth int, fetcher Fetcher) {
	// TODO: Fetch URLs in parallel.
	// TODO: Don't fetch the same URL twice.
	// This implementation doesn't do either:
	if depth <= 0 {
		return
	}

	body, urls, err := fetcher.Fetch(url)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("found: %s %q\n", url, body)
	var wg sync.WaitGroup
	visitedURLs := SafeURLs{urls: make(map[string]bool)}
	for _, u := range urls {
		if visitedURLs.Contains(u) {
			continue
		}
		visitedURLs.Add(u)
		wg.Add(1)
		go func(u string) {
			defer wg.Done()
			Crawl(u, depth-1, fetcher)
		}(u)
	}
	wg.Wait()
	return
}

func main() {
	Crawl("https://golang.org/", 4, fetcher)
}

type fakeFetcher map[string]*fakeResult

type fakeResult struct {
	body string
	urls []string
}

func (f fakeFetcher) Fetch(url string) (string, []string, error) {
	if res, ok := f[url]; ok {
		return res.body, res.urls, nil
	}
	return "", nil, fmt.Errorf("not found: %s", url)
}

var fetcher = fakeFetcher{
	"https://golang.org/": &fakeResult{
		"The Go Programming Language",
		[]string{
			"https://golang.org/pkg/",
			"https://golang.org/cmd/",
		},
	},
	"https://golang.org/pkg/": &fakeResult{
		"Packages",
		[]string{
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/cmd/",
			"https://golang.org/pkg/fmt/",
			"https://golang.org/pkg/os/",
		},
	},
	"https://golang.org/pkg/fmt/": &fakeResult{
		"Package fmt",
		[]string{
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/",
			"https://golang.org/pkg/",
		},
	},
	"https://golang.org/pkg/os/": &fakeResult{
		"Package os",
		[]string{
			"https://golang.org/",
			"https://golang.org/pkg/",
		},
	},
}
