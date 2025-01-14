# asana.ProjectStatusesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_status_for_project**](ProjectStatusesApi.md#create_project_status_for_project) | **POST** /projects/{project_gid}/project_statuses | Create a project status
[**delete_project_status**](ProjectStatusesApi.md#delete_project_status) | **DELETE** /project_statuses/{project_status_gid} | Delete a project status
[**get_project_status**](ProjectStatusesApi.md#get_project_status) | **GET** /project_statuses/{project_status_gid} | Get a project status
[**get_project_statuses_for_project**](ProjectStatusesApi.md#get_project_statuses_for_project) | **GET** /projects/{project_gid}/project_statuses | Get statuses from a project

# **create_project_status_for_project**
> ProjectStatusResponseData create_project_status_for_project(body, project_gid, opt_fields=opt_fields)

Create a project status

*Deprecated: new integrations should prefer the `/status_updates` route.*  Creates a new status update on the project.  Returns the full record of the newly created project status update.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.ProjectStatusesApi(api_client)
body = asana.ProjectGidProjectStatusesBody({"param1": "value1", "param2": "value2",}) # ProjectGidProjectStatusesBody | The project status to create.
project_gid = '1331' # str | Globally unique identifier for the project.
opt_fields = ["author","author.name","color","created_at","created_by","created_by.name","html_text","modified_at","text","title"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create a project status
    api_response = api_instance.create_project_status_for_project(body, project_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectStatusesApi->create_project_status_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectGidProjectStatusesBody**](ProjectGidProjectStatusesBody.md)| The project status to create. | 
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**ProjectStatusResponseData**](ProjectStatusResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_status**
> EmptyResponseData delete_project_status(project_status_gid)

Delete a project status

*Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*  Deletes a specific, existing project status update.  Returns an empty data record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.ProjectStatusesApi(api_client)
project_status_gid = '321654' # str | The project status update to get.

try:
    # Delete a project status
    api_response = api_instance.delete_project_status(project_status_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectStatusesApi->delete_project_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_status_gid** | **str**| The project status update to get. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_status**
> ProjectStatusResponseData get_project_status(project_status_gid, opt_fields=opt_fields)

Get a project status

*Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*  Returns the complete record for a single status update.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.ProjectStatusesApi(api_client)
project_status_gid = '321654' # str | The project status update to get.
opt_fields = ["author","author.name","color","created_at","created_by","created_by.name","html_text","modified_at","text","title"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a project status
    api_response = api_instance.get_project_status(project_status_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectStatusesApi->get_project_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_status_gid** | **str**| The project status update to get. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**ProjectStatusResponseData**](ProjectStatusResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_statuses_for_project**
> ProjectStatusResponseArray get_project_statuses_for_project(project_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get statuses from a project

*Deprecated: new integrations should prefer the `/status_updates` route.*  Returns the compact project status update records for all updates on the project.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.ProjectStatusesApi(api_client)
project_gid = '1331' # str | Globally unique identifier for the project.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["author","author.name","color","created_at","created_by","created_by.name","html_text","modified_at","offset","path","text","title","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get statuses from a project
    api_response = api_instance.get_project_statuses_for_project(project_gid, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectStatusesApi->get_project_statuses_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**ProjectStatusResponseArray**](ProjectStatusResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

