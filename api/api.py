import json 
import traceback 
from lambdarest import lambda_handler, Response 

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Method": "GET, POST, OPTIONS, DELETE, PUT",
    "Access-Control-Allow-Headers": "*"
}

######################################### 
############# Ping Route ################ 
######################################### 

@lambda_handler.handle("options", path="/warmup") 
def wakeup_options(event): 
    return Response(
        status_code=200, 
        headers=DEFAULT_HEADERS, 
    ) 

@lambda_handler.handle("get", path="/warmup")  
def wakeup_get(event): 
    """ warms up the lambda function """ 
    return Response( 
        body={"status": "lambda is warm"}, 
        status_code=200, 
        headers=DEFAULT_HEADERS, 
    )


######################################### 
############ Message Route ############## 
#########################################  

@lambda_handler.handle("options", path="/message") 
def message_options(event): 
    return Response(
        status_code=200, 
        headers=DEFAULT_HEADERS, 
    ) 

@lambda_handler.handle("post", path="/message" )
def message_post(event):
    print(event)
    return Response( 
        body={"status": "message sent"}, 
        status_code=200, 
        headers=DEFAULT_HEADERS, 
    )


######################################### 
#### 404 Route If No Routes Matched ##### 
######################################### 

NOT_FOUND_RESPONSE = Response( 
    body={"error_message": "not found"}, 
    status_code=404, 
    headers=DEFAULT_HEADERS, 
) 


@lambda_handler.handle("get", path="/<path:path>") 
def not_found_get_handler(event): 
    return NOT_FOUND_RESPONSE 


@lambda_handler.handle("post", path="/<path:path>") 
def not_found_post_handler(event): 
    return NOT_FOUND_RESPONSE 


@lambda_handler.handle("put", path="/<path:path>") 
def not_found_put_handler(event): 
    return NOT_FOUND_RESPONSE 


@lambda_handler.handle("patch", path="/<path:path>") 
def not_found_patch_handler(event): 
    return NOT_FOUND_RESPONSE 


@lambda_handler.handle("delete", path="/<path:path>") 
def not_found_delete_handler(event): 
    return NOT_FOUND_RESPONSE 
