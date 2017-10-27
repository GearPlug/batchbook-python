# Batchbook-python
Batchbook API wrapper written in python.

## Installing
```
pip install git+github.com/GearPlug/batchbook-python.git
```

## Usage
### Simple access with API KEY
```
from typeform.client import Client

client = Client('API_KEY')
```

```
Get Contacts
```
client.get_contacts()
```

Get an specific contact
```
client.get_contact(contact_id)
```
## Requirements

```
-Requests
-Urllib
```

## TODO
- Companies
- Custom Fields
- Users
- Roles
- Communications
