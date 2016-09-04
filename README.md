# openstack-project-generator
Sample generator for openstack new projects(Base on openstack stable/liberty version).

## Quick start
Following to generate a new projects:

1. Execute the command to get project of openstack-project-generator as below: 
      git clone https://github.com/JmilkFan/openstack-project-generator.git

2. Get into project-dir:
      cd openstack-project-generator

3. Usage HELP:
      ./generate.sh -h[elp]

4. Generate a new openstack-project with only `API` service:
      ./generate.sh <new_project_name> <new_project_path>

5. Generate a new openstack-project with `API` and `Manager` services:
      ./generate.sh -m <new_manager_service_name> <new_project_name> <new_project_path>

* NOTE
1. The <new_project_name> and <new_manager_service_name> can't be contain a character '-'. EG: the-name is wrong
2. Have to copy the .git directory from openstack-project-generator to <new_projecy_path>/<new_project_name> 
       cp -pr openstack-project-generator/.git <new_project_path>/<new_project_name>


## Install and Run
Install new openstack-project with `openstack-project-generator` for development level:

    sudo pip install -r <new_project_path>/requirements.txt -e <new_project_path>

Following tox commands will be usful for testing and generate config.sample files:
* To generate config.sample files:
      tox -egenconfig
* To run unit test:
      tox -epy27
* To run pep8 test:
      tox -epep8


## License

   Author: Li Xipeng <lixipeng@hihuron.com>
           JmilkFan  <fanguiju@hihuron.com>
           From Beijing Huron Technology Co.Ltd

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
