## _Learning Scrapy_
[![Scrapy Crawl](https://github.com/nickmay645/learning-scrapy/actions/workflows/run_a_crawl.yml/badge.svg)](https://github.com/nickmay645/learning-scrapy/actions/workflows/run_a_crawl.yml)
[![Scrapy Checks](https://github.com/nickmay645/learning-scrapy/actions/workflows/run_checks.yml/badge.svg)](https://github.com/nickmay645/learning-scrapy/actions/workflows/run_checks.yml)

Using this repository to hold all scrapy projects for learning how to use scrapy. 

## Goals

- Create simple spiders that can crawls and parse websites.
- Utilize [Spider Contracts](https://docs.scrapy.org/en/latest/topics/contracts.html#spiders-contracts) to test spiders.
  - Add GitHub actions to check spiders on code pushes to repository.
  - Add custom contracts to create more detailed tesing.
- Use GitHub actions to automate checks on branches before allowing a merge.
- Create custom middleware for spiders to extend funcitonality.
- More TBD.





## Installation

##### This code was built using [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
\
Once python is installed you can create a virtual environment using:
```sh
python -m venv venv
```

You can then upgrade pip and install the requirements using:
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

To run a spider you can navigate to the directory of a scrapy project and call the `scrapy crawl spider_name` command.
```sh
cd worldometers
scrapy crawl countries
```
> Notes: 
Additional arguments to pass into the `crawl` command can be found at https://docs.scrapy.org/en/latest/topics/commands.html#crawl 

To check if a project passes all checks you can navigate to the directory of a scrapy project and call the `scrapy check` command.
```sh
cd worldometers
scrapy check
```
> Notes:
>`scrapy check -l` will list the parse methods checked in the spider.
> `scrapy check --verbose` will provide more detailed info for the checks.
