import requests
import sys
import webbrowser

if len(sys.argv) != 2:
    print("Expected one argument (the run ID)")
    exit()
run_id = sys.argv[1]
response = requests.get(f'https://api.github.com/repos/openmm/openmm-build-wheels/actions/runs/{run_id}/artifacts')
if response.status_code == 200:
    artifacts = response.json().get('artifacts', [])
    for artifact in artifacts:
        print(f"Downloading {artifact['name']}")
        webbrowser.open(f'https://github.com/openmm/openmm-build-wheels/actions/runs/{run_id}/artifacts/{artifact["id"]}')
else:
    print(f'Error listing artifacts: {response.status_code}')
