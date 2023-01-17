# 0x10. Python - Network #0

## Learning Objectives

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## Requirements

- All files are created and executed on Ubuntu 14.04 LTS using Python3 (version 3.4.3)
- All Python code is linted with PEP 8 style guide (version 1.7.\*)

## Tasks

<details>
<summary>View Contents</summary>

### [0. cURL body size](./0-body_size.sh)

- Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
  - The size must be displayed in bytes
  - You have to use curl

```
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
```

### [1. cURL to the end](./1-body.sh)

- Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
  - Display only body of a 200 status code response
  - You have to use curl

```
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
```

### [2. cURL Method](./2-delete.sh)

- Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

```
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
```

### [3. cURL only methods](./3-methods.sh)

- Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

```
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
```

### [4. cURL headers](./4-header.sh)

- Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
  - A header variable X-HolbertonSchool-User-Id must be sent with the value 98
  - You have to use curl

```
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello Holberton School!
```

### [5. cURL POST parameters](./5-post_params.sh)

- Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
  - A variable email must be sent with the value hr@holbertonschool.com
  - A variable subject must be sent with the value I will always be here for PLD
  - You have to use curl

```
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: hr@holbertonschool.com
    subject: I will always be here for PLD
```

### [6. Find a peak](./6-peak.py)

- Write a function that finds a peak in a list of unsorted integers.
  - Prototype: `def find_peak(list_of_integers)`:
  - You are not allowed to import any module
  - Your algorithm must have the lowest complexity
  - 6-peak.py must contain the function
  - 6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)

```
guillaume@ubuntu:~/0x10$ cat 6-main.py
```

```python
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 3, 1]))
```

```
guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt
2 6-peak.txt
```

</details>
