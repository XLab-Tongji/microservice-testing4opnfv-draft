from flask import Flask, request
from service_discovery import ServiceDiscover
import yaml
app = Flask(__name__)
CONFIG = {'AMQP_URI': "amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx"}


@app.route('/index',methods=['GET'])
def index():
    return 'hello word', 200

@app.route('/run_001',methods=['GET'])
def run_test():
    file = open('test_cases/testcase_001.yaml','r')
    test_case = yaml.load(file)
    steps = test_case['orchestration']
    orderedSteps = sorted(steps, key=lambda x: x['order'])
    sd = ServiceDiscover()
    results = []
    for step in orderedSteps:
        service = step['service']
        result = sd.invoke(service)
        results.append({
            'description':step['description'],
            'result':result
        })
    test_results = output(results)
    return test_results,200

def output(results):
    test_result = ''
    for item in results:
        test_result += item['description'] + ', and ' + item['result'] + '<br/>'
    return test_result

app.run(debug=True,port=8080)