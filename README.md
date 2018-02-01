# networkingLab
Labs as part of Computer Networking course taught at IIT PKD. 

# LAB 1: Echo server

## Graded (Jan 19, 2018)

1. An echo server that handles multiple clients concurrently.

You can use any programming language that you like, however it would
be easier if your language has good support for concurrency
(particularly [green threads]). Some languages known to have good
concurrency support are Haskell, Erlang, Go, Java and other langauges
on JVM like scala, clojure. You might also want to stick to the
language you choose for the rest of the assignments and projects.


## Practice problem (to be done in the lab)

1. Write a TCP version of the `netcat` program in your favourite language.

2. Write a UDP version of `netcat` which sends each line in a separate
   UDP packet. Assume that the maximum length of each line is 1024
   bytes.

3. 	- Write a simple client that can make dns queries to any dns sever.
   and resolve the hostname to its ip address.

	- Write a simple dns server does the following: For every query to
   resolve the hostname `www.james.bond` returns the ip address
   `007.007.007.007`. Your name server should work with any program
   like `nslookup` not just your client in step 1.
