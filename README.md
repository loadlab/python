## LoadLab Python

A wrapper over the Python Requests library to talk to the LoadLab REST API.

## Installation

    $ pip install loadlab
    
## Python Usage

```python
from loadlab import LoadLab

client = LoadLab(token='<YOUR TOKEN HERE>')

# Get Jobs
client.jobs.get()

# Get Plans
client.plans.get()

# Get Sites
client.sites.get()


# Create new job
# Refer to REST API Docs for supported fields
data = {...}
client.jobs.create(**data)

```
## CLI Usage

    $ loadlab --help



