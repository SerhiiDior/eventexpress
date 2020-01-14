import os, requests, json, base64
import sys

#get ip address from command line system argument
ip_ad = sys.argv[1]
#string representation
ip_ad_str = ''.join([x for x in ip_ad if x.isnumeric or x == "."])

port_allure = ":5050"
protocol = "http://"

# This directory is where you have all your results locally, generally named as `allure-results`
allureResultsDirectory = '/Reports_Allure'
# This url is where the Allure container is deployed. We are using localhost as example
allureServer = protocol + ip_ad_str + port_allure


currentDirectory = os.path.dirname(os.path.realpath(__file__))
resultsDirectory = currentDirectory + allureResultsDirectory
print('RESULTS DIRECTORY PATH: ' + resultsDirectory)

files = os.listdir(resultsDirectory)

print('FILES:')
results = []
for file in files:
    result = {}

    filePath = resultsDirectory + "/" + file
    print(filePath)

    if os.path.isfile(filePath):
        try:
            with open(filePath, "rb") as f:
                content = f.read()
                if content.strip():
                    b64Content = base64.b64encode(content)
                    result['file_name'] = file
                    result['content_base64'] = b64Content.decode('UTF-8')
                    results.append(result)
                else:
                    print('Empty File skipped: '+ filePath)
        finally :
            f.close()
    else:
        print('Directory skipped: '+ filePath)

headers = {'Content-type': 'application/json'}
requestBody = {
    "results": results
}
jsonRequestBody = json.dumps(requestBody)

response = requests.post(allureServer + '/send-results', headers=headers, data=jsonRequestBody)
print("RESPONSE:")
jsonResponseBody = json.loads(response.content)
jsonPrettierResponseBody = json.dumps(jsonResponseBody, indent=4, sort_keys=True)
print(jsonPrettierResponseBody)
print("STATUS CODE:")
print(response.status_code)
