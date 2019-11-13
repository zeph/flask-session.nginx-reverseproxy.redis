# flask-session, nginx-reverseproxy, (redis)
## being able to test locally (on a laptop) nginx's LB confs

REQUIREMENTS: you should have at least a working docker setup on your laptop

Just choose a scenario/folder, fire it up with `docker-compose up`. Later scale it with `docker-compose scale web=<N>` ...N as the number of instances you want. To kill a random one you need to use `docker` itself, with a `docker stop <instance>`. Check out [Tavern](https://github.com/taverntesting/tavern) to validate that the session is being handled properly, then hammer it with [Locust](https://github.com/locustio/locust); both have a sample file in this root folder.

Happy hackin'

##### by me (Zeph/`polena28`/guido.maria.serra/`GMS`/zeph1ro) and all the Authors in the `CREDITS` file

