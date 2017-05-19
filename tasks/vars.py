import os
import addict
import yaml

from pprint import pprint
from fabric.api import task, env, run, env
from fabric.utils import abort


@task
def show():
    """
    Print all the variables.
    """
    pprint(env)


def load_variables(env_name):

    _update_env(_load_yml_as_addict(os.path.join('vars', 'common.yml')))
    _update_env(_load_yml_as_addict(os.path.join('vars', '{}.yml'.format(env_name))))

    env.env_name = env_name


def _update_env(env_overide):
    """
    fabric.env is a python dict but with dot access.
    We want to allow nested access like: env.db.user_name
    fabric.env only allows one level of dot access. ('env.db' works but 'env.db.host' does not)

    So, we use the addict package, which allows nested dot access.
    So we look at all the keys, and if they are a dict,
    we use .update(), and ensure the value is an instance of an addict.
    """
    for key, val in env_overide.items():
        if (key not in env) or not isinstance(env[key], dict):
            env[key] = val
        else:
            if not isinstance(env[key], addict.Dict):
                env[key] = addict.Dict(env[key])
            env[key].update(val)


def _load_yml_as_addict(file_path):
    if not os.path.isfile(file_path):
        abort('Vars file not found: {0}'.format(file_path))
    with open(file_path, 'r') as content:
        return addict.Dict(yaml.load(content))
