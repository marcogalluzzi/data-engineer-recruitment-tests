# Technical questions

1. How long did you spend on the coding test? What would you add to your solutions if you had more time? If you didn't spend much time on the coding test then use this as an opportunity to explain what you would add.
2. Why did you choose the language you used for the coding test?
3. What was the most useful feature that was added to the latest version of your chosen language?
4. How would you track down a performance issue in production? Have you ever had to do this?
5. Please describe yourself using JSON.

### Answer 1

I've spent around 3 days (24 hours).
* The solution was clear enough before starting, however I had to solve some corner cases.
* I spent time to make the code simple and clear.
* I wasn't used to some Python functions so I had to search for them on the internet.
* I also spent some time checking how to parallelize the first program to get extra bonus points, but finally I hadn't time to finish it.

If I had more time I would:
* Parallelize first program
* Add checking of input values
* Add unit tests
* Add type hints so I can use `mypy` or `pyre` for type checking.
* Generalize some solutions

## Answer 2

I've chosen `Python` because is a simple and powerful language for creating command line scripts related to text processing.

## Answer 3

In Python version 3.6 a useful feature, along with others, is the new kind of string literals called _Formatted string literals_. You can embed Python expressions inside string constants prefixed with 'f'. This means you can replace the following:
```
def generate_event(order_type, order_id, timestamp):
    """Create a business event as a JSON string"""
    return '{{ "Type": "{}", "Data": {{ "OrderId": "{}", "TimestampUtc": "{}" }} }}'.format(order_type, order_id, timestamp)
```
With the following:
```
def generate_event(order_type, order_id, timestamp):
    """Create a business event as a JSON string"""
    return f'{{ "Type": "{order_type}", "Data": {{ "OrderId": "{order_id}", "TimestampUtc": "{timestamp}" }} }}'
```
Which makes the task of creating formatted strings more straightforward.

## Answer 4

I've been involved in tracking down performance issues in production. What did I check?
* I've tried to check what are the most time consuming functions or queries, and the analyze them separately.
* I've checked the CPU and memory consumption in Linux or in the AWS environment (EC2 or RDS).
* I try to reproduce the same case in a test environment, if possible.
* I increase the log level to try to find more hints.

## Answer 5

I've been using JSON when creating REST APIs in the back-end with Java and when consuming it from a front-end with Javascript.
