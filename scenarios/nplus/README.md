# Please, don't ask
## a very real setup juggling with non replicated sessions
> attempting to help out desperate DevOps to... nevermind

`$ virtualenv -p python3 .p3; source .p3/bin/activate`

 - start everything up
   -   `$ docker-compose up`

open http://0.0.0.0:5000

- or tear it down Ctrl+C
   - `$ docker-compose rm; docker-compose build`
- FAIL & REPEAT

otherwise, hammer it

- test if it functionally works 
  - `$ pip install tavern`
  - `$ tavern-ci test_example1.tavern.yaml`
- fire up a cannon...  
  - `$ pip install locust`
  - `$ locust -f test_example1.locust.py --host=http://0.0.0.0:5000`

open > [Locust's UI](http://0.0.0.0:8089/)
