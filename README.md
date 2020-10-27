---
### Using Postman newman test in Docker

Current `Dockerfile` used base `node` Image and then installed two modules globally via `npm`. This file also creates a new `WORKDIR` and specifies an `ENTRYPOINT`.  

```bash
FROM node:10.11.0-alpine

RUN npm install -g newman newman-reporter-html

WORKDIR /etc/newman

ENTRYPOINT ["newman"]
```

`docker-compose.yml` file helps to make running the collection easier.
```yml
version: "2"
services:
  postman_checks:
      container_name: restful_booker_checks
      build: .
      image: postman_checks
      command:
        run Restful_Booker_Collection.json
        -e environments/Restful_Booker_Environment.json
        -r html,cli
        --reporter-html-export reports/Restful_Booker_Test_Run.html
        --reporter-html-template reports/templates/customTemplate.hbs
      volumes:
        - ./src:/etc/newman
```

This file contains a few default properties `version` and `services`, these are required to make it a valid `docker-compose` file. Service name of runing docker is `postman_checks`.

There are some additional properties that are specific to collection run:

* `container_name` - Gives the new container a friendly name or it will pick up the default random name
* `build` - This is building from the root dir as this is where my `Dockerfile` is located
* `image` - Same reason for using a `container_name`, this just gives the `image` a name
* `command` - This is the important part, it's the command that tells `newman` where your files are located and what output you would like after the collection run
* `volumes` - This is equally import as it provides a link from the local `./src` dir to the `/etc/newman` dir in the container

---

### Collection Run Output On The Command Line

The default output of using `newman` locally or using the Docker Image, is on the CLI - This will give you a simple breakdown of what happened during the collection run.


### Collection Run HTML Reports

`newman-html-reporter` module are using to generate report.
`-r cli,html` flag should be used to create the report and `--reporter-html-export` tosave it to the `report` directory.

After runing, the new HTML report will be added to the `.src/reports` directory.

It is possible to use `newman` with custom HTML templates in `reports/templates`. It can be customised using the `--reporter-html-template` flag and then passing this a filename.



---

### Using environments variables

`-e` flag can be used to set environment variables in `json` file (`-e environments/env_variables.json`)


---

### Running The Collection

To run this collection from the command line, assuming you have Docker running on your flavour of OS, type the following:

```bash
docker-compose up
```

This _should_ pull the `node` image and install all the needed components, before running through the checks.

Following the collection run, you will still have the `restful_booker_checks` container created, if you wish to removed this, you can use the following command:

```bash
docker-compose rm -f
```
---