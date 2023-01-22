<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Portfolio Dockerized](#portfolio-dockerized)
  - [Tools Used](#tools-used)
  - [Local development](#local-development)
    - [Prerequisites](#prerequisites)
    - [Environment Variables](#environment-variables)
    - [Build & run service locally](#build--run-service-locally)
    - [Testing](#testing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Portfolio Dockerized

A developer portfolio template build with a dockerized Django web application.

The Hero and About Me sections can be added and removed via the admin page. Skills and projects can also be customized via the admin page.

In case not obvious — this code serves to demonstrate my way of working. I would not necessarily recommend it for a simple portfolio webage like this.

## Tools Used

Below is a list of tools and helpers I used:

- [Ion Icons](https://ionic.io/ionicons) for hambuger menu bar
- [Drawkit](https://www.drawkit.io/) for working man illustration
- [Icon8](https://icons8.com/) for social media and skills icons
- [Animate CSS](https://animate.style/) for Hero section animation
- [Ksound22](https://github.com/Ksound22/developer-portfolio/) template for the front end

## Local development

### Prerequisites

You must have [Docker](https://www.docker.com/) installed.

### Environment Variables

Create an file `.env.local` in the root directory of the repository and add:

```
# Please take care that you do not inadvertently commit any configuration secrets
#
# PROJECT ENVIRONMENT
DEBUG
ENVIRONMENT
ALLOWED_HOSTS
POSTGRES_HOST_AUTH_METHOD
DATABASE_ENGINE
DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD
DATABASE_HOST
DATABASE_PORT
SECRET_KEY
```

### Build & run service locally

Run a web server with this service:

```bash
docker-compose -f docker-compose.dev.yml up
```

You can enter the pod with:

```bash
docker exec -it portfolio-service bash
```

### Testing

Enter the pod and run just `pytest`:

```bash
pytest
```

Or for more granular developing and testing:

```bash
pytest --ds=conf.test_settings -c /dev/null -s
```

You can generate a HTML `coverage` report by running:

```bash
coverage html
```
