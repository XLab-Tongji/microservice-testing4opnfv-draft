from flask import Flask, request,render_template
from service_discovery import ServiceDiscover
import yaml
app = Flask(__name__)
CONFIG = {'AMQP_URI': "amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx"}


@app.route('/',methods=['GET'])
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
            'senario_number': step['senario_key'],
            'service': step['service'],
            'description': step['description'],
            'result': result
        })
    return render_template('result.html', results=results),200

app.run(debug=True,port=8080)