def ssh_command="ssh -o StrictHostKeyChecking=no -l audrey audrey-server.mmcrookshanks.com"
def ssh_command_block_start="ssh -o StrictHostKeyChecking=no -l audrey audrey-server.mmcrookshanks.com <<EOF"
def ssh_command_block_end="EOF"
def init_workspace="""
$ssh_command_block_start
#mkdir /home/audrey/jenkins_workspace
cd /home/audrey/jenkins_workspace
docker compose down
rm -rf ./*
$ssh_command_block_end
"""
def copy_code="""
$ssh_command_block_start
cd /home/audrey/jenkins_workspace
git clone https://github.com/almichaud/jenky-testy.git
mv jenky-testy/* .
$ssh_command_block_end
"""
def build_image="""
$ssh_command_block_start
cd /home/audrey/jenkins_workspace
docker build -t audre-fastapi:1.0 -t audre-fastapi:latest .
$ssh_command_block_end
"""
def run_container="""
$ssh_command_block_start
cd /home/audrey/jenkins_workspace
docker compose up -d
$ssh_command_block_end
"""
def cleanup="""
$ssh_command_block_start

$ssh_command_block_end
"""

node {
    stage ('Initialize Workspace on Audrey Server'){
        sshagent(['audrey-server']) {
            sh "$init_workspace"
        }
    }
    // stage ('Pull From Git'){
    // }
    stage ('Copy Code to Audrey Server'){
        sshagent(['audrey-server']) {
            sh "$copy_code"
        }
    }
    stage ('Build Image/Compile Code'){
        sshagent(['audrey-server']) {
            sh "$build_image"
            // sh "$ssh_command cd /home/audrey/jenkins_workspace & docker build -t audre-fastapi:1.0 -t audre-fastapi:latest ."
        }
    }
    stage ('Run Container/Host Application'){
        sshagent(['audrey-server']) {
            sh "$run_container"
        }
    }
}