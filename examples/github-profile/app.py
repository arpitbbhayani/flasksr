import json
import requests
from flasksr import LayoutSR, Component

from flask import Flask, render_template


app = Flask(__name__)

TOKEN = 'xxx'


def get_repos(git_handle, token, first_n):
    resp = requests.get('https://api.github.com/users/%(git_handle)s/repos?per_page=100' % {'git_handle': git_handle},
                        headers={"Authorization": "token %s" % (token)}).text
    r = json.loads(resp)
    r = sorted(r, key=lambda k: k['stargazers_count'], reverse=True)
    return r[:first_n]


def get_user_details(git_handle, token):
    resp = requests.get('https://api.github.com/users/%(git_handle)s' % {'git_handle': git_handle},
                        headers={"Authorization": "token %s" % (token)}).text
    return json.loads(resp)


def get_user_events(git_handle, token):
    resp = requests.get('https://api.github.com/users/%(git_handle)s/events/public' % {'git_handle': git_handle},
                        headers={"Authorization": "token %s" % (token)}).text
    return json.loads(resp)


def render_page_head_component():
    with app.app_context():
        return render_template('components/page_head.html')


def render_page_end_component():
    with app.app_context():
        return render_template('components/page_end.html')


def render_component_layout():
    with app.app_context():
        return render_template('component_layout.html')


def render_top_menu_component(git_handle):
    user = get_user_details(git_handle, TOKEN)
    with app.app_context():
        return render_template('components/top_menu.html', user=user)


def render_user_events_component(git_handle):
    events = get_user_events(git_handle, TOKEN)
    with app.app_context():
        return render_template('components/user_events.html', events=events)


def render_user_profile_component(git_handle):
    user = get_user_details(git_handle, TOKEN)
    with app.app_context():
        return render_template('components/user_profile.html', user=user)


def render_user_repos_component(git_handle):
    repos = get_repos(git_handle, TOKEN, 5)
    with app.app_context():
        return render_template('components/user_repos.html', repos=repos)


@app.route('/<git_handle>/fast')
def github_profile_fast(git_handle):
    return LayoutSR(
        Component(render_top_menu_component, git_handle),
        Component(render_user_repos_component, git_handle),
        Component(render_user_profile_component, git_handle),
        Component(render_user_events_component, git_handle),
        pre_stream=(Component(render_page_head_component),),
        post_stream=(Component(render_page_end_component),),
        layout=Component(render_component_layout)
    ).response


@app.route('/<git_handle>')
def github_profile(git_handle):
    repos = get_repos(git_handle, TOKEN, 5)
    user = get_user_details(git_handle, TOKEN)
    events = get_user_events(git_handle, TOKEN)
    return render_template('fullpage.html', repos=repos, user=user, events=events)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
