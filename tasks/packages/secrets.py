import json
import pathlib
import time

from invoke import task

from tasks import snap, apt, files


@task
def pull_secrets(c):
    print(f">>> Please login using the gmail.com e-mail")
    session_token = bw_login(c)

    item_id, attachment_id = bw_find_attachment(c, session_token, "dotfiles")

    bw_download_attachment(c, session_token, item_id, attachment_id, "invoke.yaml.upstream")

    if pathlib.Path("invoke.yaml").exists():
        print(f">>> There is already an invoke.yaml locally, will not overwrite, upstream file saved as 'invoke.yaml.upstream'")
        c.run("diff -q invoke.yaml invoke.yaml.upstream", warn=True)
        c.run("diff -y --suppress-common-lines invoke.yaml invoke.yaml.upstream", pty=True, warn=True)
    else:
        print(f">>> Created invoke.yaml")
        c.run("mv invoke.yaml.upstream invoke.yaml")


@task
def push_secrets(c):
    print(f">>> Please login using the gmail.com e-mail")
    session_token = bw_login(c)

    item_id, attachment_id = bw_find_attachment(c, session_token, "dotfiles")

    bw_download_attachment(c, session_token, item_id, attachment_id, "invoke.yaml.upstream")

    if c.run("diff -q invoke.yaml invoke.yaml.upstream", warn=True):
        print(f">>> Push aborted, file upstream is identical to local.")
        return

    c.run("diff -y --suppress-common-lines invoke.yaml invoke.yaml.upstream", pty=True, warn=True)
    c.run("rm invoke.yaml.upstream")

    confirm = input(">>> You will overwrite upstream, are you sure? [Y/n]: ").strip()

    if confirm == "Y":
        bw_upload_attachment(c, session_token, item_id, attachment_id, "invoke.yaml")
    else:
        print(f">>> Push aborted")


def bw_login(c):
    c.sudo('snap install bw', password=c.config.sudo.password or input(">>> Sudo password: "))

    c.run(f"bw logout", hide=True, warn=True)

    email = input("Bitwarden account email: ")
    password = input("Bitwarden password: ")

    session_token = c.run(f"bw login --raw {email} {password}", hide=True).stdout.strip()
    session_token = c.run(f"bw unlock {password} --raw --session {session_token}", hide=True).stdout.strip()

    return session_token


def bw_find_attachment(c, session_token, search_term):
    item_json = c.run(f"bw list items --search {search_term} --session {session_token}", hide=True).stdout.strip(' []')
    item = json.loads(item_json)
    item_id = item.get("id")
    attachments = item.get("attachments", [])
    secrets_attachment = attachments[0]
    attachment_id = secrets_attachment.get("id")
    return item_id, attachment_id


def bw_download_attachment(c, session_token, item_id, attachment_id, to_path):
    c.run(f"bw get attachment {attachment_id} --output {to_path} --itemid {item_id} --session {session_token}", hide=True)


def bw_upload_attachment(c, session_token, item_id, attachment_id, path):
    c.run(f"bw delete attachment {attachment_id} --itemid {item_id}  --session {session_token}", hide=True)
    c.run(f"bw create attachment --file {path} --itemid {item_id} --session {session_token}", hide=True)


@task
def op(c, op_version='0.10.0'):
    files.curl_download(c,
                        f'https://cache.agilebits.com/dist/1P/op/pkg/v{op_version}/op_linux_amd64_v{op_version}.zip',
                        f'/tmp/op_v{op_version}.zip')
    with c.cd('/tmp/'):
        c.run(f'unzip -o op_v{op_version}.zip')
        c.run('gpg --receive-keys 3FEF9748469ADBE15DA7CA80AC2D62742012EA22')
        c.run('gpg --verify op.sig op && echo "1Password signature verified!"')

    c.sudo('cp /tmp/op /usr/local/bin/op')
