from flask import Flask, render_template, request, Markup
import requests
import backend

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    userData, userRepos = backend.userInfo("nhridoy")

    def prof(userData):
        avatar_url = userData['avatar_url']
        followers = userData['followers']
        following = userData['following']
        html_url = userData['html_url']
        uname = userData['name']
        location = userData['location']
        public_repos = userData['public_repos']
        public_gists = userData['public_gists']
        bio = userData['bio']
        email = userData['email']
        hireable = userData['hireable']
        company = userData['company']
        twitter_username = userData['twitter_username']
        blog = userData['blog']
        created_at = userData['created_at']
        updated_at = userData['updated_at']
        userProfile = Markup(f'''
                <div class="card">
                        <div class="row p-3">
                            <div class="col-md-4 border border-3 border-primary p-3 mb-sm-3">
                                <img src="{avatar_url}" alt=""
                                    class="img-fluid border border-3 border-primary mb-3">
                                <div class="row mb-3 p-3">
                                    <div class="col-md-6 col-sm-6 border border-3 border-primary">
                                        <i class="bi bi-people-fill"></i>
                                        <span>Followers: <strong>{followers}</strong></span>
                                    </div>
                                    <div class="col-md-6 col-sm-6 border border-3 border-primary">
                                        <i class="bi bi-people"></i>
                                        <span>Following: <strong>{following}</strong></span>
                                    </div>
                                </div>

                                <a href="{html_url}" target="_blank" class="d-grid btn btn-success border border-3 border-primary">View in Github</a>
                            </div>
                            <div class="col-md-8">
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Name: <strong>{uname}</strong></p>
                                </div>
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Location: <strong>{location}</strong></p>
                                </div>
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Public Repos: <strong>{public_repos}</strong></p>
                                </div>
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Public Gists: <strong>{public_gists}</strong></p>
                                </div>
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Bio: <strong>{bio}</strong></p>
                                </div>
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Email: <strong>{email}</strong></p>
                                </div>
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Ready to Hire: <strong>{hireable}</strong></p>
                                </div>
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Company: <strong>{company}</strong></p>
                                </div>
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Twitter: <strong>{twitter_username}</strong></p>
                                </div>
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Website: <strong>{blog}</strong></p>
                                </div>
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Account Created: <strong>{created_at}</strong></p>
                                </div>
                                <div class="border border-3 border-primary d-flex align-items-center mb-1">
                                    <p class="m-2">Last Activity: <strong>{updated_at}</strong></p>
                                </div>
                            </div>
                        </div>
                    </div>
                ''')
        return userProfile
    userProfile = prof(userData)
    if request.method == 'POST':
        userName = request.form.get('userName')
        # print(userName)
        userData, userRepos = backend.userInfo(str(userName))
        # print(userData)
        userProfile = prof(userData)
    return render_template("index.html", userData=userData, userRepos=userRepos, userProfile=userProfile)



if __name__ == "__main__":
    # from waitress import serve
    #
    # serve(app)
    app.run(debug=True)
