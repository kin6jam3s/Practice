import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.0.2', port=22, username='ronel', password='cisco')
stdin, stdout, stderr = ssh.exec_command('show ip int br')
output = stdout.readlines()


if __name__ == "__main__":
    print('\n'.join(output))

