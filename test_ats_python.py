from __future__ import print_function
import time
import json
import MergeATSClient
from MergeATSClient.api import candidates_api
from MergeATSClient.api import applications_api
from MergeATSClient.api import jobs_api
from MergeATSClient.api import passthrough_api
from MergeATSClient.api import available_actions_api
from MergeATSClient.model.paginated_candidate_list import PaginatedCandidateList
#from MergeATSClient.model.patched_create_candidate import PatchedCreateCandidate
#from MergeATSClient.model.patched_create_job import PatchedCreateJob
from MergeATSClient.model.candidate_request import CandidateRequest
from MergeATSClient.model.application_request import ApplicationRequest
from MergeATSClient.model.email_address import EmailAddress

from MergeATSClient.model.data_passthrough import DataPassthrough
from MergeATSClient.model.remote_response import RemoteResponse
from pprint import pprint
# Swap the test key below with your production key from:
# https://app.merge.dev/configuration/keys
configuration = MergeATSClient.Configuration()
configuration.api_key['tokenAuth'] = 'nkc9wDxSQa5pRMWApkN6VyfDYND6DesaAlgkhMoOxUiAqJYEpuDq1Q'
configuration.api_key_prefix['tokenAuth'] = 'Bearer'
api_client = MergeATSClient.ApiClient(configuration)

api_instance = passthrough_api.PassthroughApi(api_client)
c_api_instance = candidates_api.CandidatesApi(api_client)
a_api_instance = available_actions_api.AvailableActionsApi(api_client)
ap_api_instance = applications_api.ApplicationsApi(api_client)

x_account_token = '0ujLbPIWI4BdnjvnrVsVR5c9kra_TGRv8ekuiUfGyZfsEyYS4OwlfA'
"""r = DataPassthrough(method="GET", path="/scooters", data={"a": "b"}, headers={"bbb": "ccc"})
try:
    api_response = a_api_instance.available_actions_retrieve(x_account_token)
    print(api_response)
except MergeATSClient.ApiException as e:
    print("Exception when calling CandidatesApi->candidate_create: %s" % e)

r = DataPassthrough(method="GET", path="/scooters", data={"a": "b"}, headers={"bbb": "ccc"})
try:
    api_response = api_instance.passthrough_create(x_account_token, r)
    print(api_response)
except MergeATSClient.ApiException as e:
    print("Exception when calling CandidatesApi->candidate_create: %s" % e)
    """
try:
    candidate = CandidateRequest(first_name="Dan")
    application = ApplicationRequest()
    application.candidate = candidate
    patch_result = ap_api_instance.applications_create(x_account_token, remote_user_id="abc", application_request=application)
    print(patch_result)
except MergeATSClient.ApiException as e:
    print("Exception when calling CandidatesApi->candidate_create: %s\n" % e)

"""
MergeATSClient.Api.Jobs.jobs_create(MergeATSClient.Connection.new(),"Bearer nkc9wDxSQa5pRMWApkN6VyfDYND6DesaAlgkhMoOxUiAqJYEpuDq1Q" ,"iRrSK0Cn3JAV0Y4kQeaIzgp-j77uNVKmjrbQ7ICs07iY3UOUqVFxyQ", %MergeATSClient.Model.Job{})  
    MergeATSClient.Api.Jobs.jobs_partial_update(MergeATSClient.Connection.new(),"Bearer nkc9wDxSQa5pRMWApkN6VyfDYND6DesaAlgkhMoOxUiAqJYEpuDq1Q" ,"0ujLbPIWI4BdnjvnrVsVR5c9kra_TGRv8ekuiUfGyZfsEyYS4OwlfA", "40c84ed3-5f41-4bec-b1bb-2e33bab4e25a" [{:body, %MergeATSClient.Model.Job{name: "patched with elixir!"}}])"""