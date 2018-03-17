
import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.70.128', port=22, username='gns3', password='gns3')
stdin, stdout, stderr = ssh.exec_command('df -h')
output = stdout.readlines()


if __name__ == "__main__":
    print('\n'.join(output))

