import logging
import os

logging.basicConfig(level=logging.INFO)

os.environ["API_ID"] = "2303792"
os.environ["API_HASH"] = "1e293b7a2f7a59c6b5819f7bfc29d340"

os.environ[
    "TGCF_CONFIG"
] = """
forwards:
- dest:
  - -1001620411172
  offset: '316'
  source: -1001751290097
plugins: {}
show_forwarded_from: false

"""


from tgcf.config import CONFIG

print(CONFIG)
