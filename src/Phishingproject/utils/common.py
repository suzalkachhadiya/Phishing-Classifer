import yaml
import os
import json
import joblib
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path
from urllib.parse import urlparse,urlencode
import ipaddress
import re
from bs4 import BeautifulSoup
import whois
import urllib
import urllib.request
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import networkx as nx


from Phishingproject.logging import logger

@ensure_annotations
def read_yaml_file(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """
    Create directories based on the provided path.

    Args:
        path_to_directories (list): The list of path to create directories for.

    Returns:
        None
    """
    try:
        for path in path_to_directories:
            os.makedirs(path,exist_ok=True)
            if verbose:
                logger.info(f"createD Directory at:{path}")
    except Exception as e:
        logger.info(f"Error creating directories: {e}")

@ensure_annotations
def save_json_file(file_path:Path, data:dict):
    """
    Save a dictionary of data as a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data (dict): The dictionary of data to be saved.

    Returns:
        None
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        logger.info(f"Data has been saved to {file_path}")
    except Exception as e:
        logger.info(f"Error saving JSON file: {e}")

@ensure_annotations
def save_txt_file(file_path: Path, report: str):
    try:
        with open(file_path, "w") as file:
            file.write(report)
    except Exception as e:
        logger.info(f"Error saving txt file: {e}")

@ensure_annotations
def save_binary_file(file_path:Path, data:dict):
    """
    Save data as a binary file using joblib.dump().

    Args:
        file_path (str): The path to the binary file.
        data (any): The data to be saved. It can be any Python object that can be serialized by joblib.

    Returns:
        None
    """
    try:
        joblib.dump(data, file_path)
        logger.info(f"Data has been saved to {file_path}")
    except Exception as e:
        raise e
@ensure_annotations    
def load_binary_file(file_path:Path):
    """
    Load data from a binary file using joblib.load().

    Args:
        file_path (str): The path to the binary file.

    Returns:
        object: The loaded data.
    """
    try:
        data = joblib.load(file_path)
        logger.info(f"binary file has been loaded from {file_path}")
        return data
    except Exception as e:
        logger.info(f"Error loading binary file: {e}")
        return None
    
@ensure_annotations
def get_file_size_kb(file_path:Path, min_size=0, max_size=float('inf')):
    """
    Check if the size of a file is within a specified range in kilobytes (KB).

    Args:
        file_path (str): The path to the file.
        min_size (float, optional): The minimum file size in KB. Default is 0.
        max_size (float, optional): The maximum file size in KB. Default is infinity.

    Returns:
        bool: True if the file size is within the specified range, False otherwise.
    """
    try:
        file_size = os.path.getsize(file_path)
        file_size_kb = file_size / 1024  # Convert bytes to kilobytes

        if min_size <= file_size_kb <= max_size:
            return f"{file_size_kb} KB"
        else:
            return False
    except Exception as e:
        logger.info(f"Error checking file size: {e}")
        return False

@ensure_annotations
def havingIP(url):
    try:
        ipaddress.ip_address(url)
        ip = 1
    except:
        ip = 0
    return ip

@ensure_annotations
def haveAtSign(url):
    if "@" in url:
        at = 1
    else:
        at = 0
    return at

@ensure_annotations
def getLength(url):
    if len(url) < 54:
        length = 0
    else:
        length = 1
    return length

@ensure_annotations
def getDepth(url):
    s = urlparse(url).path.split('/')
    depth = 0
    for j in range(len(s)):
        if len(s[j]) != 0:
            depth = depth+1
    return depth

@ensure_annotations
def redirection(url):
    pos = url.rfind('//')
    if pos > 7:
        return 1
    else:
        return 0

@ensure_annotations
def httpDomain(url):
    domain = urlparse(url).netloc
    if 'https' in domain:
        return 1
    else:
        return 0
    
@ensure_annotations
def tinyURL(url):
    shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                    r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                    r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                    r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                    r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                    r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                    r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                    r"tr\.im|link\.zip\.net"
    match=re.search(shortening_services,url)
    if match:
        return 1
    else:
        return 0
    
@ensure_annotations
def prefixSuffix(url):
    if '-' in urlparse(url).netloc:
        return 1            # phishing
    else:
        return 0            # legitimate

@ensure_annotations   
def is_potential_phishing(url, damping_factor=0.85, max_iterations=100, tolerance=0.0001, rank_threshold=100000):
    """
    Estimates if a website is likely phishing based on a simulated rank and Alexa rank limitations (not a definitive indicator).

     Args:
        url (str): The URL of the website to be evaluated.
        damping_factor (float, optional): The damping factor used in the PageRank algorithm. Defaults to 0.85.
        max_iterations (int,  optional): The maximum number of iterations for the algorithm. Defaults to 100.
        tolerance (float, optional): The tolerance for convergence. Defaults to 0.0001.
        rank_threshold (int, optional): The threshold for classifying a website as phishing based on rank. Defaults to 100000.

    Returns:
        int: 1 if the estimated rank is below the threshold (potential phishing), 0 otherwise (not necessarily legitimate).
    """

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract outbound links from the website
        outbound_links = []
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href and not href.startswith('#') and not href.startswith('mailto:'):
                outbound_links.append(href.strip())

        # Create a directed graph representing the link structure
        G = nx.DiGraph()
        G.add_node(url)
        for link in outbound_links:
            G.add_edge(url, link)

        # Simulate PageRank algorithm
        page_ranks = nx.pagerank(G, alpha=damping_factor, max_iter=max_iterations, tol=tolerance)

        # Return phishing prediction based on rank (consider additional checks)
        if url in page_ranks:
            estimated_rank = page_ranks[url]
            return 1 if estimated_rank < rank_threshold else 0
        else:
        # Handle cases where rank estimation fails (consider additional checks)
            print(f"Failed to estimate rank for {url}. Assuming potential phishing.")
            return 1  # Return 1 for failed estimation (potential phishing for safety)

    except Exception as e:
        print(f"Error occurred while evaluating {url}: {e}")
        return 0  # Return 0 on errors (assume non-phishing for safety)

@ensure_annotations 
def domainAge(domain_name):
    creation_date = domain_name.creation_date
    expiration_date = domain_name.expiration_date
    if (isinstance(creation_date,str) or isinstance(expiration_date,str)):
        try:
            creation_date = datetime.strptime(creation_date,'%Y-%m-%d')
            expiration_date = datetime.strptime(expiration_date,"%Y-%m-%d")
        except:
            return 1
    if ((expiration_date is None) or (creation_date is None)):
        return 1
    elif ((type(expiration_date) is list) or (type(creation_date) is list)):
        return 1
    else:
        ageofdomain = abs((expiration_date - creation_date).days)
        if ((ageofdomain/30) < 6):
            age = 1
        else:
            age = 0
    return age

@ensure_annotations
def domainEnd(domain_name):
    expiration_date = domain_name.expiration_date
    if isinstance(expiration_date,str):
        try:
            expiration_date = datetime.strptime(expiration_date,"%Y-%m-%d")
        except:
            return 1
    if (expiration_date is None):
        return 1
    elif (type(expiration_date) is list):
        return 1
    else:
        today = datetime.now()
        end = abs((expiration_date - today).days)
        if ((end/30) < 6):
            end = 0
        else:
            end = 1
    return end

@ensure_annotations
def iframe(response):
  if response == "":
      return 1
  else:
      if re.findall(r"[<iframe>|<frameBorder>]", response.text):
          return 0
      else:
          return 1

@ensure_annotations    
def mouseOver(response):
    if response == "" :
        return 1
    else:
        if re.findall("<script>.+onmouseover.+</script>", response.text):
            return 1
        else:
            return 0

@ensure_annotations
def rightClick(response):
    if response == "":
        return 1
    else:
        if re.findall(r"event.button ?== ?2", response.text):
            return 0
        else:
            return 1
@ensure_annotations  
def forwarding(response):
    if response == "":
        return 1
    else:
        if len(response.history) <= 2:
            return 0
        else:
            return 1