import json 
import traceback 
from lambdarest import lambda_handler, Response 



######################################### 
############# Ping Route ############### 
######################################### 


@lambda_handler.handle("get", path="/ping")  
def wakeup(event): 
    """ warms up the lambda function """ 
    return Response( 
        body={"status": "alive"}, 
        status_code=200, 
        headers={"Content-Type": "application/json"}, 
    )


######################################### 
############ Message Route ############## 
#########################################  


@lambda_handler.handle("post", path="/message" )
def post_preference(event, user_id, preference_id): 
    return Response( 
        body={"status": "message sent"}, 
        status_code=200, 
        headers={"Content-Type": "application/json"}, 
    )


######################################### 
#### 404 Route If No Routes Matched ##### 
######################################### 

NOT_FOUND_RESPONSE = Response( 
    body={"error_message": "endpoint not found"}, 
    status_code=404, 
    headers={"Content-Type": "application/json"}, 
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
