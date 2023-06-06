from furl import furl

def add_params(url, params):    
    formated_url = furl(url) 
    for k, v in params.items():
        formated_url.args[k] = v
    return formated_url.tostr()